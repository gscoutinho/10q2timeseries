from sklearn.linear_model import LinearRegression

def corr_df(df, threshold=0.8):
    corr_matrix = df.corr(min_periods=4).fillna(0)
    correlated_pairs = {}

    for col in df.columns:
        correlated_cols = corr_matrix.index[(corr_matrix[col] >= threshold) | (corr_matrix[col] <= -threshold)]
        correlations = corr_matrix[col][correlated_cols].to_dict()
        if correlations:
            correlated_pairs[col] = correlations
    return corr_matrix, correlated_pairs

def fill_lr(df):

    #fill missing 'between' and 'frontier' values with linear interpolation
    df.interpolate(method='linear', limit=4, limit_area='inside', inplace=True)
    df.interpolate(method='linear', limit=2, limit_area='outside', limit_direction='both', inplace=True)
    corr_matrix, corr_pairs = corr_df(df)
    df_raw = df.copy()
    
    for col, correlations in corr_pairs.items():
        correlated_cols = list(correlations.keys())
        #idxs with missing values
        missing_idx = df_raw[df_raw[col].isna()].index

        if missing_idx.empty:
            continue

        for idx in missing_idx:
            df_correlated = df_raw.dropna(axis=0, subset=[col]+correlated_cols)
            
            if df_correlated.empty:
                continue

            X_train = df_correlated[correlated_cols]
            y_train = df_correlated[col]
            X_pred = df_raw.loc[[idx], correlated_cols]

            # Identify columns in X_pred without NaN values
            non_nan_columns = X_pred.columns[~X_pred.iloc[0].isna()]

            # If no columns are left after removing NaNs, skip this index
            if non_nan_columns.empty:
                continue

            # Filter X_train and X_pred to keep only columns without NaNs in X_pred
            X_train_filtered = X_train[non_nan_columns]
            X_pred_filtered = X_pred[non_nan_columns]

            # Ensure X_train_filtered has no NaNs (should be the case if original X_train had no NaNs)
            if X_train_filtered.isnull().values.any():
                # Handle this case as needed
                continue

            # Proceed with model training and prediction
            model = LinearRegression()
            model.fit(X_train_filtered, y_train)
            y_pred = model.predict(X_pred_filtered)

            df_raw.loc[idx, col] = y_pred[0]    
            # Debug: Check the type and shape of df_raw after assignment
    df = df_raw.copy()
    return df

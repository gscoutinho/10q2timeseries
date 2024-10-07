
import pandas as pd

def ten_q_2_df(ten_q, minimum_records):
    #dictionary of dataframes: store every paramter of 10q with cols 'end' and 'val'
    dict_10q = {}
    for param, param_data in ten_q.items():
        for unit, entries in param_data['units'].items():
            if unit != 'USD':
                continue
            else:
                    #store data in a dataframe for the parameter
                    df_entries = pd.DataFrame([{'end':value['end'], 'val': value['val']} for value in entries
                                                    if 'frame' in value and 'val' in value and 'end' in value
                                                    ]).drop_duplicates()
                    #adjust dataframe
                    if not df_entries.empty:
                        dict_10q[param] = df_entries
                        dict_10q[param]['end'] = pd.to_datetime(dict_10q[param]['end'])
                        dict_10q[param].set_index('end', inplace=True)
                        dict_10q[param].sort_index(inplace=True)
    dict_10q_filtered = {k: v for k, v in dict_10q.items() if v['val'].count() >= minimum_records}
    #concatenate dfs
    df_2_concat = []
    for k, df in dict_10q_filtered.items():
        df_renamed = df.rename(columns={'val': k})
        df_2_concat.append(df_renamed)
    
    df_10q = pd.concat(df_2_concat, axis=1, join='outer')
    return df_10q

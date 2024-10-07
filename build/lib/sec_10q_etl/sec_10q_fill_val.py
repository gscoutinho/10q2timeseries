import pandas as pd
from .sec_10q_etl import ten_q_2_df
from sec_10q_data import get_10q_data


df_aapl = ten_q_2_df(get_10q_data('AAPL', 'eng.gabrielcoutinho@outlook.com.br'), 16)

print(df_aapl)




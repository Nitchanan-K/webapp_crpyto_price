import csv
import pandas as pd
from patterns_list import candlestick_patterns
import talib
import os
from flask import Flask, render_template, request

#def get_data():




df_main = pd.DataFrame()
datafiles = os.listdir('dataset/daily')

for filesname in datafiles:
    df = pd.read_csv(f'dataset/daily/{filesname}')
    df.rename(columns={'Unnamed: 0': 'date'}, inplace=True)
    df_main = pd.concat([df_main, df.tail(5)])
ee = 0
result = []
for n in df_main['ticker']:
    ee += 1
    result.append(ee)
    if ee == 5:
        ee = 0
df_main['Result'] = result
df_main['New_col'] = df_main['ticker'] + "-" + df_main['Result'].astype(str)
df_main.set_index('New_col', inplace=True)
print(df_main)










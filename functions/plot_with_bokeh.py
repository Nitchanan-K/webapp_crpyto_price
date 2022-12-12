import talib
import pandas as pd
import os
from math import pi
from math import pi
from bokeh.plotting import figure
from bokeh.io import output_notebook,show
from bokeh.resources import INLINE

# make dataframe
df_main = pd.DataFrame()
datafiles = os.listdir('./dataset/daily')

# test dt
df_new = pd.DataFrame()

for filesname in datafiles:
    df = pd.read_csv(f'./dataset/daily/{filesname}')
    df.rename(columns={'Unnamed: 0': 'date'}, inplace=True)
    df_main = pd.concat([df_main,df.tail(10)])
    ee = 0
    result = []
    for n in df_main['ticker']:
        ee += 1
        result.append(ee)
        if ee == 10:
            ee = 0
    df_main['Result'] = result
    df_main['New_col'] = df_main['ticker'] + "-" + df_main['Result'].astype(str)
    df_main.set_index('New_col', inplace=True)

def make_data_for_plot(crypto_name):
    Open = [df_main.loc[f'{crypto_name}-1']['open'],df_main.loc[f'{crypto_name}-2']['open'],df_main.loc[f'{crypto_name}-3']['open'],df_main.loc[f'{crypto_name}-4']['open'],df_main.loc[f'{crypto_name}-5']['open'],df_main.loc[f'{crypto_name}-6']['open'],df_main.loc[f'{crypto_name}-7']['open'],df_main.loc[f'{crypto_name}-8']['open'],df_main.loc[f'{crypto_name}-9']['open'],df_main.loc[f'{crypto_name}-10']['open']]
    close = [df_main.loc[f'{crypto_name}-1']['close'],df_main.loc[f'{crypto_name}-2']['close'],df_main.loc[f'{crypto_name}-3']['close'],df_main.loc[f'{crypto_name}-4']['close'],df_main.loc[f'{crypto_name}-5']['close'],df_main.loc[f'{crypto_name}-6']['close'],df_main.loc[f'{crypto_name}-7']['close'],df_main.loc[f'{crypto_name}-8']['close'],df_main.loc[f'{crypto_name}-9']['close'],df_main.loc[f'{crypto_name}-10']['close']]
    low = [df_main.loc[f'{crypto_name}-1']['low'],df_main.loc[f'{crypto_name}-2']['low'],df_main.loc[f'{crypto_name}-3']['low'],df_main.loc[f'{crypto_name}-4']['low'],df_main.loc[f'{crypto_name}-5']['low'],df_main.loc[f'{crypto_name}-6']['low'],df_main.loc[f'{crypto_name}-7']['low'],df_main.loc[f'{crypto_name}-8']['low'],df_main.loc[f'{crypto_name}-9']['low'],df_main.loc[f'{crypto_name}-10']['low']]
    high = [df_main.loc[f'{crypto_name}-1']['high'],df_main.loc[f'{crypto_name}-2']['high'],df_main.loc[f'{crypto_name}-3']['high'],df_main.loc[f'{crypto_name}-4']['high'],df_main.loc[f'{crypto_name}-5']['high'],df_main.loc[f'{crypto_name}-6']['high'],df_main.loc[f'{crypto_name}-7']['high'],df_main.loc[f'{crypto_name}-8']['high'],df_main.loc[f'{crypto_name}-9']['high'],df_main.loc[f'{crypto_name}-10']['high']]
    date = [df_main.loc[f'{crypto_name}-1']['date'],df_main.loc[f'{crypto_name}-2']['date'],df_main.loc[f'{crypto_name}-3']['date'],df_main.loc[f'{crypto_name}-4']['date'],df_main.loc[f'{crypto_name}-5']['date'],df_main.loc[f'{crypto_name}-6']['date'],df_main.loc[f'{crypto_name}-7']['date'],df_main.loc[f'{crypto_name}-8']['date'],df_main.loc[f'{crypto_name}-9']['date'],df_main.loc[f'{crypto_name}-10']['date']]
    data_frame = pd.DataFrame({'open':Open,'close':close,'low':low,'high':high,'date':date})
    data_frame['date2'] = pd.to_datetime(data_frame['date'],errors='coerce')

    #print(data_frame)
    return data_frame

def plot_candle_stick(crypto_name):
    data_frame = make_data_for_plot(crypto_name)
    inc = data_frame.close > data_frame.open
    dec = data_frame.open > data_frame.close
    w = 12*60*60*1000 # half day in ms

    TOOLS = "pan,wheel_zoom,box_zoom,reset,save"
    p = figure(x_axis_type="datetime", tools=TOOLS,title="Candles Stick Chart daily timeframe")
    p.xaxis.major_label_orientation = pi/4
    p.grid.grid_line_alpha=0.8

    p.segment (data_frame['date2'],data_frame['high'], data_frame['date2'],data_frame['low'],color = 'black')
    p.vbar(data_frame['date'][inc], w, data_frame['open'][inc], data_frame['close'][inc], fill_color="#D5E1DD", line_color="black")
    p.vbar(data_frame.date2[inc], w, data_frame.open[inc], data_frame.close[inc], fill_color="#30d9a0", line_color="black")
    p.vbar(data_frame.date2[dec], w, data_frame.open[dec], data_frame.close[dec], fill_color="#F2583E", line_color="black")

    #show(p)
    return p


















import streamlit as st
import streamlit.components.v1 as components
import os
import quantstats as qs
import pandas as pd
import numpy as np
from bokeh.plotting import figure
from PIL import Image
from patterns_list import candlestick_patterns
# import talib
import csv
# make dataframe
df_main = pd.DataFrame()
datafiles = os.listdir('./dataset/daily')
for filesname in datafiles:
    df = pd.read_csv(f'./dataset/daily/{filesname}')
    df.rename(columns={'Unnamed: 0': 'date'}, inplace=True)
    df_main = pd.concat([df_main,df.tail(5)])
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
    
# functions

#@st.cache
def load_data(data_name):
    data = qs.utils.download_returns(f'{data_name}')
    return data


def plot_with_quant(data_name,plot_name):
    data_dt = qs.utils.download_returns(f'{data_name}')
    import functions.plot_with_quant
    functions.plot_with_quant.plot_data(data_name,plot_name,data_dt)


def plot_full_report(data_name):
    import functions.create_full_report
    print(data_name)
    functions.create_full_report.create_report(data_name)
 


def plot_benchmark_report(data_name,benchmark_name):
    import functions.create_benchmark_report
    print(data_name)
    functions.create_benchmark_report.create_benchmark_report(data_name,benchmark_name)


# set title
st.title('Test WebAPP With QuantStats')

# Dict
crypto_dict = {}

# expander Plot Data
with st.expander("Plot Data"):
    # select box crypto name
    import crypto_names
    select_crypto_name = st.selectbox('Select Crypto Name', crypto_names.crypto_name_tuple
                                      )
    # select widget box plot type
    import plot_type_name
    select_plot_type = st.selectbox('Select Plot Type',plot_type_name.plot_type_name_tuple
                                   )

    # sub header
    st.subheader(f'{select_crypto_name} - {select_plot_type}')

    # plot widget button

    if st.button('Plot Data'):
        plot_with_quant(select_crypto_name, select_plot_type)

        image = Image.open(f'output_plot/{select_plot_type}-{select_crypto_name}.png')
        st.image(image, caption=f'{select_plot_type} of {select_crypto_name}.')

        # widget save button
        with open(f'output_plot/{select_plot_type}-{select_crypto_name}.png',"rb") as file:
            save_png_button = st.download_button(
                label="Download Image",
                data=file,
                file_name=f'{select_plot_type}-{select_crypto_name}.png',
                mime="image/png"
            )

with st.expander("Full Report"):

    # Default Report
    default_title = '<p style="font-family:Helvetica; color:Black; font-size: 25px;">Default Report</p>'
    st.markdown(default_title, unsafe_allow_html=True)

    # select box for crypto name
    select_crypto_name_report = st.selectbox('Select Crypto For analyze', crypto_names.crypto_name_tuple
                                      )
    # sub header
    st.subheader(f'{select_crypto_name_report}')
    # plot default report
    if st.button('Create Full Report'):
        plot_full_report(select_crypto_name_report)
        tearsheet = open("quantstats-tearsheet.html")
        components.html(tearsheet.read(),height=1000,width=700,scrolling=True)

    # Benchmark Report
    original_title = '<p style="font-family:Helvetica; color:Black; font-size: 25px;">Benchmark Report</p>'
    st.markdown(original_title, unsafe_allow_html=True)

    # select benchmark box
    select_benchmark_crypto = st.selectbox('VS Benchmark',crypto_names.crypto_name_tuple
                                   )
    # sub header
    st.subheader(f'{select_crypto_name_report} | vs | {select_benchmark_crypto}')

    # plot benchmark report
    if st.button('Create Benchmark Report'):
        plot_benchmark_report(select_crypto_name_report,select_benchmark_crypto)
        tearsheet_benchmark = open("quantstats-tearsheet.html")
        components.html(tearsheet_benchmark.read(), height=1000, width=700, scrolling=True)



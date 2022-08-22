import streamlit as st
import streamlit.components.v1 as components
import os
import quantstats as qs
import pandas as pd
import numpy as np
from bokeh.plotting import figure
from PIL import Image


# functions

@st.cache
def load_data(data_name):
    data = qs.utils.download_returns(f'{data_name}')
    return data


def plot_with_quant(data_name,plot_name):
    data_dt = qs.utils.download_returns(f'{data_name}')
    import functions.plot_with_quant
    functions.plot_with_quant.plot_data(data_name,plot_name,data_dt)


def plot_full_report(data_name):
    data_dt = qs.utils.download_returns(f'{data_name}')
    import functions.create_full_report
    functions.create_full_report.create_report(data_name,data_dt)


def plot_benchmark_report(data_name):
    data_dt = qs.utils.download_returns(f'{data_name}')
    import functions.create_benchmark_report
    functions.create_benchmark_report.create_benchmark_report(data_name,data_dt,benchmark=select_benchmark_crypto)

# set title
st.title('Test WebAPP With QuantStats')




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
        os.remove("quantstats-tearsheet.html")
        plot_benchmark_report(select_crypto_name_report)
        tearsheet_benchmark = open("quantstats-tearsheet.html")
        components.html(tearsheet_benchmark.read(), height=1000, width=700, scrolling=True)


# expander Show Return %
with st.expander("Show Return %"):
    # load data button
    if st.button('Download Data Return %'):
        st.write(load_data(select_crypto_name))










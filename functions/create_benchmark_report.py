import quantstats as qs
# import streamlit as st
# import streamlit.components.v1 as components
# import quantstats as qs
# import pandas as pd
# import numpy as np
# from bokeh.plotting import figure
# from PIL import Image
# from patterns_list import candlestick_patterns

def create_benchmark_report(dataname,benchmark):
    
    stock = qs.utils.download_returns(dataname)
    bench = qs.utils.download_returns(benchmark)

    stock.index = stock.index.tz_convert(None)
    bench.index = bench.index.tz_convert(None)
    print(stock)
    qs.reports.html(stock, mode='full', benchmark=bench ,output='output_plot/test12_report.html',title=f"{dataname} VS {benchmark}")
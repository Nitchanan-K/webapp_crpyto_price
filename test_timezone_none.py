import streamlit as st
import streamlit.components.v1 as components
import os
import quantstats as qs
import pandas as pd
import numpy as np
from bokeh.plotting import figure
from PIL import Image
from patterns_list import candlestick_patterns


def test_plot(dataname):

    stock = qs.utils.download_returns(dataname)
    bench = qs.utils.download_returns("ETH-USD")

    stock.index = stock.index.tz_convert(None)
    bench.index = bench.index.tz_convert(None)

    qs.reports.html(stock, mode='full', benchmark=bench ,output='output/test12_report.html',title=f"{dataname}")
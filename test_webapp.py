import streamlit as st
import quantstats as qs
import pandas as pd
import numpy as np
from bokeh.plotting import figure
from PIL import Image

# set title
st.title('Test WebAPP With QuantStats')

@st.cache
def load_data(data_name):
    data = qs.utils.download_returns(f'{data_name}')
    return data

@st.cache
def plot_with_quant(data_name,plot_name):
    data_dt = qs.utils.download_returns(f'{data_name}')

    if plot_name == 'daily_returns':
        qs.plots.monthly_heatmap(data_dt,savefig=f'output_plot/daily_returns-{data_name}')
    elif plot_name == 'drawdown':
        qs.plots.drawdown(data_dt,savefig=f'output_plot/drawdown-{data_name}')
    elif plot_name == 'monthly_heatmap':
        qs.plots.monthly_heatmap(data_dt,savefig=f'output_plot/monthly_heatmap-{data_name}')
    elif plot_name == 'distribution':
        qs.plots.distribution(data_dt,savefig=f'output_plot/distribution-{data_name}')
    elif plot_name == 'drawdowns_periods':
        qs.plots.drawdowns_periods(data_dt,savefig=f'output_plot/drawdowns_periods-{data_name}')
    elif plot_name == 'earnings':
        qs.plots.earnings(data_dt,savefig=f'output_plot/earnings-{data_name}')
    elif plot_name == 'histogram':
        qs.plots.histogram(data_dt,savefig=f'output_plot/histogram-{data_name}')
    elif plot_name == 'log_returns':
        qs.plots.log_returns(data_dt,savefig=f'output_plot/log_returns-{data_name}')
    elif plot_name == 'returns':
        qs.plots.returns(data_dt,savefig=f'output_plot/returns-{data_name}')
    #elif plot_name == 'rolling_beta':
        #qs.plots.rolling_beta(data_dt,savefig=f'output_plot/rolling_beta{data_name}')
    elif plot_name == 'rolling_sharpe':
        qs.plots.rolling_sharpe(data_dt,savefig=f'output_plot/rolling_sharpe-{data_name}')
    elif plot_name == 'rolling_sortino':
        qs.plots.rolling_sortino(data_dt,savefig=f'output_plot/rolling_sortino-{data_name}')
    elif plot_name == 'rolling_volatility':
        qs.plots.rolling_volatility(data_dt,savefig=f'output_plot/rolling_volatility-{data_name}')
    elif plot_name == 'snapshot':
        qs.plots.snapshot(data_dt,savefig=f'output_plot/snapshot-{data_name}')
    elif plot_name == 'yearly_returns':
        qs.plots.yearly_returns(data_dt,savefig=f'output_plot/yearly_returns-{data_name}')

# select box crypto name
select_crypto_name = st.selectbox('Select Crypto Name',
                                      ('BTC-USD', "ETH-USD", 'USDT-USD', 'USDC-USD', 'BNB-USD', 'BUSD-USD', 'XRP-USD', 'ADA-USD', 'SOL-USD', 'DOGE-USD', 'HEX-USD', 'DAI-USD', 'DOT-USD',
                                       'WTRX-USD', 'MATIC-USD', 'TRX-USD', 'AVAX-USD', 'SHIB-USD', 'WBTC-USD', 'STETH-USD',
                                       'LEO-USD', 'YOUC-USD', 'LTC-USD', 'FTT-USD', 'ETC-USD', 'CRO-USD', 'LINK-USD', 'NEAR-USD', 'ATOM-USD', 'XLM-USD', 'XMR-USD', 'BCH-USD', 'BTCB-USD',
                                       'ALGO-USD', 'XCN1-USD', 'APE3-USD', 'VET-USD', 'FLOW-USD', 'MANA-USD', 'ICP-USD',
                                       'SAND-USD', 'FRAX-USD', 'HBAR-USD', 'XTZ-USD', 'FIL-USD', 'AXS-USD', 'TUSD-USD', 'THETA-USD', 'EGLD-USD', 'AAVE-USD', 'WBNB-USD', 'EOS-USD',
                                       'HNT-USD', 'QNT-USD', 'TONCOIN-USD', 'BSV-USD', 'USDP-USD', 'KCS-USD', 'OKB-USD', 'BTT-USD', 'MKR-USD', 'HBTC-USD', 'BTT2-USD', 'ZEC-USD',
                                       'RUNE-USD', 'FTM-USD', 'MIOTA-USD', 'XEC-USD', 'USDN-USD', 'KLAY-USD', 'USDD-USD', 'MV-USD',
                                       'GRT1-USD', 'HT-USD', 'NEO-USD', 'CHZ-USD', 'CRV-USD', "LUNA1-USD", 'PAXG-USD', 'DFI-USD', 'GMT3-USD', 'BAT-USD', 'WAVES-USD', 'STX-USD',
                                       'KSM-USD', 'LRC-USD', 'DASH-USD', 'ZIL-USD', 'ENJ-USD', 'CAKE-USD', 'FRTS-USD', 'LDO-USD', 'XAUT-USD', 'CVX-USD', 'FEI-USD', 'AR-USD',
                                       'XEM-USD', 'MINA-USD', 'KAVA-USD'
                                      ))

with st.expander("Plot Data"):
    # select box plot type
    select_plot_type = st.selectbox('Select Plot Type',
                                    ('daily_returns', 'distribution', 'drawdown', 'drawdowns_periods', 'earnings',
                                     'histogram', 'log_returns', 'monthly_heatmap', 'returns',
                                     'rolling_sharpe',
                                     'rolling_sortino', 'rolling_volatility', 'snapshot', 'yearly_returns')
                                    ) #'rolling_beta',
    # plot button
    if st.button('Plot Heatmap'):
        plot_with_quant(select_crypto_name, select_plot_type)

        image = Image.open(f'output_plot/{select_plot_type}-{select_crypto_name}.png')
        st.image(image, caption=f'{select_plot_type} of {select_crypto_name}.')

with st.expander("Show Return %"):
    # load data button
    if st.button('Download Data Return %'):
        st.write(load_data(select_crypto_name))










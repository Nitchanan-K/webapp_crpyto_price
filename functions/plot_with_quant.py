import quantstats as qs

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
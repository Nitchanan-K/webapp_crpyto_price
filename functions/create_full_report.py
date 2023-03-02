import quantstats as qs

def create_report(dataname,date_dt):
    #qs.reports.full(date_dt)
    #qs.reports.html(date_dt,dataname,title=f'{dataname}Report Investments', output='output/BTC_report.html', mode='full')
    """, title=f'{dataname} Report Investments', output='output/BTC_report.html', mode='full'"""
    """using qs.reports.html"""
    qs.reports.plots(date_dt, mode='full')

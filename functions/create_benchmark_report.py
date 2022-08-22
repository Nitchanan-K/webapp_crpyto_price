import quantstats as qs
def create_benchmark_report(dataname,date_dt,benchmark):
    qs.reports.html(date_dt,benchmark,title=f'{dataname} Report Investments', output='output/BTC_report.html', mode='full')
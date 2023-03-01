import quantstats as qs

def create_report(dataname,date_dt):
    print(dataname,date_dt)
    qs.reports.html(date_dt, title=f'{dataname} Report Investments', output='output/BTC_report.html', mode='full')

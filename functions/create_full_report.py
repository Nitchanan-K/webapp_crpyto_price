import quantstats as qs

def create_report(dataname,date_dt):
    print(dataname,date_dt)
    qs.reports.full(date_dt)

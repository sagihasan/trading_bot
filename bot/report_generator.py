import pandas as pd
import datetime

# פונקציה ליצירת דוח שבועי
def generate_weekly_report():
    df = pd.read_excel('trade_management_log.xlsx')
    df['report_date'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    df.to_excel('weekly_report.xlsx', index=False)

# פונקציה ליצירת דוח חודשי
def generate_monthly_report():
    df = pd.read_excel('trade_management_log.xlsx')
    df['report_date'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    df.to_excel('monthly_report.xlsx', index=False)

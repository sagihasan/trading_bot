import schedule
import time
from report_generator import generate_weekly_report, generate_monthly_report

def start_report_scheduler():
    # שליחת דוח שבועי כל שבת ב-12:00 בצהריים
    schedule.every().saturday.at("12:00").do(generate_weekly_report)

    # שליחת דוח חודשי כל 1 לחודש ב-12:00 בצהריים
    schedule.every().month.at("12:00").do(generate_monthly_report)

    while True:
        schedule.run_pending()
        time.sleep(1)

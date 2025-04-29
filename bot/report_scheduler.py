import schedule
import time
import datetime
from report_generator import generate_weekly_report, generate_monthly_report
from utils.alert_manager import send_discord_file, mark_alert_sent
from config import private_webhook

def send_monthly_report():
    # שליחת דו"ח חודשי רק אם היום הוא הראשון לחודש
    if datetime.datetime.now().day != 1:
        return

    try:
        generate_monthly_report()
        send_discord_file(private_webhook, "monthly_report.xlsx")
        mark_alert_sent("monthly_sent")
    except Exception as e:
        print(f"שגיאה בשליחת הדו\"ח החודשי: {e}")

def start_report_scheduler():
    # שליחת דו"ח שבועי כל שבת ב־12:00 בצהריים
    schedule.every().saturday.at("12:00").do(generate_weekly_report)

    # שליחת דו"ח חודשי (תנאי ל־1 לחודש כל יום ב־12:00)
    schedule.every().day.at("12:00").do(send_monthly_report)

    while True:
        schedule.run_pending()
        time.sleep(1)

import schedule
import time
import os
from report_generator import generate_weekly_report, generate_monthly_report

# שליפת Webhook מהסביבה
private_webhook = os.getenv("DISCORD_PRIVATE_WEBHOOK")

def start_report_scheduler():
    # שליחת דוח שבועי כל שבת ב־12:00 בצהריים
    schedule.every().saturday.at("12:00").do(generate_weekly_report)

    # שליחת דוח חודשי כל 1 לחודש ב־12:00 בצהריים
    schedule.every().day.at("12:00").do(send_monthly_report)

    while True:
        schedule.run_pending()
        time.sleep(1)

def send_monthly_report():
    generate_monthly_report()
    send_discord_message(private_webhook, "הבוט שלח דוח חודשי אוטומטי")

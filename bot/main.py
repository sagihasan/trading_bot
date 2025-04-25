import os
import requests
from dotenv import load_dotenv
from datetime import datetime
import pytz

from keep_alive.keep_alive import keep_alive
from utils.helpers import example_helper
from macro.macro_analyzer import analyze_macro
from reports.weekly_report_generator import generate_report

# טוען משתני סביבה
load_dotenv()

# הגדרת Webhooks
private_webhook = os.getenv("DISCORD_PRIVATE_WEBHOOK")
public_webhook = os.getenv("DISCORD_PUBLIC_WEBHOOK")

# הגדרת מפתחות API
alpha_vantage_key = os.getenv("API_ALPHA_VANTAGE_KEY")
news_api_key = os.getenv("API_NEWS_KEY")

# שליחת הודעה לדיסקורד
def send_discord_message(webhook_url, message):
    data = {"content": message}
    try:
        response = requests.post(webhook_url, json=data)
        if response.status_code == 204:
            print(f"הודעה נשלחה בהצלחה ל־Webhook: {webhook_url}")
        else:
            print(f"שגיאה בשליחה ל־Webhook: {webhook_url} – קוד: {response.status_code}")
    except Exception as e:
        print(f"שגיאה בשליחת הודעה לדיסקורד: {e}")

# הרצת הבוט
def run_bot():
    # קבלת שעה לפי שעון ישראל
    israel_tz = pytz.timezone('Asia/Jerusalem')
    now = datetime.now(israel_tz)
    current_hour = now.hour

    # שליחת הודעה רק בזמנים מתאימים
    if 10 <= current_hour < 12:
        send_discord_message(private_webhook, "הבוט התחיל לפעול (ערוץ פרטי)")
    elif 1 <= current_hour < 3:
        send_discord_message(private_webhook, "סיום פעילות הבוט (ערוץ פרטי)")

    print("...הבוט מתחיל לפעול")
    helper_result = example_helper()
    print("Helper:", helper_result)

    macro_data = analyze_macro()
    print("מאקרו:", macro_data)

    generate_report()
    print("שלח דוח שבועי")

# הרצת הקוד
if __name__ == "__main__":
    keep_alive()
    run_bot()

# בדיקת משתנים (רק למסוף)
print("בודק Webhook ציבורי...")
print("Webhook ציבורי:", "קיים" if public_webhook else "לא נמצא")

print("בודק Webhook פרטי...")
print("Webhook פרטי:", "קיים" if private_webhook else "לא נמצא")

print("בודק מפתח Alpha Vantage...")
print("Alpha Vantage:", "קיים" if alpha_vantage_key else "לא נמצא")

print("בודק מפתח NewsAPI...")
print("NewsAPI:", "קיים" if news_api_key else "לא נמצא")

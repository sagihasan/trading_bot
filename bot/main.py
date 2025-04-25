import os
import requests
from dotenv import load_dotenv

from keep_alive.keep_alive import keep_alive
from utils.helpers import example_helper
from macro.macro_analyzer import analyze_macro
from reports.weekly_report_generator import generate_report

# הפעלת שרת לשמירה על הרצה (Replit / Render)
keep_alive()

# טען משתנים מקובץ .env (אם קיים)
load_dotenv()

# משתני Webhook
private_webhook = os.getenv("DISCORD_PRIVATE_WEBHOOK")
public_webhook = os.getenv("DISCORD_PUBLIC_WEBHOOK")

# מפתחות API
alpha_vantage_key = os.getenv("API_ALPHA_VANTAGE_KEY")
news_api_key = os.getenv("API_NEWS_KEY")

# פונקציה לשליחת הודעה לדיסקורד
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
    send_discord_message(private_webhook, "(הבוט התחיל לפעול (ערוץ פרטי")
    
    print("...הבוט מתחיל לפעול")
    helper_result = example_helper()
    print("Helper:", helper_result)

    macro_data = analyze_macro()
    print("מאקרו:", macro_data)

    generate_report()
    print("שלח דוח שבועי")

    send_discord_message(private_webhook, "(סיום פעילות הבוט (ערוץ פרטי")

# הפעלה אם זה הקובץ הראשי
if __name__ == "__main__":
    keep_alive()
    run_bot()

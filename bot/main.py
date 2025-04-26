import os
import requests
from dotenv import load_dotenv
from datetime import datetime
import pytz

from keep_alive.keep_alive import keep_alive
from utils.helpers import example_helper
from macro.macro_analyzer import analyze_macro
from reports.weekly_report_generator import generate_report
from signals.signals_engine import run_signals_engine
from trade_management import manage_trade

# טען משתנים מקובץ .env
load_dotenv()

# קבלת ה-Webhook מהסביבה
private_webhook = os.getenv('DISCORD_PRIVATE_WEBHOOK')
public_webhook = os.getenv('DISCORD_PUBLIC_WEBHOOK')
alpha_vantage_key = os.getenv('API_ALPHA_VANTAGE_KEY')
news_api_key = os.getenv('API_NEWS_KEY')

# פונקציה לשליחת הודעה לדיסקורד
def send_discord_message(webhook_url, message):
    data = {"content": message}
    try:
        response = requests.post(webhook_url, json=data)
        if response.status_code != 204:
            print(f"שגיאה בשליחת הודעה לדיסקורד: {response.status_code}")
    except Exception as e:
        print(f"שגיאה בשליחת הודעה לדיסקורד: {e}")

# פונקציה להרצת הבוט
def run_bot():
    israel_tz = pytz.timezone('Asia/Jerusalem')
    now = datetime.now(israel_tz)
    current_hour = now.hour
    current_minute = now.minute

    if 10 <= current_hour < 12:
        send_discord_message(private_webhook, "(הבוט התחיל לפעול - ערוץ פרטי)")
    elif 1 <= current_hour < 3:
        send_discord_message(private_webhook, "(סיום פעילות הבוט - ערוץ פרטי)")
    elif current_hour == 22 and 40 <= current_minute < 45:
        print("...והגיע 22:40 - מפעיל מנוע איתותים")
        run_signals_engine()

    # ריצה רגילה
    print("הבוט מתחיל לפעול...")
    helper_result = example_helper()
    print("Helper:", helper_result)

    macro_data = analyze_macro()
    print("מאקרו:", macro_data)

    generate_report()
    print("שלח דוח שבועי")

    # רשימת עסקאות פתוחות לדוגמה
    open_trades = [
        {
            "symbol": "AAPL",
            "entry_price": 150,
            "current_price": 155,
            "stop_loss": 145,
            "take_profit": 165,
            "direction": "long"
        },
        {
            "symbol": "TSLA",
            "entry_price": 700,
            "current_price": 680,
            "stop_loss": 670,
            "take_profit": 750,
            "direction": "short"
        },
        {
            "symbol": "PLTR",
            "entry_price": 10,
            "current_price": 11,
            "stop_loss": 9.5,
            "take_profit": 12,
            "direction": "long"
        }
        # אפשר להוסיף כאן עוד עסקאות
    ]

    # מעבר על כל המניות וניהול עסקאות
    for trade in open_trades:
        manage_trade(trade, public_webhook)

# הפעלת הבוט
if __name__ == "__main__":
    keep_alive()
    run_bot()import os
import requests
from dotenv import load_dotenv
from datetime import datetime
import pytz

from keep_alive.keep_alive import keep_alive
from utils.helpers import example_helper
from macro.macro_analyzer import analyze_macro
from reports.weekly_report_generator import generate_report
from signals.signals_engine import run_signals_engine
from trade_management import manage_trade

# טען משתנים מקובץ .env
load_dotenv()

# קבלת ה-Webhook מהסביבה
private_webhook = os.getenv('DISCORD_PRIVATE_WEBHOOK')
public_webhook = os.getenv('DISCORD_PUBLIC_WEBHOOK')
alpha_vantage_key = os.getenv('API_ALPHA_VANTAGE_KEY')
news_api_key = os.getenv('API_NEWS_KEY')

# פונקציה לשליחת הודעה לדיסקורד
def send_discord_message(webhook_url, message):
    data = {"content": message}
    try:
        response = requests.post(webhook_url, json=data)
        if response.status_code != 204:
            print(f"שגיאה בשליחת הודעה לדיסקורד: {response.status_code}")
    except Exception as e:
        print(f"שגיאה בשליחת הודעה לדיסקורד: {e}")

# פונקציה להרצת הבוט
def run_bot():
    israel_tz = pytz.timezone('Asia/Jerusalem')
    now = datetime.now(israel_tz)
    current_hour = now.hour
    current_minute = now.minute

    if 10 <= current_hour < 12:
        send_discord_message(private_webhook, "(הבוט התחיל לפעול - ערוץ פרטי)")
    elif 1 <= current_hour < 3:
        send_discord_message(private_webhook, "(סיום פעילות הבוט - ערוץ פרטי)")
    elif current_hour == 22 and 40 <= current_minute < 45:
        print("...והגיע 22:40 - מפעיל מנוע איתותים")
        run_signals_engine()

    # ריצה רגילה
    print("הבוט מתחיל לפעול...")
    helper_result = example_helper()
    print("Helper:", helper_result)

    macro_data = analyze_macro()
    print("מאקרו:", macro_data)

    generate_report()
    print("שלח דוח שבועי")

    # רשימת עסקאות פתוחות לדוגמה
    open_trades = [
        {
            "symbol": "AAPL",
            "entry_price": 150,
            "current_price": 155,
            "stop_loss": 145,
            "take_profit": 165,
            "direction": "long"
        },
        {
            "symbol": "TSLA",
            "entry_price": 700,
            "current_price": 680,
            "stop_loss": 670,
            "take_profit": 750,
            "direction": "short"
        },
        {
            "symbol": "PLTR",
            "entry_price": 10,
            "current_price": 11,
            "stop_loss": 9.5,
            "take_profit": 12,
            "direction": "long"
        }
        # אפשר להוסיף כאן עוד עסקאות
    ]

    # מעבר על כל המניות וניהול עסקאות
    for trade in open_trades:
        manage_trade(trade, public_webhook)

# הפעלת הבוט
if __name__ == "__main__":
    keep_alive()
    run_bot()

import os
import requests
from datetime import datetime
import pytz
from dotenv import load_dotenv
from trade_management import log_trade_update

# טעינת קובץ .env (אם יש)
load_dotenv()

# טעינת Webhooks מהסביבה
private_webhook = os.getenv('DISCORD_PRIVATE_WEBHOOK')
public_webhook = os.getenv('DISCORD_PUBLIC_WEBHOOK')
error_webhook = os.getenv('DISCORD_ERROR_WEBHOOK')

# פונקציה לשליחת הודעה לדיסקורד
def send_discord_message(webhook_url, message):
    data = {"content": message}
    try:
        response = requests.post(webhook_url, json=data)
        if response.status_code != 204:
            print(f"שגיאה בשליחת הודעה לדיסקורד: {response.status_code}")
    except Exception as e:
        print(f"שגיאה בשליחת הודעה לדיסקורד: {e}")
# רשימת עסקאות פתוחות - 118 מניות
open_trades = [
    {"symbol": "PLTR", "entry_price": 20, "current_price": 21, "stop_loss": 19, "take_profit": 23, "direction": "long"},
    {"symbol": "AMZN", "entry_price": 3200, "current_price": 3250, "stop_loss": 3150, "take_profit": 3350, "direction": "long"},
    {"symbol": "NVDA", "entry_price": 600, "current_price": 620, "stop_loss": 580, "take_profit": 650, "direction": "long"},
    {"symbol": "AAPL", "entry_price": 175, "current_price": 178, "stop_loss": 170, "take_profit": 185, "direction": "long"},
    {"symbol": "TSLA", "entry_price": 650, "current_price": 640, "stop_loss": 670, "take_profit": 610, "direction": "short"},
    {"symbol": "ANET", "entry_price": 180, "current_price": 185, "stop_loss": 175, "take_profit": 190, "direction": "long"},
    {"symbol": "SNEX", "entry_price": 90, "current_price": 92, "stop_loss": 87, "take_profit": 95, "direction": "long"},
    {"symbol": "CRGY", "entry_price": 15, "current_price": 16, "stop_loss": 14, "take_profit": 17, "direction": "long"},
    {"symbol": "MSFT", "entry_price": 300, "current_price": 310, "stop_loss": 290, "take_profit": 320, "direction": "long"},
    {"symbol": "GOOG", "entry_price": 140, "current_price": 145, "stop_loss": 135, "take_profit": 150, "direction": "long"},
    {"symbol": "AMD", "entry_price": 120, "current_price": 125, "stop_loss": 115, "take_profit": 130, "direction": "long"},
    {"symbol": "ADBE", "entry_price": 550, "current_price": 560, "stop_loss": 530, "take_profit": 580, "direction": "long"},
    {"symbol": "META", "entry_price": 330, "current_price": 340, "stop_loss": 320, "take_profit": 350, "direction": "long"},
    {"symbol": "AI", "entry_price": 30, "current_price": 32, "stop_loss": 28, "take_profit": 35, "direction": "long"},
    {"symbol": "AR", "entry_price": 12, "current_price": 13, "stop_loss": 11, "take_profit": 14, "direction": "long"},
    {"symbol": "ALSN", "entry_price": 60, "current_price": 62, "stop_loss": 58, "take_profit": 65, "direction": "long"},
    {"symbol": "ASGN", "entry_price": 85, "current_price": 88, "stop_loss": 82, "take_profit": 92, "direction": "long"},
    {"symbol": "HIMS", "entry_price": 10, "current_price": 11, "stop_loss": 9, "take_profit": 12, "direction": "long"},
    {"symbol": "ASTS", "entry_price": 7, "current_price": 7.5, "stop_loss": 6.5, "take_profit": 8, "direction": "long"},
    {"symbol": "HOOD", "entry_price": 12, "current_price": 13, "stop_loss": 11.5, "take_profit": 14, "direction": "long"},
    {"symbol": "DKNG", "entry_price": 25, "current_price": 26, "stop_loss": 24, "take_profit": 28, "direction": "long"},
    {"symbol": "SOUN", "entry_price": 4, "current_price": 4.2, "stop_loss": 3.8, "take_profit": 4.5, "direction": "long"},
    {"symbol": "APP", "entry_price": 60, "current_price": 62, "stop_loss": 58, "take_profit": 65, "direction": "long"},
    {"symbol": "PZZA", "entry_price": 70, "current_price": 72, "stop_loss": 68, "take_profit": 75, "direction": "long"},
    {"symbol": "AVGO", "entry_price": 850, "current_price": 860, "stop_loss": 830, "take_profit": 880, "direction": "long"},
    {"symbol": "SMCI", "entry_price": 900, "current_price": 920, "stop_loss": 880, "take_profit": 950, "direction": "long"},
    {"symbol": "ADI", "entry_price": 190, "current_price": 195, "stop_loss": 185, "take_profit": 200, "direction": "long"},
    {"symbol": "SEDG", "entry_price": 150, "current_price": 155, "stop_loss": 145, "take_profit": 160, "direction": "long"},
    {"symbol": "ARKK", "entry_price": 40, "current_price": 42, "stop_loss": 38, "take_profit": 45, "direction": "long"},
    {"symbol": "PERI", "entry_price": 25, "current_price": 26, "stop_loss": 24, "take_profit": 28, "direction": "long"},
    {"symbol": "NU", "entry_price": 8, "current_price": 8.5, "stop_loss": 7.5, "take_profit": 9, "direction": "long"},
    {"symbol": "ACHC", "entry_price": 80, "current_price": 82, "stop_loss": 78, "take_profit": 85, "direction": "long"},
    {"symbol": "SMMT", "entry_price": 2, "current_price": 2.2, "stop_loss": 1.8, "take_profit": 2.5, "direction": "long"},
    {"symbol": "ZIM", "entry_price": 15, "current_price": 16, "stop_loss": 14, "take_profit": 17, "direction": "long"},
    {"symbol": "GRPN", "entry_price": 8, "current_price": 8.5, "stop_loss": 7.5, "take_profit": 9, "direction": "long"},
    {"symbol": "RKT", "entry_price": 10, "current_price": 10.5, "stop_loss": 9.5, "take_profit": 11, "direction": "long"},
    {"symbol": "EBAY", "entry_price": 45, "current_price": 46, "stop_loss": 43, "take_profit": 48, "direction": "long"},
    {"symbol": "CVNA", "entry_price": 35, "current_price": 36, "stop_loss": 33, "take_profit": 38, "direction": "long"},
    {"symbol": "XBI", "entry_price": 80, "current_price": 82, "stop_loss": 78, "take_profit": 85, "direction": "long"},
    {"symbol": "DE", "entry_price": 390, "current_price": 395, "stop_loss": 380, "take_profit": 400, "direction": "long"},
    {"symbol": "CAT", "entry_price": 270, "current_price": 275, "stop_loss": 260, "take_profit": 280, "direction": "long"},
    {"symbol": "BA", "entry_price": 180, "current_price": 185, "stop_loss": 175, "take_profit": 190, "direction": "long"},
    {"symbol": "GE", "entry_price": 100, "current_price": 102, "stop_loss": 97, "take_profit": 105, "direction": "long"},
    {"symbol": "LMT", "entry_price": 450, "current_price": 460, "stop_loss": 440, "take_profit": 470, "direction": "long"},
    {"symbol": "NOC", "entry_price": 450, "current_price": 455, "stop_loss": 440, "take_profit": 470, "direction": "long"},
    {"symbol": "RTX", "entry_price": 90, "current_price": 92, "stop_loss": 88, "take_profit": 95, "direction": "long"},
    {"symbol": "TSM", "entry_price": 110, "current_price": 112, "stop_loss": 107, "take_profit": 115, "direction": "long"},
    {"symbol": "ASML", "entry_price": 900, "current_price": 920, "stop_loss": 880, "take_profit": 950, "direction": "long"},
    {"symbol": "AMAT", "entry_price": 160, "current_price": 165, "stop_loss": 155, "take_profit": 170, "direction": "long"},
    {"symbol": "LRCX", "entry_price": 750, "current_price": 770, "stop_loss": 720, "take_profit": 800, "direction": "long"},
    {"symbol": "KLAC", "entry_price": 650, "current_price": 670, "stop_loss": 630, "take_profit": 690, "direction": "long"},
    {"symbol": "MU", "entry_price": 100, "current_price": 102, "stop_loss": 97, "take_profit": 105, "direction": "long"},
    {"symbol": "NXPI", "entry_price": 200, "current_price": 205, "stop_loss": 190, "take_profit": 210, "direction": "long"},
    {"symbol": "ON", "entry_price": 75, "current_price": 78, "stop_loss": 72, "take_profit": 80, "direction": "long"},
    {"symbol": "QCOM", "entry_price": 140, "current_price": 145, "stop_loss": 135, "take_profit": 150, "direction": "long"},
    {"symbol": "AVGO", "entry_price": 850, "current_price": 860, "stop_loss": 830, "take_profit": 880, "direction": "long"},
    {"symbol": "META", "entry_price": 330, "current_price": 340, "stop_loss": 320, "take_profit": 350, "direction": "long"},
    {"symbol": "NFLX", "entry_price": 500, "current_price": 510, "stop_loss": 480, "take_profit": 530, "direction": "long"},
    {"symbol": "GOOG", "entry_price": 140, "current_price": 145, "stop_loss": 135, "take_profit": 150, "direction": "long"},
    {"symbol": "AAPL", "entry_price": 175, "current_price": 178, "stop_loss": 170, "take_profit": 185, "direction": "long"},
    {"symbol": "MSFT", "entry_price": 300, "current_price": 310, "stop_loss": 290, "take_profit": 320, "direction": "long"},
    {"symbol": "AMZN", "entry_price": 3200, "current_price": 3250, "stop_loss": 3150, "take_profit": 3350, "direction": "long"},
    {"symbol": "PANW", "entry_price": 300, "current_price": 310, "stop_loss": 290, "take_profit": 320, "direction": "long"},
    {"symbol": "NFLX", "entry_price": 500, "current_price": 510, "stop_loss": 480, "take_profit": 530, "direction": "long"},
    {"symbol": "LNG", "entry_price": 150, "current_price": 155, "stop_loss": 145, "take_profit": 160, "direction": "long"},
    {"symbol": "ET", "entry_price": 12, "current_price": 12.5, "stop_loss": 11.5, "take_profit": 13.5, "direction": "long"},
    {"symbol": "OXY", "entry_price": 60, "current_price": 62, "stop_loss": 58, "take_profit": 65, "direction": "long"},
    {"symbol": "PXD", "entry_price": 230, "current_price": 235, "stop_loss": 225, "take_profit": 245, "direction": "long"},
    {"symbol": "MPC", "entry_price": 140, "current_price": 145, "stop_loss": 135, "take_profit": 150, "direction": "long"},
    {"symbol": "VLO", "entry_price": 130, "current_price": 135, "stop_loss": 125, "take_profit": 140, "direction": "long"},
    {"symbol": "PSX", "entry_price": 110, "current_price": 115, "stop_loss": 105, "take_profit": 120, "direction": "long"},
    {"symbol": "FANG", "entry_price": 155, "current_price": 160, "stop_loss": 150, "take_profit": 165, "direction": "long"},
    {"symbol": "CTRA", "entry_price": 27, "current_price": 28, "stop_loss": 26, "take_profit": 30, "direction": "long"},
    {"symbol": "DVN", "entry_price": 45, "current_price": 46, "stop_loss": 43, "take_profit": 48, "direction": "long"},
    {"symbol": "PBR", "entry_price": 15, "current_price": 15.5, "stop_loss": 14.5, "take_profit": 16.5, "direction": "long"},
    {"symbol": "COST", "entry_price": 600, "current_price": 610, "stop_loss": 580, "take_profit": 630, "direction": "long"},
    {"symbol": "WMT", "entry_price": 150, "current_price": 153, "stop_loss": 145, "take_profit": 158, "direction": "long"},
    {"symbol": "TGT", "entry_price": 135, "current_price": 138, "stop_loss": 130, "take_profit": 143, "direction": "long"},
    {"symbol": "LOW", "entry_price": 210, "current_price": 215, "stop_loss": 205, "take_profit": 220, "direction": "long"},
    {"symbol": "HD", "entry_price": 300, "current_price": 305, "stop_loss": 290, "take_profit": 320, "direction": "long"},
    {"symbol": "KR", "entry_price": 45, "current_price": 46, "stop_loss": 43, "take_profit": 48, "direction": "long"},
    {"symbol": "SBUX", "entry_price": 100, "current_price": 102, "stop_loss": 97, "take_profit": 105, "direction": "long"},
    {"symbol": "MCD", "entry_price": 280, "current_price": 285, "stop_loss": 270, "take_profit": 295, "direction": "long"},
    {"symbol": "CMG", "entry_price": 1900, "current_price": 1920, "stop_loss": 1850, "take_profit": 1950, "direction": "long"},
    {"symbol": "WING", "entry_price": 160, "current_price": 165, "stop_loss": 155, "take_profit": 170, "direction": "long"},
    {"symbol": "DPZ", "entry_price": 450, "current_price": 460, "stop_loss": 440, "take_profit": 470, "direction": "long"},
    {"symbol": "SHAK", "entry_price": 65, "current_price": 68, "stop_loss": 62, "take_profit": 72, "direction": "long"},
    {"symbol": "DRI", "entry_price": 145, "current_price": 148, "stop_loss": 140, "take_profit": 155, "direction": "long"},
    {"symbol": "NKE", "entry_price": 95, "current_price": 98, "stop_loss": 90, "take_profit": 105, "direction": "long"},
    {"symbol": "LULU", "entry_price": 350, "current_price": 360, "stop_loss": 340, "take_profit": 370, "direction": "long"},
]
# פונקציה לזיהוי שינוי מגמה או בעיה בעסקה
def check_trade_direction(trade):
    entry = trade['entry_price']
    current = trade['current_price']
    direction = trade['direction']

    if direction == "long" and current < entry * 0.98:
        return "consider_short"
    elif direction == "short" and current > entry * 1.02:
        return "consider_long"
    else:
        return "ok"

# פונקציה לניהול עסקאות
def manage_trades():
    for trade in open_trades:
        status = check_trade_direction(trade)
        symbol = trade['symbol']
        entry = trade['entry_price']
        current = trade['current_price']
        stop = trade['stop_loss']
        take = trade['take_profit']
        direction = trade['direction']

        if status == "ok":
            # הכל בסדר
            message = (
                f"איתות עסקה:\n"
                f"מניה: {symbol}\n"
                f"כיוון מתוכנן: {direction.upper()}\n"
                f"מחיר כניסה: {entry}$\n"
                f"סטופ לוס: {stop}$\n"
                f"טייק פרופיט: {take}$\n"
                f"מצב שוק: תואם לניתוח.\n"
            )
            send_discord_message(public_webhook, message)
            log_trade_update(symbol, entry, current, stop, take, status)
        elif status == "consider_short":
            # המלצה להפוך ללונג -> שורט
            message = (
                f"התראת שינוי מגמה!\n"
                f"מניה: {symbol}\n"
                f"כיוון מתוכנן: LONG\n"
                f"סטטוס: ירידה חזקה זוהתה.\n"
                f"המלצה: לסגור עסקת לונג ולשקול פתיחת SHORT.\n"
                f"מחיר נוכחי: {current}$"
            )
            send_discord_message(public_webhook, message)
            log_trade_update(symbol, entry, current, stop, take, status)
        elif status == "consider_long":
            # המלצה להפוך לשורט -> לונג
            message = (
                f"התראת שינוי מגמה!\n"
                f"מניה: {symbol}\n"
                f"כיוון מתוכנן: SHORT\n"
                f"סטטוס: עלייה חזקה זוהתה.\n"
                f"המלצה: לסגור עסקת שורט ולשקול פתיחת LONG.\n"
                f"מחיר נוכחי: {current}$"
            )
            send_discord_message(public_webhook, message)
            log_trade_update(symbol, entry, current, stop, take, status)
            # הפעלת הבוט
import schedule
import time

if __name__ == "__main__":
    try:
        print("הבוט התחיל לפעול...")
       send_discord_message(private_webhook, "הבוט התחיל לפעול ✅")

        # להריץ ניהול עסקאות כל 5 דקות
        schedule.every(5).minutes.do(manage_trades)

        while True:
            schedule.run_pending()
            time.sleep(1)

    except Exception as e:
        print(f"שגיאה: {e}")
        send_discord_message(error_webhook, f"שגיאת בוט: {e}")

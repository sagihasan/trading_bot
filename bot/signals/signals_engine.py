import os
import random
import requests
import yfinance as yf

# טוען משתני סביבה
public_webhook = os.getenv("DISCORD_PUBLIC_WEBHOOK")

# רשימת המניות לבדיקה
symbols = [
    "PLTR", "AMZN", "NVDA", "AAPL", "TSLA", "ANET", "SNEX", "CRGY", "MSFT", "GOOG",
    "AMD", "ADBE", "META", "AI", "AR", "ALSN", "ASGN", "HIMS", "ASTS", "HOOD",
    "DKNG", "SOUN", "APP", "PZZA", "AVGO", "SMCI", "ADI", "SEDG", "ARKK", "PERI",
    "NU", "ACHC", "SMMT", "ZIM", "GRPN", "RKT", "EBAY", "CVNA", "XBI", "PANW",
    "NFLX", "ET", "LNG", "OXY", "PXD", "VLO", "PSX", "FANG", "CTRA", "PBR", "COST",
    "WMT", "TGT", "LOW", "HD", "KR", "SBUX", "MCD", "CMG", "WING", "DPZ", "DRI",
    "NKE", "LULU", "XOM", "CVX", "COP", "MRO", "APA", "HAL", "SLB", "BKR", "PSX",
    "PAA", "OKE", "WMB", "ENB", "KMI", "EOG", "PBF", "MPC", "HES", "FSLR", "SEDG",
    "RUN", "SPWR", "JKS", "DQ", "MAXN", "NEE", "DUK", "SO", "D", "AEP", "EXC",
    "ED", "PEG", "FE", "EIX", "AES", "TATT", "ALL", "ALKS"
]

# פונקציה לניתוח מניה
def analyze_stock(symbol):
    try:
        stock = yf.Ticker(symbol)
        hist = stock.history(period="6mo")

        last_volume = hist['Volume'].iloc[-1]
        last_close = hist['Close'].iloc[-1]

        if last_volume < 500_000:
            return None

        # סימולציה של ניקוד: נבחר רנדומלית רק לצורך בדיקה
        score = random.randint(1, 100)

        if score > 70:
            direction = random.choice(["לונג", "שורט"])
            return {
                "symbol": symbol,
                "price": round(last_close, 2),
                "direction": direction
            }
        else:
            return None

    except Exception as e:
        print(f"שגיאה בניתוח {symbol}: {e}")
        return None

# שליחת האיתות לדיסקורד
def send_signal_to_discord(signal):
    message = (
        f"איתות יומי\n\n"
        f"שם מניה: {signal['symbol']}\n"
        f"סוג עסקה: {signal['direction']}\n"
        f"מחיר כניסה: {signal['price']}\n"
        f"סטופ לוס: {(signal['price'] * 0.97):.2f}\n"
        f"טייק פרופיט: {(signal['price'] * 1.05):.2f}\n"
        f"\nבהצלחה!"
    )
    data = {"content": message}
    try:
        response = requests.post(public_webhook, json=data)
        if response.status_code == 204:
            print("איתות נשלח בהצלחה לדיסקורד.")
        else:
            print(f"שגיאה בשליחת איתות: {response.status_code}")
    except Exception as e:
        print(f"שגיאה בשליחת איתות: {e}")

# הרצת מנוע האיתותים
def run_signals_engine():
    print("מתחיל סריקת מניות...")
    for symbol in symbols:
        result = analyze_stock(symbol)
        if result:
            send_signal_to_discord(result)
            break
    else:
        print("לא נמצא איתות מתאים היום.")

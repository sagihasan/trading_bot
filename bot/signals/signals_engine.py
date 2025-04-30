import os
import random
import requests
import yfinance as yf
from signals.signal_selector import get_best_signal

# טוען משתני סביבה
public_webhook = os.getenv("DISCORD_PUBLIC_WEBHOOK")

# רשימת המניות לבדיקה
symbols = [
    "AAPL", "ACHC", "ADI", "ADBE", "AI", "ALKS", "ALRM", "ALL", "AMAT", "AMD", "AMZN",
    "ANET", "APP", "APPF", "AR", "ARKK", "ASAN", "ASGN", "ASTS", "AVGO", "AVLR", "CAT",
    "CMG", "COIN", "COST", "CRGY", "CRWD", "CVNA", "DDOG", "DKNG", "DQ", "DRI", "DUK",
    "EBAY", "ED", "ET", "EIX", "EXC", "FANG", "FROG", "FSLR", "FUBO", "GOOG", "GRPN",
    "GTLB", "HD", "HIMS", "HES", "HOOD", "HUBS", "JKS", "KLAC", "KR", "LOW", "LRCX",
    "LNG", "LULU", "MAXN", "MCD", "MNDY", "MPC", "META", "MSTR", "MU", "NFLX", "NEE",
    "NET", "NKE", "NOW", "NU", "NXPI", "NVDA", "OKTA", "ON", "OXY", "PANW", "PATH",
    "PBF", "PD", "PEG", "PERI", "PZZA", "PLTR", "PSX", "PXD", "RKT", "RNG", "RUN",
    "SAIL", "SEDG", "SMCI", "SMMT", "SNEX", "SO", "SOUN", "SPWR", "SPLK", "SQ", "SBUX",
    "TEAM", "TATT", "TGT", "TENB", "TSLA", "TXN", "UPST", "VLO", "VRNS", "WK", "WING",
    "WMT", "XBI", "XBT", "ZI", "ZIM"
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
    best_signal = get_best_signal(symbols)

if best_signal:
    signal_message = format_trade_signal(
        symbol=best_signal["symbol"],
        price=best_signal["price"],
        stop_loss=round(best_signal["price"] * 0.97, 2),  # לדוגמה 3% סטופ לוס
        take_profit=round(best_signal["price"] * 1.05, 2),  # לדוגמה 5% טייק פרופיט
        score=best_signal["score"],
        recommendation=best_signal["recommendation"]
    )
    send_discord_message(public_webhook, signal_message)
else:
    send_discord_message(public_webhook, "לא נמצאה מניה מתאימה היום.")
        

import requests

# פונקציה לשליחת הודעה לדיסקורד
def send_discord_message(webhook_url, message):
    data = {"content": message}
    try:
        response = requests.post(webhook_url, json=data)
        if response.status_code != 204:
            print(f"שגיאה בשליחת הודעה לדיסקורד: {response.status_code}")
    except Exception as e:
        print(f"שגיאה בשליחת הודעה לדיסקורד: {e}")

# פונקציה לניהול עסקה
def manage_trade(trade_data, webhook_url):
    """
    trade_data: {
        "symbol": "AAPL",
        "entry_price": 150,
        "current_price": 155,
        "stop_loss": 145,
        "take_profit": 165,
        "direction": "long"  # או "short"
    }
    """

    entry_price = trade_data["entry_price"]
    current_price = trade_data["current_price"]
    stop_loss = trade_data["stop_loss"]
    take_profit = trade_data["take_profit"]
    direction = trade_data["direction"]
    symbol = trade_data["symbol"]

    # אחוזי שינוי מהכניסה
    change_percent = ((current_price - entry_price) / entry_price) * 100 if direction == "long" else ((entry_price - current_price) / entry_price) * 100

    # זיהוי חוזקה
    if change_percent >= 5:
        new_stop_loss = entry_price  # להזיז סטופ לוס לכניסה
        message = f"""חוזקה מזוהה בעסקה על {symbol}:
        מחיר כניסה: {entry_price}
        מחיר נוכחי: {current_price}
        סטופ לוס קודם: {stop_loss}
        סטופ לוס חדש: {new_stop_loss}
        טייק פרופיט: {take_profit}
        עדכון: העברת סטופ לוס למחיר כניסה!
        """
        send_discord_message(webhook_url, message)

    # זיהוי חולשה
    if change_percent <= -3:
        message = f"""חולשה מזוהה בעסקה על {symbol}:
        מחיר כניסה: {entry_price}
        מחיר נוכחי: {current_price}
        סטופ לוס: {stop_loss}
        טייק פרופיט: {take_profit}
        המלצה: לשקול סגירה חלקית או מלאה.
        """
        send_discord_message(webhook_url, message)

    # אם העסקה ברווח חזק - לשדרג טייק פרופיט
    if change_percent >= 8:
        new_take_profit = take_profit * 1.05  # מעלים טייק פרופיט ב-5%
        message = f"""עדכון טייק פרופיט בעסקה על {symbol}:
        מחיר כניסה: {entry_price}
        מחיר נוכחי: {current_price}
        טייק פרופיט קודם: {take_profit}
        טייק פרופיט חדש: {round(new_take_profit, 2)}
        סטופ לוס: {stop_loss}
        """
        send_discord_message(webhook_url, message)

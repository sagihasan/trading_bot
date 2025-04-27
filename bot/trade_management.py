import pandas as pd
import os
from datetime import datetime

# יצירת קובץ Excel אם לא קיים
if not os.path.exists('trade_management_log.xlsx'):
    df = pd.DataFrame(columns=["Date", "Symbol", "Old Stop Loss", "New Stop Loss", "Old Take Profit", "New Take Profit", "Action"])
    df.to_excel('trade_management_log.xlsx', index=False)

# פונקציה לשמירה ללוג
def save_trade_management_log(symbol, old_stop, new_stop, old_take, new_take, action):
    log_file = 'trade_management_log.xlsx'

    df = pd.read_excel(log_file)

    new_row = {
        "Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Symbol": symbol,
        "Old Stop Loss": old_stop,
        "New Stop Loss": new_stop,
        "Old Take Profit": old_take,
        "New Take Profit": new_take,
        "Action": action
    }
    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    df.to_excel(log_file, index=False)

# פונקציה לניהול עסקה חכם
def manage_trade_dynamically(trade):
    symbol = trade['symbol']
    entry_price = trade['entry_price']
    current_price = trade['current_price']
    stop_loss = trade['stop_loss']
    take_profit = trade['take_profit']
    direction = trade['direction']

    profit_percentage = ((current_price - entry_price) / entry_price) * 100 if direction == "long" else ((entry_price - current_price) / entry_price) * 100

    actions = []
    new_stop = stop_loss
    new_take = take_profit

    # שדרוג סטופ לוס אם יש רווח
    if profit_percentage >= 3:
        new_stop = entry_price  # להזיז סטופ למחיר כניסה
        actions.append("Moved Stop Loss to Entry Price")

    if profit_percentage >= 5:
        new_stop = entry_price * (1.02 if direction == "long" else 0.98)  # להזיז סטופ לרווח קטן
        actions.append("Updated Stop Loss to small profit")

    if profit_percentage >= 8:
        actions.append("Partial close 50%")

    if profit_percentage >= 10:
        new_take = take_profit * (1.05 if direction == "long" else 0.95)  # לשפר טייק פרופיט
        actions.append("Updated Take Profit to extend")

    if actions:
        message = (
            f"ניהול עסקה חכם:\n"
            f"מניה: {symbol}\n"
            f"פעולות שבוצעו:\n" + "\n".join(f"- {action}" for action in actions) +
            f"\nמחיר נוכחי: {current_price:.2f}$\n"
            f"סטופ לוס חדש: {new_stop:.2f}$\n"
            f"טייק פרופיט חדש: {new_take:.2f}$"
        )
        send_discord_message(public_webhook, message)

        # שמירת שינוי ל-Excel
        save_trade_management_log(symbol, stop_loss, new_stop, take_profit, new_take, "; ".join(actions))

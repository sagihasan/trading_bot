import pandas as pd
from datetime import datetime

# פונקציה לשמירה של עדכון ניהול העסקה ל־Excel
def save_trade_management_log(symbol, old_stop, new_stop, old_take, new_take, action):
    log_file = 'trade_management_log.xlsx'

    # בדיקה אם הקובץ קיים, אם לא - יצירה עם כותרות
    if not os.path.exists(log_file):
        df = pd.DataFrame(columns=[
            "Date",
            "Symbol",
            "Old Stop Loss",
            "New Stop Loss",
            "Old Take Profit",
            "New Take Profit",
            "Action"
        ])
        df.to_excel(log_file, index=False)
    else:
        df = pd.read_excel(log_file)

    # הוספת שורה חדשה
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

    # שמירה חזרה לקובץ
    df.to_excel(log_file, index=False)

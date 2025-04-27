import pandas as pd
import datetime

def generate_trade_report(trades):
    # יצירת טבלה מדאטה
    df = pd.DataFrame(trades)

    # הוספת עמודת תאריך הפקה
    df['report_date'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # שמירת הקובץ
    df.to_excel('trade_management_log.xlsx', index=False)

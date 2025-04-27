import openpyxl
from openpyxl import Workbook
import os

def log_trade_update(symbol, entry_price, current_price, old_stop, new_stop, old_take, new_take, status):
    file_path = "trade_management_log.xlsx"

    # אם הקובץ לא קיים - ליצור אותו
    if not os.path.exists(file_path):
        wb = Workbook()
        ws = wb.active
        ws.append(["מניה", "מחיר כניסה", "מחיר נוכחי", "סטופ קודם", "סטופ חדש", "טייק קודם", "טייק חדש", "תוצאה צפויה"])
        wb.save(file_path)

    # לפתוח קובץ קיים ולעדכן
    wb = openpyxl.load_workbook(file_path)
    ws = wb.active

    # להוסיף שורה חדשה
    ws.append([symbol, entry_price, current_price, old_stop, new_stop, old_take, new_take, status])

    # לשמור
    wb.save(file_path)

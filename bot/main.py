from keep_alive.keep_alive import keep_alive
from utils.helpers import example_helper
from macro.macro_analyzer import analyze_macro
from reports.weekly_report_generator import generate_report

def run_bot():
    print("הבוט מתחיל לפעול...")
    helper_result = example_helper()
    print("Helper:", helper_result)

    macro_data = analyze_macro()
    print("מאקרו:", macro_data)

    generate_report()
    print("נשלח דוח שבועי")

if __name__ == "__main__":
    keep_alive()
    run_bot()

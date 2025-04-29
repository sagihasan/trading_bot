import os

# === ניהול התראות חכמות בעזרת קבצי נעילה (.lock) ===

def get_lock_file(alert_type):
    return f"{alert_type}.lock"

def mark_alert_sent(alert_type):
    with open(get_lock_file(alert_type), "w") as f:
        f.write("sent")

def can_send_alert(alert_type):
    return not os.path.exists(get_lock_file(alert_type))

def reset_alert_flags():
    for alert_type in ["error_sent", "signal_sent", "management_sent", "report_sent"]:
        try:
            os.remove(get_lock_file(alert_type))
        except FileNotFoundError:
            pass

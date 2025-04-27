# ניהול התראות חכמות

alert_flags = {
    "error_sent": False,
    "signal_sent": False,
    "management_sent": False,
    "report_sent": False
}

def reset_alert_flags():
    for key in alert_flags:
        alert_flags[key] = False

def mark_alert_sent(alert_type):
    if alert_type in alert_flags:
        alert_flags[alert_type] = True

def can_send_alert(alert_type):
    if alert_type == "error_sent":
        return not alert_flags["error_sent"]
    if alert_type == "signal_sent":
        return not alert_flags["error_sent"] and not alert_flags["signal_sent"]
    if alert_type == "management_sent":
        return not alert_flags["error_sent"] and not alert_flags["signal_sent"] and not alert_flags["management_sent"]
    if alert_type == "report_sent":
        return True
    return False

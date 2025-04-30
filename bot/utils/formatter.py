def format_trade_signal(
    symbol,
    direction,
    entry_price,
    stop_loss,
    take_profit,
    market_condition,
    trend_line,
    support_resistance,
    fundamental_status,
    bot_recommendation,
    total_score,
    strategic_zone
):
    return (
        f"איתות עסקה חדש:\n"
        f"מניה: {symbol}\n"
        f"כיוון: {direction.upper()}\n"
        f"כניסה: {entry_price}$\n"
        f"סטופ לוס: {stop_loss}$\n"
        f"טייק פרופיט: {take_profit}$\n"
        f"מצב שוק: {market_condition}\n"
        f"קו מגמה: {trend_line}\n"
        f"תמיכה/התנגדות: {support_resistance}\n"
        f"ניתוח פונדומנטלי: {fundamental_status}\n"
        f"המלצת הבוט: {bot_recommendation}\n"
        f"ניקוד כולל: {total_score}/10\n"
        f"אזור אסטרטגי: {strategic_zone}"
    )

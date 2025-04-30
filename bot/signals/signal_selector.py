import yfinance as yf
import random
from datetime import datetime
from signals.news_sentiment import get_sentiment_score

def score_stock(symbol):
    try:
        stock = yf.Ticker(symbol)
        hist = stock.history(period="6mo")

        if hist.empty or len(hist) < 60:
            return None

        close_price = hist['Close'].iloc[-1]
        ma20 = hist['Close'].rolling(window=20).mean().iloc[-1]
        rsi = compute_rsi(hist['Close'])

        sentiment = get_sentiment_score(symbol)

        score = 0
        if close_price > ma20:
            score += 2
        if rsi > 50:
            score += 2
        if sentiment == "Positive":
            score += 2
        elif sentiment == "Neutral":
            score += 1

        trend_strength = get_trend_strength(hist)
        score += trend_strength  # בין 0 ל־3

        return {
            "symbol": symbol,
            "score": score,
            "price": round(close_price, 2),
            "sentiment": sentiment,
            "recommendation": "הבוט ממליץ להיכנס לעסקה" if score >= 7 else "הבוט ממליץ להמתין"
        }

    except Exception as e:
        print(f"שגיאה בניתוח {symbol}: {e}")
        return None

def compute_rsi(prices, period=14):
    delta = prices.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    rs = gain / loss
    return 100 - (100 / (1 + rs)).iloc[-1]

def get_trend_strength(hist):
    recent = hist['Close'].iloc[-1]
    week_ago = hist['Close'].iloc[-5]
    month_ago = hist['Close'].iloc[-21]
    if recent > week_ago > month_ago:
        return 3
    elif recent > week_ago:
        return 2
    elif recent > month_ago:
        return 1
    else:
        return 0

def get_best_signal(symbols):
    scored = []
    for symbol in symbols:
        result = score_stock(symbol)
        if result:
            scored.append(result)

    if not scored:
        return None

    sorted_scored = sorted(scored, key=lambda x: x['score'], reverse=True)
    return sorted_scored[0]

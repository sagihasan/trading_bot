import requests
import os

NEWS_API_KEY = os.getenv("NEWS_API_KEY")

def get_sentiment_score(symbol):
    url = f"https://newsapi.org/v2/everything?q={symbol}&language=en&sortBy=publishedAt&pageSize=10&apiKey={NEWS_API_KEY}"
    try:
        response = requests.get(url)
        if response.status_code != 200:
            print(f"שגיאה ב-NewsAPI עבור {symbol}: {response.status_code}")
            return 0  # סנטימנט ניטרלי כברירת מחדל

        data = response.json()
        articles = data.get("articles", [])
        if not articles:
            return 0  # אין חדשות – סנטימנט ניטרלי

        positive_words = ["growth", "beats", "strong", "profit", "positive", "record", "surge", "up", "rally", "bullish"]
        negative_words = ["loss", "misses", "decline", "weak", "negative", "drop", "fall", "crash", "down", "bearish"]

        score = 0
        for article in articles:
            content = (article["title"] or "") + " " + (article["description"] or "")
            content_lower = content.lower()
            for word in positive_words:
                if word in content_lower:
                    score += 1
            for word in negative_words:
                if word in content_lower:
                    score -= 1

        return max(min(score, 5), -5)  # מגביל בין -5 ל+5
    except Exception as e:
        print(f"שגיאת סנטימנט ({symbol}): {e}")
        return 0

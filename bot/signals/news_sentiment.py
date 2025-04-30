import os
import requests

def analyze_news_sentiment(symbol):
    api_key = os.getenv("API_NEWS_KEY")
    if not api_key:
        return "לא הוזן API של חדשות"

    url = f"https://newsapi.org/v2/everything?q={symbol}&language=en&sortBy=publishedAt&pageSize=10&apiKey={api_key}"

    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code != 200 or "articles" not in data:
            return "שגיאה בניתוח חדשות"

        headlines = [article["title"] for article in data["articles"] if "title" in article]

        # ניתוח פשוט: אם יש יותר כותרות חיוביות מאשר שליליות
        positive_words = ["growth", "profit", "beat", "strong", "up", "surge"]
        negative_words = ["loss", "drop", "miss", "down", "weak", "cut"]

        pos_count = sum(any(p in h.lower() for p in positive_words) for h in headlines)
        neg_count = sum(any(n in h.lower() for n in negative_words) for h in headlines)

        if pos_count > neg_count:
            return "סנטימנט חיובי"
        elif neg_count > pos_count:
            return "סנטימנט שלילי"
        else:
            return "סנטימנט ניטרלי"

    except Exception as e:
        return f"שגיאה בניתוח סנטימנט: {e}"

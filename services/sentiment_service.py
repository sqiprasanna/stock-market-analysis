import requests
import os
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Get API token from environment variable
API_TOKEN = os.getenv('MARKETAUX_API_TOKEN')

def get_news_sentiment(ticker: str):
    """Fetches real-time news for a ticker via Marketaux API and calculates sentiment."""
    if not API_TOKEN:
        return {"sentiment": "Neutral", "score": 0, "headlines": ["Error: API token not set."]}
        
    url = f'https://api.marketaux.com/v1/news/all?symbols={ticker}&filter_entities=true&language=en&api_token={API_TOKEN}'
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if 'data' not in data or not data['data']:
            return {"sentiment": "Neutral", "score": 0, "headlines": ["No recent news found."]}
        
        analyzer = SentimentIntensityAnalyzer()
        headlines = [article['title'] for article in data['data'][:5]]
        scores = [analyzer.polarity_scores(title)['compound'] for title in headlines]
        avg_sentiment = sum(scores) / len(scores)
        
        return {
            "sentiment": "Positive" if avg_sentiment > 0.05 else "Negative" if avg_sentiment < -0.05 else "Neutral",
            "score": avg_sentiment,
            "headlines": headlines
        }
    except Exception as e:
        return {"sentiment": "Neutral", "score": 0, "headlines": [f"Error fetching news: {str(e)}"]}

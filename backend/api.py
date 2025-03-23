from fastapi import APIRouter, HTTPException
from backend.news_scraper import fetch_bing_news
from backend.summarizer import summarize
from backend.sentiment import analyze_sentiment
from backend.text_to_speech import text_to_speech
from collections import Counter
import re
router = APIRouter()
def extract_keywords(text, top_n=3):
    words = re.findall(r'\b\w+\b', text.lower())
    common_words = {'the', 'and', 'for', 'this', 'that', 'with', 'from', 'they', 'will', 'have'}
    keywords = [w for w in words if w not in common_words and len(w) > 3]
    freq = Counter(keywords)
    return [word for word, _ in freq.most_common(top_n)]
@router.post("/analyze")
def analyze_news(company: str):
    articles = fetch_bing_news(query=company)
    if isinstance(articles, dict) and "error" in articles:
        raise HTTPException(status_code=500, detail=articles["error"])
    results = []
    sentiment_counts = {"Positive": 0, "Negative": 0, "Neutral": 0}
    all_topics = []
    for article in articles[:5]:
        summary = summarize(article["title"])
        sentiment = analyze_sentiment(summary)
        sentiment_counts[sentiment] += 1
        topics = extract_keywords(summary)
        all_topics.extend(topics)
        results.append({
            "title": article["title"],
            "link": article["link"],
            "summary": summary,
            "sentiment": sentiment,
            "topics": topics
        })
    final_summary = f"{company} has {sentiment_counts['Positive']} positive, {sentiment_counts['Negative']} negative, and {sentiment_counts['Neutral']} neutral articles."
    audio_url = text_to_speech(final_summary)
    insights = (
        f"Most articles focus on topics like {', '.join(set(all_topics[:5]))}. "
        f"The sentiment is mostly {max(sentiment_counts, key=sentiment_counts.get).lower()}."
    )
    return {
        "company": company,
        "articles": results,
        "summary": final_summary,
        "sentiment_distribution": sentiment_counts,
        "insights": insights,
        "audio": audio_url
    }

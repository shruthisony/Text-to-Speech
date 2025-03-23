from transformers import pipeline
sentiment_analyzer = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")
def analyze_sentiment(text):
    try:
        result = sentiment_analyzer(text)[0]
        label = result['label']  
        if '1' in label or '2' in label:
            return "Negative"
        elif '3' in label:
            return "Neutral"
        elif '4' in label or '5' in label:
            return "Positive"
        else:
            return "Neutral"
    except Exception as e:
        return f"Error in sentiment analysis: {str(e)}"
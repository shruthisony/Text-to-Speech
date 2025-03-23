# News Summarization and Text-to-Speech Application (Akaike Internship Assignment)
This web application summarizes news about a given company, analyzes the sentiment of each article, extracts key topics, and converts the final summary into Hindi audio using a TTS engine. It is built as part of the Akaike internship assignment.

## Features
•⁠  ⁠Fetches latest news (up to 10) using Bing News
•⁠  ⁠Summarizes articles using BART (facebook/bart-large-cnn)
•⁠  ⁠Performs Sentiment Analysis (Positive/Negative/Neutral) using multilingual BERT
•⁠  ⁠Extracts Topics from each summary
•⁠  ⁠Computes Sentiment Distribution
•⁠  ⁠Provides Insights on article tone and topic focus
•⁠  ⁠Converts final summary into Hindi audio using gTTS
•⁠  ⁠Clean and interactive Gradio interface

## Tech Stack
Layer           | Tools Used
----------------|-------------------------------
Web UI          | Gradio
Backend         | FastAPI
Summarization   | BART (facebook/bart-large-cnn)
Sentiment       | BERT (nlptown/bert-base-multilingual-uncased-sentiment)
TTS             | gTTS (Google Text-to-Speech)
Scraping        | Selenium + BeautifulSoup
Extras          | Redis (optional), Requests, Transformers


## Project Structure
news_analyzer/
├── app.py                    -> Gradio frontend (used for deployment)
├── main.py                   -> FastAPI backend entrypoint (for local testing)
├── requirements.txt          -> All Python dependencies
├── README.md                 -> Project documentation

├── frontend/
│   └── app.py                -> Gradio app file (optional if separate)

├── backend/
│   ├── api.py                -> FastAPI route for summarization, sentiment, TTS
│   ├── news_scraper.py       -> Scrapes latest Bing news
│   ├── summarizer.py         -> Summarizes text using BART
│   ├── sentiment.py          -> Analyzes sentiment using BERT
│   ├── text_to_speech.py     -> Converts summary to Hindi audio
│   ├── redis_cache.py        -> Optional: Redis-based caching

├── output.mp3                -> Example output Hindi audio



## How to Run the Project Locally
1.⁠ ⁠Clone the repository:
   git clone <your-repo-url>
   cd news_analyzer
2.⁠ ⁠(Optional) Create and activate virtual environment:
   python -m venv venv
   source venv/bin/activate   (on Windows: venv\Scripts\activate)
3.⁠ ⁠Install dependencies:
   pip install -r requirements.txt
4.⁠ ⁠Start FastAPI backend:
   uvicorn main:app --reload
5.⁠ ⁠In another terminal, run Gradio frontend:
   python app.py


## Example API Output

{
  "company": "Tesla",
  "articles": [
    {
      "title": "...",
      "summary": "...",
      "sentiment": "Positive",
      "topics": ["tesla", "launch", "india"]
    }
  ],
  "summary": "Tesla has 4 positive, 1 negative, and 0 neutral articles.",
  "sentiment_distribution": {
    "Positive": 4,
    "Negative": 1,
    "Neutral": 0
  },
  "insights": "Most articles focus on topics like tesla, launch, india. The sentiment is mostly positive.",
  "audio": "output.mp3"
}


## Deployment (Hugging Face Spaces)

1.⁠ ⁠Create a new Space at: https://huggingface.co/spaces
2.⁠ ⁠Choose 'Gradio' as the SDK
3.⁠ ⁠Upload the following files:
   - app.py
   - requirements.txt
   - README.md
4.⁠ ⁠The application will deploy and be available publicly


## Author
Shruthi G B

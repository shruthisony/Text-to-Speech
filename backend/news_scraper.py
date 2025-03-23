from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
def fetch_bing_news(query="Tesla", max_articles=10):
    search_url = f"https://www.bing.com/news/search?q={query}"
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("user-agent=Mozilla/5.0")
    driver = webdriver.Chrome(options=options)
    driver.get(search_url)
    time.sleep(2)
    html = driver.page_source
    driver.quit()
    soup = BeautifulSoup(html, "html.parser")
    articles = []
    for item in soup.select(".news-card, .news-card.newsitem")[:max_articles]:
        title_tag = item.select_one("a.title")
        link = title_tag["href"] if title_tag else None
        title = title_tag.text.strip() if title_tag else None
        if title and link:
            articles.append({
                "title": title,
                "link": link
            })
    return articles if articles else {"error": "No Bing news articles found."}
if __name__ == "__main__":
    result = fetch_bing_news("Tesla")
    if isinstance(result, dict) and "error" in result:
        print("Error:", result["error"])
    else:
        print(f"Found {len(result)} articles:\n")
        for article in result:
            print(article)
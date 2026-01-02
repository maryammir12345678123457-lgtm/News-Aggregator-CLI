import requests
import json
import sqlite3
import pandas as pd
from datetime import datetime

API_KEY = "b5658b237bb047c0940839c6d37dde53"
BASE_URL = "https://newsapi.org/v2/top-headlines"

def fetch_news(keyword=None, source=None, date=None):
    params = {
        "apiKey": API_KEY,
        "language": "en"
    }

    if keyword:
        params["q"] = keyword
    if source:
        params["sources"] = source
    if date:
        params["from"] = date

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    articles = []
    for article in data.get("articles", []):
        articles.append({
            "title": article["title"],
            "source": article["source"]["name"],
            "published": article["publishedAt"][:10],
            "url": article["url"]
        })

    return articles

def remove_duplicates(news):
    unique = {}
    for item in news:
        unique[item["title"]] = item
    return list(unique.values())

def save_json(news):
    with open("news.json", "w", encoding="utf-8") as f:
        json.dump(news, f, indent=4)
    print("✔ Saved to news.json")

def save_sqlite(news):
    conn = sqlite3.connect("news.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS news (
            title TEXT UNIQUE,
            source TEXT,
            published TEXT,
            url TEXT
        )
    """)

    for item in news:
        cursor.execute("""
            INSERT OR IGNORE INTO news VALUES (?,?,?,?)
        """, (item["title"], item["source"], item["published"], item["url"]))

    conn.commit()
    conn.close()
    print("✔ Saved to SQLite database")

def export_files(news):
    df = pd.DataFrame(news)
    df.to_csv("news.csv", index=False)
    df.to_excel("news.xlsx", index=False)
    print("✔ Exported to CSV & Excel")

def main():
    print("\n📰 NEWS AGGREGATOR CLI\n")

    keyword = input("Enter keyword (or press Enter to skip): ")
    source = input("Enter source (bbc-news, cnn) or Enter: ")
    date = input("Enter date (YYYY-MM-DD) or Enter: ")

    news = fetch_news(keyword, source, date)
    news = remove_duplicates(news)

    if not news:
        print("❌ No news found")
        return

    for i, item in enumerate(news, 1):
        print(f"\n{i}. {item['title']}")
        print(f"   Source: {item['source']}")
        print(f"   Date: {item['published']}")

    save_json(news)
    save_sqlite(news)
    export_files(news)

    print("\n✅ Done!")


if __name__ == "__main__":
    main()

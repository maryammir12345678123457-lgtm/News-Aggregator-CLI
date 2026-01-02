A Python-based Command Line News Aggregator that collects headlines from multiple sources using NewsAPI, allows filtering through the CLI, removes duplicate news articles, stores data locally, and exports results to CSV and Excel.
This project is designed for beginners and serves as a capstone-style project combining API usage, data processing, and file automation.
Project Overview

The News Aggregator CLI fetches real-time news headlines and lets users:
Filter news by keyword, source, or date
Store fetched data in JSON and SQLite
Export results to CSV and Excel
Avoid duplicate news entries automatically
The application runs entirely in the command line, making it lightweight and easy to use.

Features

Fetch news from multiple sources using NewsAPI

Command Line Interface (CLI)

Filter by:
Keyword
News source
Date

Basic deduplication (removes duplicate headlines)

Store data in:
JSON file
SQLite database

Export data to:
CSV
Excel (.xlsx)

Technologies Used
Python
NewsAPI
requests
pandas
sqlite3
json

csv

openpyxl

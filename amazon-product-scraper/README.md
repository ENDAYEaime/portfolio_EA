# Amazon to Pinterest Scraper 🛍️📌

Automated web scraping pipeline built with **Python + Selenium**  
Designed to extract Amazon product data and prepare it for content automation platforms such as Pinterest.

---

## 🚀 Project Overview

This project automates the extraction of Amazon product information from affiliate links and generates a clean CSV file ready for:

- Pinterest automation
- Affiliate marketing workflows
- Content generation
- Social media publishing pipelines
- Integration with tools like n8n, Zapier, or Make

The scraper handles dynamic page loading, avoids duplicates, and structures the data in a clean, reusable format.

---

## 🧠 What This Project Demonstrates

- Web automation using Selenium
- Dynamic content scraping (JavaScript-rendered pages)
- Data cleaning and formatting
- Duplicate detection logic
- CSV export pipeline
- Automation-ready dataset generation
- Error handling & resilience
- Headless browser configuration

---

## 📦 Extracted Data Fields

Each scraped product contains:

| Column | Description |
|--------|------------|
| Lien d'affiliation | Affiliate short link (amzn.to) |
| Titre de l'article | Product title |
| Couleur | Extracted product color (multi-strategy detection) |
| Image URL | Main product image URL |

---

## 🏗️ Tech Stack

- Python 3.10+
- Selenium
- WebDriver Manager
- Pandas (for analysis)
- CSV module
- Chrome Headless

---

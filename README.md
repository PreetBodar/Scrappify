# Flipkart Review Sentiment Analyzer

A web app that scrapes Flipkart product reviews, analyzes sentiment with VADER, and visualizes results in a pie chart.

## 🚀 Features

- Review Scraping: Extracts user reviews from Flipkart product pages
- Sentiment Analysis: Classifies reviews as Positive 😊, Negative 😠, or Neutral 😐 using VADER
- Data Visualization: Shows sentiment distribution in a pie chart
- Web Interface: Flask-based UI for entering product URLs and viewing results

## 🛠️ Tech Stack

- Backend: Python, Flask
- Web Scraping: BeautifulSoup, Requests
- NLP: NLTK (VADER)
- Visualization: Matplotlib / Chart.js
- Frontend: HTML, CSS, JavaScript

## ⚙️ How It Works

1. User enters a Flipkart product URL
2. App scrapes reviews from the page
3. VADER analyzes each review's sentiment score
4. Reviews categorize into Positive, Negative, or Neutral
5. Results display as a pie chart

## 📂 Project Structure
├── main.py # Main Flask application
├── templates/ # HTML templates
└── static/ # CSS, JS, charts

## ⚠️ Limitations

- Flipkart may block scraping (add headers/rate limiting)
- Only public product pages
- VADER is rule-based; accuracy varies
- No requirements.txt yet—install dependencies manually

## 📈 Future Enhancements

- Bar charts and trend analysis
- Advanced NLP (BERT/Transformers)
- Multi-language support
- Export to CSV/PDF
- Real-time scraping with pagination

## 📜 Disclaimer

For educational purposes only. Comply with Flipkart's terms of service for scraping.

## 👨‍💻 Author

**Preet Bodar**  
GitHub: [PreetBodar](https://github.com/PreetBodar)

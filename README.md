🛒 Flipkart Review Sentiment Analyzer
A web application that scrapes product reviews from Flipkart and performs sentiment analysis using VADER to classify reviews as Positive, Negative, or Neutral, with results visualized in a pie chart.
---

🚀 Features
🔍 Review Scraping  
Extracts user reviews from Flipkart product pages.
💬 Sentiment Analysis  
Uses VADER (Valence Aware Dictionary and sEntiment Reasoner) to classify reviews:
Positive 😊
Negative 😠
Neutral 😐
📊 Data Visualization  
Displays sentiment distribution using a pie chart.
🌐 Web Interface  
Simple UI built with Flask for inputting product URLs and viewing results.
---

🛠️ Tech Stack
Backend: Python, Flask
Web Scraping: BeautifulSoup, Requests
NLP: NLTK (VADER Sentiment Analyzer)
Visualization: Matplotlib / Chart.js
Frontend: HTML, CSS, JavaScript
---

⚙️ How It Works
User inputs a Flipkart product URL
Application scrapes reviews from the product page
Each review is analyzed using VADER sentiment scoring
Reviews are categorized into Positive, Negative, or Neutral
Results are displayed as a pie chart
---

---
📂 Project Structure
├── main.py              # Main Flask application  \
├── templates/          # HTML templates  
├── static/             # CSS, JS, charts  

---
⚠️ Limitations
Flipkart may block scraping requests (use headers / rate limiting if needed)
Works only for publicly accessible product pages
Sentiment accuracy depends on VADER (rule-based model)
---
📈 Future Enhancements
📊 Bar charts and trend analysis
🧠 Advanced NLP models (BERT / Transformers)
🌍 Multi-language sentiment support
📦 Export results (CSV / PDF)
🔄 Real-time scraping with pagination support
---

📜 Disclaimer
This project is for educational purposes only. Web scraping should comply with Flipkart’s terms of service.
The requirements.txt file is not added, will add in near future, So manually install dependencies
---

👨‍💻 Author
Preet Bodar
GitHub: https://github.com/PreetBodar

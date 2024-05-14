from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
def scrape_page(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept-Encoding": "gzip, deflate", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,/;q=0.8",
        "DNT": "1", "Connection": "close", "Upgrade-Insecure-Requests": "1"}

    # Request the HTML page from the web server based on the provided URL
    web_pages = requests.get(url, headers=headers)

    # Convert the HTML page into a BeautifulSoup object
    soup = BeautifulSoup(web_pages.content, "html.parser")

    # Find all the div tags containing reviews
    elements = soup.find_all("div", attrs={"class": "ZmyHeo"})

    # converting the html content in the list to string
    # string_list = [str(element) for element in elements]

    # Extract the text content from each div tag and append to the proto_list
    proto_list = [element.get_text(strip=True) for element in elements]

    # Convert the list of HTML elements to strings
    # string_list = [str(element) for element in elements]

    # Data cleaning: Remove specific words from each string in the list
    words_to_remove = ["READ MORE"]
    cleaned_list = [string for string in proto_list]
    for i, string in enumerate(cleaned_list):
        for word in words_to_remove:
            cleaned_list[i] = cleaned_list[i].replace(word, '')

    return cleaned_list

def Analyze_Sentiment(Review_list):

    obj=SentimentIntensityAnalyzer()
    # Genertaes sentiment list of reviews
    sen_list=[]
    for i in Review_list:
        sen_dict=obj.polarity_scores(i)
        sen_list.append(sen_dict)
    print(sen_list)
    #Helps with graph generation
    rp = 0
    rn = 0
    rnu = 0
    for i in sen_list:
        if i.get("compound") > 0.1:
            rp = rp + 1
        elif i.get("compound") < -0.1:
            rn = rn + 1
        else:
            rnu = rnu + 1
    return rp,rn,rnu

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')


@app.route("/",methods=['POST'])
def resultpg():
    url = request.form['urlToBeSent']
    print(url)
    review_list = scrape_page(url)
    print(review_list)
    rp,rn,rnu = Analyze_Sentiment(review_list)
    total = rp + rn + rnu
    print(total)
    rp = rp/total *100
    rn = rn/total *100
    rnu = rnu/total *100
    data = { 'pos_num' : rp,
             'neg_num' : rn,
             'neu_num' : rnu
            }
    print(data)

    return render_template('resultpg.html', data = data)


app.run(debug=True)


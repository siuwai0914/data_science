from flask import Flask, render_template
import requests
import json
from bs4 import BeautifulSoup as soup

app = Flask(__name__)

@app.route("/weather")
def index():
    url = "https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=fnd&lang=en"
    weather = json.loads(requests.get(url).content)
    date_list = []
    max_temp_list = []
    min_temp_list = []
    
    for day in weather["weatherForecast"]:
        date_list.append(day["forecastDate"])
        max_temp_list.append(day["forecastMaxtemp"]["value"])
        min_temp_list.append(day["forecastMintemp"]["value"])
    weather_json = {"date_list": date_list, "max_temp_list": max_temp_list, "min_temp_list": min_temp_list}
    return render_template("weather_forecast.html", weather_json=weather_json)


@app.route("/news")
def show_news():
    url = "https://www.scmp.com/rss/40/feed"
    soup_page = soup(requests.get(url).content, "xml")
    news_list = soup_page.find_all("item")

    title_list = []
    link_list = []
    pubDate_list = []
    description_list = []

    for news in news_list:
        title_list.append(news.title.text)
        link_list.append(news.link.text)
        pubDate_list.append(news.pubDate.text)
        description_list.append(news.description.text)

    news_dict = {
        "title": title_list,
        "link": link_list,
        "pubDate": pubDate_list,
        "description": description_list
    }

    return render_template("news.html", news_dict=news_dict)

@app.route("/nike/<string:category>")
def nike_scraping(category):
    url = "https://www.nike.com.hk/man/" + category + "/shoe/list.htm?intpromo=PNTP"
    html_page = soup(requests.get(url).content, "html")
    product_page = html_page.find_all("dl", {"class": "product_list_content"})

    product_name_list = []
    product_price_list = []

    for product in product_page:
        product_name_list.append(product.find("span", {"class": "up"}).text)
        product_price_list.append(product.find("dd", {"class": "color666"}).text.split("HK$")[-1].replace(",", ""))

    product_dict = {
        "name": product_name_list,
        "price": product_price_list
    }

    return render_template("nike_products.html", product_dict=product_dict)

@app.route("/nike")
def nike_home():
    return render_template("nike_home.html")

@app.route("/")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)
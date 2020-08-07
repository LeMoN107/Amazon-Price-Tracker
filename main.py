import requests                     #pip install requests bs4
from bs4 import BeautifulSoup

URL = 'https://www.amazon.com.au/GeForce-RTX-2060-Architecture-6G/dp/B07MQ36Z6L/ref=sr_1_1?dchild=1&keywords=gtx+2060&qid=1596768907&s=home&sr=1-1'
    #webpage that you want to get price off
headers = {
    "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'}
    #go into your browser and type "my user agent"
def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text() #Gets product name
    price = soup.find(id="priceblock_ourprice").get_text() #Gets product price
    converted_price = price[0:8] #Takes first 8 numbers from price.
    print(title.strip())
    print(converted_price)

check_price()

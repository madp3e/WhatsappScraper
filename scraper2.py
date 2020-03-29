from bs4 import BeautifulSoup

import requests

def scraper2(url):

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/79.0.3945.88 Safari/537.36"}

    source = requests.get(url, headers=headers).text
    soup = BeautifulSoup(source, "lxml")

    tax_price = soup.find("p", class_="decTxtTaxIncPrice").text

    item_name = soup.find("h1", property="auction:Title").text

    try:
        item_price = soup.find("p", property="auction:BidOrBuyPrice").text

    except:
        try:
            if int(tax_price[3]) > 0:
                item_price = tax_price
            else:
                item_price = soup.find("p", property="auction:Price").text
        except:
            if int(tax_price[2]) > 0:
                item_price = tax_price
            else:
                item_price = soup.find("p", property="auction:Price").text
    try:
        converted_price = int("".join(item_price.split("円")[0].split(",")))

    except:
        converted_price = "".join(tax_price[3:].split("円")[0].split(","))

    return item_name, converted_price

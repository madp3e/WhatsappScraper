from bs4 import BeautifulSoup

import requests

def scraper2(url):
    # url = "https://page.auctions.yahoo.co.jp/jp/auction/u338419633"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/79.0.3945.88 Safari/537.36"}

    source = requests.get(url, headers=headers).text
    soup = BeautifulSoup(source, "lxml")

    item_name = soup.find("h1", class_="ProductTitle__text").text

    item_price_tax = int("".join(soup.find("span", class_="Price__tax").text[3:].strip().split("円")[0].strip().split(",")))

    item_prices = [item_price.text.strip() for item_price in soup.findAll("dd", class_="Price__value")]

    if item_price_tax == 0:

        if len(item_prices) > 1:
            item_price = int("".join(item_prices[1].split("円")[0].split(","))) #sokuketsu
            return item_name, item_price
        else:
            item_price = int("".join(item_prices[0].split("円")[0].split(",")))
            return item_name, item_price

    else:
        item_price = item_price_tax
        return item_name, item_price


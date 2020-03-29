from bs4 import BeautifulSoup

import requests


def scraper(url):
    # url = "https://item.mercari.com/jp/m33095911983"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/79.0.3945.88 Safari/537.36"}

    source = requests.get(url, headers=headers).text
    soup = BeautifulSoup(source, "lxml")

    try:
        item_name = soup.find("h1", class_="item-name").text
        item_price = soup.find("span", class_="item-price bold").text[1:].split(",")
        converted_price = int("".join(item_price))

        return item_name, converted_price
    except:
        print("Item not exist or deleted")

        return "no item", 0


import gspread
import json
import datetime

from oauth2client.service_account import ServiceAccountCredentials
from scraper import scraper
from scraper2 import scraper2

def update_sheet():
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    credential = ServiceAccountCredentials.from_json_keyfile_name("Spreadsheet-7d40ecda88b4.json", scope)
    google_sheet = gspread.authorize(credential)

    # Change sheet name here
    work_sheet = google_sheet.open("M 13").worksheet("2020/05") # Tukar sini

    with open("link.json") as f:
        data = json.load(f)

    keys = [key for key in data["MERCARI_LINK"]]  # get the name of key used in link.json

    # url = "".join(data["MERCARI_LINK"][keys[len(keys) - 1]][-1])

    # Change json dict name here *got 2 places
    # If add new link insert the range from link
    for i in range(len(data["MERCARI_LINK"]["M13"])): # Tukar sini
        url = data["MERCARI_LINK"]["M13"][i] # Tukar sini

        if url[8:20] == "item.mercari":

            print("item mercari ni")
            # new_link_index = data["MERCARI_LINK"][keys[i]].index(url)

            item_name = scraper(url)[0]  # change to url later using whatsapp scraper
            item_price = scraper(url)[1]  # change to url later using whatsapp scraper

            work_sheet.update_acell("I{}".format(i + 4), format(str(datetime.date.today())))
            work_sheet.update_acell("B{}".format(i + 4), item_name)

            # Change json dict name here
            work_sheet.update_acell("C{}".format(i + 4),
                                    data["MERCARI_LINK"]["M13"][i]) # Tukar sini
            work_sheet.update_acell("D{}".format(i + 4), item_price)

        elif url[8:21] == "page.auctions":  # Yahoo auction item

            print("item yahoo auction")
            item_name = scraper2(url)[0]
            item_price = scraper2(url)[1]
            # new_link_index = data["MERCARI_LINK"][keys[i]].index(url)

            work_sheet.update_acell("I{}".format(i + 4), format(str(datetime.date.today())))
            work_sheet.update_acell("B{}".format(i + 4), item_name)

            # Change json dict name here
            work_sheet.update_acell("C{}".format(i + 4),
                                    data["MERCARI_LINK"]["M13"][i]) # Tukar sini
            work_sheet.update_acell("D{}".format(i + 4), item_price)
        
        else:
            print("MANTUL")
            work_sheet.update_acell("B{}".format(i + 4), "check sdiri ejas")
            work_sheet.update_acell("C{}".format(i + 4),
                                data["MERCARI_LINK"]["M13"][i]) # Tukar sini


update_sheet()

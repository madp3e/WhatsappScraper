import gspread
import json
import datetime

from oauth2client.service_account import ServiceAccountCredentials
from scraper import scraper
from scraper2 import scraper2


def update_sheet(url, i):
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    credential = ServiceAccountCredentials.from_json_keyfile_name("Spreadsheet-7d40ecda88b4.json", scope)
    google_sheet = gspread.authorize(credential)

    work_sheet = google_sheet.open("M 0{}".format(i + 1) if i < 9 else "M {}".format(i + 1)).worksheet("2020/03")
    with open("link.json") as f:
        data = json.load(f)

    keys = [key for key in data["MERCARI_LINK"]]  # get the name of key used in link.json

    # url = "".join(data["MERCARI_LINK"][keys[len(keys) - 1]][-1])
    if url[8:19] == "www.mercari":

        print("item mercari ni")

        new_link_index = data["MERCARI_LINK"][keys[i]].index(url)

        item_name = scraper(url)[0]  # change to url later using whatsapp scraper
        item_price = scraper(url)[1]  # change to url later using whatsapp scraper

        work_sheet.update_acell("N{}".format(new_link_index + 4), format(str(datetime.date.today())))
        work_sheet.update_acell("B{}".format(new_link_index + 4), item_name)
        work_sheet.update_acell("C{}".format(new_link_index + 4),
                                data["MERCARI_LINK"][keys[i]][new_link_index])
        work_sheet.update_acell("D{}".format(new_link_index + 4), item_price)
        work_sheet.update_acell("U{}".format(new_link_index + 4), "group {}".format(i + 1))

    elif url[8:21] == "page.auctions":  # Yahoo auction item

        print("item yahoo auction")

        new_link_index = data["MERCARI_LINK"][keys[i]].index(url)

        item_name = scraper2(url)[0]
        item_price = scraper2(url)[1]

        work_sheet.update_acell("N{}".format(new_link_index + 4), format(str(datetime.date.today())))
        work_sheet.update_acell("B{}".format(new_link_index + 4), item_name)
        work_sheet.update_acell("C{}".format(new_link_index + 4), data["MERCARI_LINK"][keys[i]][new_link_index])
        work_sheet.update_acell("D{}".format(new_link_index + 4), item_price)
        work_sheet.update_acell("U{}".format(new_link_index + 4), "group {}".format(i + 1))

    else:
        print("MANTUL!")

        new_link_index = data["MERCARI_LINK"][keys[i]].index(url)

        work_sheet.update_acell("N{}".format(new_link_index + 4), format(str(datetime.date.today())))
        work_sheet.update_acell("B{}".format(new_link_index + 4), scraper(url)[0])
        work_sheet.update_acell("C{}".format(new_link_index + 4), data["MERCARI_LINK"][keys[i]][new_link_index])
        work_sheet.update_acell("D{}".format(new_link_index + 4), scraper(url)[1])
        work_sheet.update_acell("U{}".format(new_link_index + 4), "group {}".format(i + 1))
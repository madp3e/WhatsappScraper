import gspread
import json
import datetime

from oauth2client.service_account import ServiceAccountCredentials
from scraper import scraper


def update_sheet():
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    credential = ServiceAccountCredentials.from_json_keyfile_name("Spreadsheet-7d40ecda88b4.json", scope)
    google_sheet = gspread.authorize(credential)

    # Change sheet name here
    work_sheet = google_sheet.open("M 03").worksheet("2020/03") # Tukar sini

    with open("link.json") as f:
        data = json.load(f)

    keys = [key for key in data["MERCARI_LINK"]]  # get the name of key used in link.json

    # url = "".join(data["MERCARI_LINK"][keys[len(keys) - 1]][-1])

    # Change json dict name here *got 2 places
    # If add new link insert the range from link
    for i in range(43, len(data["MERCARI_LINK"]["M03"])): # Tukar sini
        url = data["MERCARI_LINK"]["M03"][i] # Tukar sini

        try:
            # new_link_index = data["MERCARI_LINK"][keys[i]].index(url)

            item_name = scraper(url)[0]  # change to url later using whatsapp scraper
            item_price = scraper(url)[1]  # change to url later using whatsapp scraper

            work_sheet.update_acell("N{}".format(i + 4), format(str(datetime.date.today())))
            work_sheet.update_acell("B{}".format(i + 4), item_name)

            # Change json dict name here
            work_sheet.update_acell("C{}".format(i + 4),
                                    data["MERCARI_LINK"]["M03"][i]) # Tukar sini
            work_sheet.update_acell("D{}".format(i + 4), item_price)

        except:
            # new_link_index = data["MERCARI_LINK"][keys[i]].index(url)

            work_sheet.update_acell("N{}".format(i + 4), format(str(datetime.date.today())))
            work_sheet.update_acell("B{}".format(i + 4), "")
            work_sheet.update_acell("C{}".format(i + 4), url)
            work_sheet.update_acell("D{}".format(i + 4), "")


update_sheet()

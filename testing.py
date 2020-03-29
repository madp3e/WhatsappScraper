import gspread
import json
import datetime

from oauth2client.service_account import ServiceAccountCredentials
from scraper import scraper

# run this from different terminal
def update_sheet():
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    credential = ServiceAccountCredentials.from_json_keyfile_name("Spreadsheet-7d40ecda88b4.json", scope)
    google_sheet = gspread.authorize(credential)

    work_sheet = google_sheet.open("M 02").worksheet("2020/02")

    with open("link.json") as f:
        data = json.load(f)

    last_link = data["MERCARI_LINK"]["M02"][-1]
    all_link = []

    for i in range(4, int(work_sheet.find(last_link).row) + 1):
        # Take all link from google sheet
        all_link.append(work_sheet.acell("C{}".format(i)).value)

    for link in data["MERCARI_LINK"]["M02"]:
        if link not in all_link:
            index = data["MERCARI_LINK"]["M02"].index(link)
            value = ["", scraper(link)[0], link, scraper(link)[1]]
            work_sheet.insert_row(index=index+4, values=value)


update_sheet()

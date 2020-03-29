from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from googlesheet import update_sheet

import time
import json


def scrape_whatsapp():
    driver = webdriver.Chrome()
    driver.get("https://web.whatsapp.com/")

    input("Click Enter after scanning")

    try:
        driver.find_element_by_xpath('//input[@title="Search or start new chat"]').send_keys("MERCARI")

    except Exception:
        driver.find_element_by_xpath('//div[@class="_2S1VP copyable-text selectable-text"]').send_keys("MERCARI")

    while True:
        names = ["MERCARI 0{}".format(x) if x < 10 else "MERCARI {}".format(x) for x in range(1, 14)]
        for name in names:

            index = names.index(name)
            element = WebDriverWait(driver, 100).until(
                EC.visibility_of_element_located((By.XPATH, '//span[@title="{}"]'.format(name))))
            # element = driver.find_element_by_xpath('//span[@title="{}"]'.format(name))

            element.click()
            print(element.text)

            title = WebDriverWait(driver, 100).until(
                EC.visibility_of_element_located((By.XPATH, '//span[@title="{}"]'.format(name)))).text

            if title == element.text:
                print(title + "=" + element.text)
                soup = BeautifulSoup(driver.page_source, "lxml")

                all_urls = []

                for urls in soup.find_all("a", class_="_3FXB1 selectable-text invisible-space copyable-text"):
                    all_urls.append(urls["href"])

                with open("link.json") as f:
                    data = json.load(f)

                keys = [key for key in data["MERCARI_LINK"]]

                for url in all_urls:
                    if url not in data["MERCARI_LINK"][keys[index]]:
                        print("NEW LINK DETECTED!")
                        print("ADDING NEW LINK TO DATABASE..")
                        print()
                        data["MERCARI_LINK"][keys[index]].append(url)
                        f.close()

                        with open("link.json", "w") as nf:
                            json.dump(data, nf, indent=2)
                        nf.close()
                        print("URL SUCCESSFULLY ADDED")
                        print("UPDATING LIST..")
                        print("updated group no = " + str(index + 1))
                        print()

                        update_sheet(url, index)

            # pakoh = WebDriverWait(driver, 100).until(EC.visibility_of_element_located((By.XPATH, '//button['
            #                                                                                    '@class="_2heX1"]')))
            # # pakoh = driver.find_element_by_xpath('//button[@class="_2heX1"]')
            # pakoh.click()

        print("checkin` update  in 3s")
        for i in range(1, 4):
            print(i)
            time.sleep(1)
        print("No update!")


scrape_whatsapp()

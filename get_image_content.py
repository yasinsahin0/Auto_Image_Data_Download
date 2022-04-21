from selenium import webdriver
import os
import time
import pandas as pd

class GetContent:

    def __init__(self):
        self.number_of_scrolls = 1
        self.timer = 2
        self.save_data_path = "html_content/"
        self.class_data_path = "html_content/class_name.csv"

    def downloadContent(self):
        data = pd.read_csv(self.class_data_path)
        for d in data["class"]:
            html_cont = self.getBrowser(d)
            with open("html_content/"+d+".html", "a") as file:
                file.write(html_cont)
            time.sleep(1)


    def getBrowser(self, search_text):
        url = "https://www.google.co.in/search?q=" + search_text + "&source=lnms&tbm=isch"
        driver = webdriver.Firefox()
        driver.get(url)
        for _ in range(self.number_of_scrolls):
            for __ in range(10):
                driver.execute_script("window.scrollBy(0, 1000000)")
                time.sleep(self.timer)
            time.sleep(self.timer)
            try:
                driver.find_element_by_xpath("//input[@value='Show more results']").click()
            except Exception as e:
                print("Less images found:", e)
                break
        html_content = driver.page_source
        time.sleep(2)
        driver.close()
        return html_content

GT = GetContent()
GT.downloadContent()


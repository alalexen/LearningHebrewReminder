from time import sleep

import pytest
from selenium import webdriver
import sys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By as by

url = "https://www.pealim.com/search/?q=%s"
search_word_input = "//input[@id='search-box']"
go_button = "//input[@value='Go']"
view_full_conjugation = "//a[@class='btn btn-primary' and contains(text(), 'View full conjugation')]"
active_forms_title = "//h3[@class='page-header' and contains(text(), 'Active forms')]"

class BasePage:
    def __init__(self, timeout=15):

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_extension('/Users/store/Desktop/extensions/1.9.6_0.crx')

        self.driver = webdriver.Chrome(options=chrome_options)
        self.wait = WebDriverWait(self.driver, timeout=timeout)

    def open_pealim(self, word) -> None:
        """ Open browser and navigate to pealim app"""
        self.driver.get(url % word)
        self.driver.get(url % word)
        self.driver.maximize_window()
        sleep(7)

    def close_addBlock_tabs(self) -> None:
        """ Close all tabs that were opened with addBlock extension, stitch to the main tab"""
        tabs = self.driver.window_handles
        for t in tabs:
            self.driver.switch_to.window(t)
            if "Blocker" in self.driver.title:
                self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.refresh()

    def click_on_element(self, xpath) -> None:
        """ Wait until element is displayed and click """
        element = self.wait_until_element_displayed(xpath)
        element.click()

    def wait_until_element_displayed(self, element):
        element = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((by.XPATH, element)))
        return element

    def fill_input_with_text(self, input_xpath, text) -> None:
        """ Wait until input is displayed and fill the text """
        element = self.wait_until_element_displayed(input_xpath)
        element.send_keys(text)


class AddWord(BasePage):

    def test_view_full_conjugation(self) -> None:
        self.click_on_element(view_full_conjugation)
        self.wait_until_element_displayed(active_forms_title)


search_word = AddWord(15)
search_word.open_pealim("לייצר")
search_word.close_addBlock_tabs()
search_word.test_view_full_conjugation()




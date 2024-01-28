import os
from time import sleep
import locators as xpath
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By as by


class BasePage:
    def __init__(self, timeout=15):
        self.url = "https://www.pealim.com"
        self.search_word_url = "https://www.pealim.com/search/?q=%s"

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_extension("/Users/store/Desktop/extensions/1.9.6_0.crx")

        self.driver = webdriver.Chrome(options=chrome_options)
        self.wait = WebDriverWait(self.driver, timeout=timeout)

    def navigate_to_url(self, url) -> None:
        self.driver.get(url)
        self.driver.refresh()  # add block issue

    def open_pealim(self) -> None:
        """Open browser and navigate to pealim app"""
        self.navigate_to_url(self.url)
        self.driver.maximize_window()
        sleep(5)
        self.close_addBlock_tabs()

    def close_addBlock_tabs(self) -> None:
        """Close all tabs that were opened with addBlock extension, switch to the main tab"""
        tabs = self.driver.window_handles
        for t in tabs:
            self.driver.switch_to.window(t)
            if "Blocker" in self.driver.title:
                self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

    def click_on_element(self, xpath) -> None:
        """Wait until element is displayed and click"""
        element = self.wait_until_element_displayed(xpath)
        element.click()

    def wait_until_element_displayed(self, element):
        element = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((by.XPATH, element))
        )
        return element

    def fill_input_with_text(self, input_xpath, text) -> None:
        """Wait until input is displayed and fill the text"""
        element = self.wait_until_element_displayed(input_xpath)
        element.send_keys(text)


class AddWord(BasePage):
    def view_full_conjugation(self) -> None:
        self.click_on_element(xpath.view_full_conjugation)
        self.wait_until_element_displayed(xpath.meaning_title)

    def get_all_conjugations(self) -> str:
        """Get all conjugations
        :return: String with conjugations separated by comma
        """
        all_forms = ""
        all_forms += (
            self.driver.find_element(by.XPATH, value=xpath.conjugation_of).text.replace(
                "Conjugation of ", ""
            )
            + ","
        )

        for i in list(xpath.conjugations.values())[1:]:
            form = self.driver.find_element(
                by=by.XPATH, value=xpath.conjugation % i
            ).text
            all_forms += form + ","

        return all_forms.replace("*", "")[:-1]

    def get_translation(self) -> str:
        """Get translation"""
        translation = self.driver.find_element(
            by=by.XPATH, value=xpath.translation
        ).text
        return translation.replace(",", ";")

    def add_conjugations_and_translations_to_file(self) -> None:
        conjugations = self.get_all_conjugations()
        translation = self.get_translation()

        verbs_size = os.stat("verbs.csv").st_size
        translations_size = os.stat("verbs_translations.csv").st_size

        with open("verbs.csv", "a") as v:
            v.write(conjugations if verbs_size == 0 else "\n" + conjugations)

        with open("verbs_translations.csv", "a") as t:
            t.write(translation if translations_size == 0 else "\n" + translation)

    def add_verbs_to_file_batch(self, infinitives: list) -> None:
        """Open pealim and search for infinitive from the list.
        Add conjugations to verbs file and translation to translations file
        """
        self.open_pealim()

        for w in infinitives:
            self.navigate_to_url(self.search_word_url % w)
            self.view_full_conjugation()
            self.add_conjugations_and_translations_to_file()
            print(f"Added the word {w}")
        print("**** Words were successfully added to verbs.csv ****")









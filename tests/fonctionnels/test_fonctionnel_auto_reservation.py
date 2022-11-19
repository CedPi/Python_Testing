from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


def test_route_reservation():
    # browser = webdriver.Chrome("tests/fonctionnels/chromedriver")
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    browser.get("http://127.0.0.1:5000/")
    time.sleep(8)
    email = browser.find_element(By.ID, "input_email")
    time.sleep(2)
    email.send_keys("kate@shelifts.co.uk")
    time.sleep(2)
    cn_button = browser.find_element(By.ID, "submit_email")
    cn_button.click()
    time.sleep(2)

    book_link = browser.find_element(By.ID, "book_Spring Festival")
    book_link.click()
    time.sleep(2)
    nb_places = browser.find_element(By.ID, "input_nb_places")
    nb_places.send_keys("2")
    time.sleep(2)
    bk_button = browser.find_element(By.ID, "submit_booking")
    bk_button.click()
    time.sleep(2)

    logout_link = browser.find_element(By.ID, "link_logout")
    logout_link.click()
    time.sleep(2)

    browser.close()
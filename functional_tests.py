"""Place where the user experience will be tested."""

from selenium import webdriver
import time

browser = webdriver.Firefox()
# Bob visits homepage of Umblr
browser.get('http://127.0.0.1:8000/')
time.sleep(3)
browser.quit()

# Bob visits homepage and sees title Umblr and navigation bar

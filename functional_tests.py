"""Place where the user experience will be tested."""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        time.sleep(1)

    def tearDown(self):
        self.browser.quit()

    def test_homepage(self):
        # Bob visits homepage of Umblr
        self.browser.get('http://127.0.0.1:8000/')
        # Bob visits homepage and sees title Umblr 
        self.assertIn('Umblr', self.browser.title)

    def test_sign_up(self):
        self.browser.get('http://127.0.0.1:8000/')
        # Bob clicks the option to sign-up
        self.browser.find_element_by_link_text('Sign up').click()
        # Bob enters username, email, password twice and submits it
        inputbox = self.browser.find_element_by_id('id_username')
        inputbox.send_keys('Bobfake')
        inputbox = self.browser.find_element_by_id('id_email')
        inputbox.send_keys('Bob@bobfake.com')
        # inputbox = self.browser.find_element_by_id('id_password')
        # inputbox.send_keys('necklace')
        # inputbox = self.browser.find_element_by_id('id_password')
        # inputbox.send_keys('necklace')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        # why does this test pass even though it is not possible to hit enter w/o password
        # why does id_password not work

    def test_login(self):
        self.browser.get('http://127.0.0.1:8000/')
        # Bob clicks the option to login
        self.browser.find_element_by_link_text('Login').click()
        # Bob enters his username and password and submits it
        inputbox = self.browser.find_element_by_id('id_username')
        inputbox.send_keys('Bob')
        inputbox = self.browser.find_element_by_id('id_password')
        inputbox.send_keys('necklace')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)


if __name__ == '__main__':
    unittest.main(warnings='ignore')

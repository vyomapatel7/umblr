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

        # After logging in Bob can create a blog by clicking on create blog
        # Bob can then enter a title and text for his blog and submit it
        # After submitting the data Bob is redirected to his blog
        
        # Bob can edit his blog by clicking on edit blog 
        # Bob can submit the edits to his blog

        # Bob can delete his blog by clicking on delete
        # Bob is asked if he is sure he wants to delete his blog

        # Bob can create a post by clicking on create post
        # Bob can enter a title and text for his post and submit it

        # Bob can edit his post by clicking on edit post 
        # Bob can submit the edits to his post

        # Bob can delete his post by clicking on delete post
        # Bob is asked if he is sure he wants to delete his post

        # Bob can view the about page for his blo



if __name__ == '__main__':
    unittest.main(warnings='ignore')

"""Place where the user experience will be tested."""

from selenium import webdriver
import time
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        time.sleep(3)

    def tearDown(self):
        self.browser.quit()

    def test_homepage(self):
        # Bob visits homepage of Umblr
        self.browser.get('http://127.0.0.1:8000/')
        # Bob visits homepage and sees title Umblr and navigation bar
        self.assertIn('Umblr', self.browser.title)


if __name__ == '__main__':
    unittest.main(warnings='ignore')

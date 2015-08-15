import unittest

from selenium import webdriver


class FunctionalTests(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(2)

    def tearDown(self):
        self.browser.quit()

    def test_get_home_page(self):
        self.browser.get('http://localhost:8000/')
        self.assertIn('Home', self.browser.title)


if __name__ == '__main__':
    unittest.main()

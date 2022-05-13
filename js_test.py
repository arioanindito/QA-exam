import time
import unittest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class TestJavascriptError(unittest.TestCase):
    """javacript_error
    http://the-internet.herokuapp.com/javascript_error"""

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.base_url = "http://the-internet.herokuapp.com/javascript_error"
        self.driver.maximize_window()
        time.sleep(1)
        self.driver.get(self.base_url)

    def test_javascript_error(self):
        "test_javascript_error"
        driver = self.driver
        driver.save_screenshot("js_error.png")

    def tearDown(self):
        time.sleep(1)
        self.driver.close()


if __name__ == '__main__':
    unittest.main()

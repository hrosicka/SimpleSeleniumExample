import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import *
from selenium.webdriver.support.ui import WebDriverWait
import logging


class ChromeMenuTest(unittest.TestCase):
    """
    This test class defines automated test cases for interacting with links on the Python website using Selenium and Chrome webdriver.
    It utilizes logging to record informative messages and explicit waits for reliable page interactions.
    """

    def setUp(self):
        """
        Initializes a new Chrome webdriver instance and configures logging.
        """
        logging.basicConfig(level=logging.INFO, filename="py_log.log", filemode="w")

        logging.info("Initializing Chrome webdriver...")
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(options=options)


    def test_menu_link_psf_newsletter(self):
        """
        Verifies navigation to the "PSF Newsletter Signup" page by clicking the "PSF Newsletter" link.
        """

        logging.info("Testing navigation to 'PSF Newsletter Signup' page...")

        # Get the Chrome webdriver instance
        driver = self.driver

        # Open the Python website
        driver.get("https://www.python.org")

        # Verify the page title contains "Python"
        self.assertIn("Python", driver.title)

        psf_newsletter_link_xpath = "//li[@class='tier-1 element-6']/ul[@class='subnav menu']/li[2]"
        news_link = WebDriverWait(driver, 10).until(  # Explicit wait for element presence
            presence_of_element_located((By.XPATH, psf_newsletter_link_xpath))
        )
        news_link.click()

        expected_url = "https://www.python.org/psf/newsletter/"
        actual_url = driver.current_url
        self.assertEqual(actual_url, expected_url)

        logging.info("Navigation to 'PSF Newsletter Signup' page successful!")

    def test_menu_link_psf_news(self):
        """
        Verifies navigation to the "News from the Python Software Foundation" page by clicking the "PSF News" link.
        """

        logging.info("Testing navigation to 'News from the Python Software Foundation' page...")

        # Get the Chrome webdriver instance
        driver = self.driver

        # Open the Python website
        driver.get("https://www.python.org")

        # Verify the page title contains "Python"
        self.assertIn("Python", driver.title)

        psf_news_link_xpath = "//li[@class='tier-1 element-6']/ul[@class='subnav menu']/li[3]"
        news_link = WebDriverWait(driver, 10).until(  # Explicit wait for element presence
            presence_of_element_located((By.XPATH, psf_news_link_xpath))
        )
        news_link.click()

        expected_url = "https://pyfound.blogspot.com/"
        actual_url = driver.current_url
        self.assertEqual(actual_url, expected_url)

        logging.info("Navigation to 'News from the Python Software Foundation' page successful!")


    def tearDown(self):
        """
        This method closes the Chrome webdriver instance after each test case.
        """

        logging.info("Closing Chrome webdriver...")
        self.driver.close()

if __name__ == "__main__":
    """
    Executes the test suite if the script is run directly.
    """

    print("Running test suite...")
    unittest.main()
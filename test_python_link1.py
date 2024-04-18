import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class ChromeLinksTest(unittest.TestCase):
    """
    This test class defines automated test cases for interacting with links on the Python website using Selenium and Chrome webdriver.
    """

    def setUp(self):
        """
        Initializes a new Chrome webdriver instance before each test case.
        """
        
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])

        print("Initializing Chrome webdriver...")
        self.driver = webdriver.Chrome()

    def test_search_pypi_link(self):
        """
        This test case verifies that clicking the "PyPI" link on the Python website redirects the user to the expected PyPI URL.
        """

        print("Testing navigation to PyPI using the 'PyPI' link...")

        # Get the Chrome webdriver instance
        driver = self.driver

        # Open the Python website
        driver.get("https://www.python.org")

        # Verify the page title contains "Python"
        self.assertIn("Python", driver.title)

        # Find the "PyPI" link element using its link text
        pypi_link = driver.find_element(By.LINK_TEXT, "PyPI")

        # Click on the "PyPI" link
        pypi_link.click()

        # Wait for 3 seconds for the page to load
        time.sleep(3)

        print("Navigation to PyPI using 'PyPI' link test passed!")
        expected_url = "https://pypi.org/"
        actual_url = driver.current_url
        self.assertEqual(actual_url, expected_url)

        print("Search with Enter key test passed!")

    def tearDown(self):
        """
        This method closes the Chrome webdriver instance after each test case.
        """

        print("Closing Chrome webdriver...")
        self.driver.close()

if __name__ == "__main__":
	"""
    This block checks if the script is run directly (not imported as a module) and executes the test cases.
    """

	print("Running test suite...")
	unittest.main()
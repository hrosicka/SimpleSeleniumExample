import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class ChromeSearch(unittest.TestCase):
    """
    This class contains automated test cases for searching on the Python website using Selenium and Chrome webdriver.
    """

    def setUp(self):
        """
        This method initializes the Chrome webdriver and sets it up for the test cases.
        """
        
        print("Initializing Chrome webdriver...")
        self.driver = webdriver.Chrome()

    def test_search_in_python_org_enter(self):
        """
        This test case searches for "matplotlib" on the Python website using the search bar and hitting Enter.
        """

        print("Testing search with Enter key...")

        # Get the Chrome webdriver instance
        driver = self.driver

        # Open the Python website
        driver.get("https://www.python.org")

        # Verify the page title contains "Python"
        self.assertIn("Python", driver.title)

        # Find the search bar element using its name attribute
        elem = driver.find_element(By.NAME, "q")

        # Enter "matplotlib" in the search bar
        elem.send_keys("matplotlib")

        # Simulate pressing Enter to submit the search
        elem.send_keys(Keys.RETURN)

        # Wait for 3 seconds for the page to load
        time.sleep(3)
        
        # Assert that the current URL matches the expected search results URL
        expected_url = "https://www.python.org/search/?q=matplotlib&submit="
        actual_url = driver.current_url
        self.assertEqual(actual_url, expected_url)

        print("Search with Enter key test passed!")

    def test_search_in_python_org_go(self):
        """
        This test case searches for "python3" on the Python website using the search bar and clicking the "Go" button.
        """

        print("Testing search with Go button...")
    
        # Get the Chrome webdriver instance
        driver = self.driver

        # Open the Python website
        driver.get("https://www.python.org")

        # Verify the page title contains "Python"
        self.assertIn("Python", driver.title)

        # Find the search bar element using its name attribute
        elem = driver.find_element(By.NAME, "q")

        # Enter "python3" in the search bar
        elem.send_keys("python3")

        # Find the "Go" button element using its ID attribute
        button = driver.find_element(By.ID, "submit")

        # Click the "Go" button to submit the search
        button.click()

        # Wait for 3 seconds for the page to load
        time.sleep(3)

        # Assert that the current URL matches the expected search results URL
        expected_url = "https://www.python.org/search/?q=python3&submit="
        actual_url = driver.current_url
        self.assertEqual(actual_url, expected_url)

        print("Search with Go button test passed!")


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
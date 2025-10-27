# Automated Python Website Testing with Selenium and Chrome

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/Selenium-Automation-green)](https://www.selenium.dev/)
![Stars](https://img.shields.io/github/stars/hrosicka/SimpleSeleniumExample)
![Made with Love](https://img.shields.io/badge/Made%20with-%E2%9D%A4-red)
![Last Commit](https://img.shields.io/github/last-commit/hrosicka/SimpleSeleniumExample)

A concise example repository demonstrating how to automate browser interactions with [Selenium](https://www.selenium.dev/) and Chrome WebDriver in Python. The example focuses on interacting with the official [python.org](https://www.python.org/) website.

---

## Features

- **Test-Driven Approach:** All functionality is covered by unit tests using Python's built-in `unittest` framework.
- **Beginner-Friendly:** Clear class organization, comprehensive comments, and step-by-step explanations make this repository accessible to those new to Selenium or automated testing.
- **Focused Testing:** The repository targets specific website features and provides a solid base for building more advanced test suites.
- **Easy to Extend:** The modular structure allows for straightforward addition of new tests or adaptation to other web applications.

---

## Getting Started

### Prerequisites

- Python 3.x
- Google Chrome browser
- [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/) (ensure it matches your Chrome version)
- Selenium (`pip install selenium`)

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/hrosicka/SimpleSeleniumExample.git
   cd SimpleSeleniumExample
   ```
2. Install required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

### Running Tests

```sh
python -m unittest discover
```

---

## File Structure

- `test_*.py`: Test scripts with organized test classes and detailed comments.
- `requirements.txt`: List of Python dependencies.

---

## Author

Lovingly crafted by [Hanka Robovska](https://github.com/hrosicka) 👩‍🔬

---

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.


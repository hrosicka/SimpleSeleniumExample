# Automated Python Website Testing with Selenium and Chrome

<div align="center">

  <a href="https://github.com/hrosicka/SimpleSeleniumExample/stargazers">
    <img src="https://img.shields.io/github/stars/hrosicka/SimpleSeleniumExample?style=for-the-badge&color=4F8EF7&logo=starship&logoColor=white" alt="Stars" />
  </a>
  <a href="https://github.com/hrosicka/SimpleSeleniumExample/network/members">
    <img src="https://img.shields.io/github/forks/hrosicka/SimpleSeleniumExample?style=for-the-badge&color=4F8EF7&logo=git&logoColor=white" alt="Forks" />
  </a>
  <a href="https://github.com/hrosicka/SimpleSeleniumExample/commits/master">
    <img src="https://img.shields.io/github/last-commit/hrosicka/SimpleSeleniumExample?style=for-the-badge&color=6366F1&logo=githubactions&logoColor=white" alt="Last Commit" />
  </a>
  <a href="https://github.com/hrosicka/SimpleSeleniumExample/issues">
    <img src="https://img.shields.io/github/issues/hrosicka/SimpleSeleniumExample?style=for-the-badge&color=F59E0B&logo=github&logoColor=white" alt="Issues" />
  </a>
  <br/>

  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.x" />
  </a>
  <a href="https://www.selenium.dev/">
    <img src="https://img.shields.io/badge/Selenium-Automation-43B02A?style=for-the-badge&logo=selenium&logoColor=white" alt="Selenium Automation" />
  </a>
  <a href="https://www.google.com/chrome/">
    <img src="https://img.shields.io/badge/Browser-Chrome-F59E0B?style=for-the-badge&logo=googlechrome&logoColor=white" alt="Google Chrome" />
  </a>
  <img src="https://img.shields.io/badge/Testing-unittest-334155?style=for-the-badge&logo=pytest&logoColor=white" alt="Testing: unittest" />
  <br/>

  <img src="https://img.shields.io/badge/For-Beginners-22C55E?style=for-the-badge&logo=sparkles&logoColor=white" alt="Beginner Friendly" />
  <img src="https://img.shields.io/badge/Made%20With-Love-EC4899?style=for-the-badge&logo=sparkles&logoColor=white" alt="Made with Love" />
  <a href="./LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-10B981?style=for-the-badge&logo=opensourceinitiative&logoColor=white" alt="License: MIT" />
  </a>

</div>

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


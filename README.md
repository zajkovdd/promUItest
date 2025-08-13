# promUItest
promUItest
Overview
promUItest is an automated UI testing project for the promminer.ru website. The project uses Python, Selenium WebDriver, and Pytest to perform functional testing of the website's user interface, including search and comparison features. Allure is integrated for generating detailed test reports.
Features

Automated UI tests for key functionalities of promminer.ru.
Support for search functionality testing.
Support for product comparison testing.
Detailed test reporting with Allure.
Modular page object model (POM) design for maintainability.

Prerequisites
Before running the tests, ensure you have the following installed:

Python 3.8+
pip (Python package manager)
Web browser (e.g., Google Chrome) and corresponding WebDriver (e.g., ChromeDriver)
Git (optional, for cloning the repository)

Installation

Clone the repository:
git clone https://github.com/zajkovdd/promUItest.git
cd promUItest


Set up a virtual environment (optional but recommended):
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install dependencies:
pip install -r requirements.txt

Ensure you have a requirements.txt file with the following dependencies:
pytest
selenium
allure-pytest


Install WebDriver:

Download and configure the appropriate WebDriver (e.g., ChromeDriver) for your browser.
Ensure the WebDriver executable is in your system's PATH.



Usage

Run tests:To execute all tests, use the following command:
pytest tests/


Generate Allure reports:To generate and view Allure reports, run:
pytest --alluredir=./allure-results
allure serve allure-results


Test structure:

Tests are located in the tests/ directory.
Page objects are defined in helper classes (e.g., BasePageHelper, CatalogPageHelper, ComparePageHelper).
Example test: test_compare_two_asic_positive verifies the comparison of two ASIC products.



Project Structure
promUItest/
│
├── tests/                   # Test cases
│   └── test_compare_asic.py # Example test for ASIC comparison
├── helpers/                 # Page object models
│   ├── base_page.py        # Base page helper
│   ├── catalog_page.py     # Catalog page helper
│   └── compare_page.py     # Compare page helper
├── requirements.txt         # Project dependencies
└── README.md               # This file

Contributing
Contributions are welcome! To contribute:

Fork the repository.
Create a new branch (git checkout -b feature/your-feature).
Commit your changes (git commit -m "Add your feature").
Push to the branch (git push origin feature/your-feature).
Create a Pull Request.

License
This project is licensed under the MIT License. See the LICENSE file for details.
Contact
For questions or suggestions, contact the project maintainer at GitHub Issues.

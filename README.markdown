# promUItest

## Overview

`promUItest` is an automated UI testing project for the [promminer.ru](https://promminer.ru/) website. The project uses Python, Selenium WebDriver, and Pytest to perform functional testing of the website's user interface, including search and comparison features. Allure is integrated for generating detailed test reports.

## Features

- Automated UI tests for key functionalities of promminer.ru.
- Support for search functionality testing.
- Support for product comparison testing (e.g., ASICs).
- Detailed test reporting with Allure.
- Modular page object model (POM) design for maintainability.

## Prerequisites

Before running the tests, ensure you have the following installed:

- Python 3.8+
- pip (Python package manager)
- Web browser (e.g., Google Chrome) and corresponding WebDriver (e.g., ChromeDriver)
- Git (optional, for cloning the repository)

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/zajkovdd/promUItest.git
   cd promUItest
   ```

2. **Set up a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

   Example `requirements.txt`:
   ```
   pytest
   selenium
   allure-pytest
   ```

4. **Install WebDriver**:
   - Download and configure the appropriate WebDriver (e.g., [ChromeDriver](https://chromedriver.chromium.org/downloads)) for your browser.
   - Ensure the WebDriver executable is in your system's PATH.

## Usage

1. **Run tests**:
   To execute all tests, run from the project root:
   ```bash
   pytest tests/
   ```

2. **Generate Allure reports**:
   To generate and view Allure reports, run:
   ```bash
   pytest --alluredir=./allure-results
   allure serve allure-results
   ```

3. **Test structure**:
   - Tests are located in the `tests/` directory.
   - Page objects are defined in the `pages/` directory (e.g., `BasePageHelper`, `CatalogPageHelper`, `ComparePageHelper`, `SearchPageHelper`).
   - Example tests:
     - `test_compare.py`: Verifies the comparison of two ASIC products.
     - `test_search.py`: Tests the search functionality.

## Project Structure

```
promUItest/
│
├── pages/                   # Page object models
│   ├── __init__.py         # Makes pages a Python module
│   ├── BasePage.py        # Base page helper
│   ├── CatalogPage.py     # Catalog page helper
│   ├── ComparePage.py     # Compare page helper
│   ├── SearchPage.py      # Search page helper
├── tests/                   # Test cases
│   ├── conftest.py         # Pytest fixtures (e.g., browser)
│   ├── test_compare.py     # Test for ASIC comparison
│   └── test_search.py      # Test for search functionality
├── requirements.txt         # Project dependencies
└── README.md               # This file
```

## Troubleshooting

- **ModuleNotFoundError: No module named 'pages'**:
  - Ensure the `pages/` directory exists and contains `BasePage.py`, `CatalogPage.py`, `ComparePage.py`, and `SearchPage.py`.
  - Verify that `pages/__init__.py` exists (can be empty).
  - Check imports in test files:
    ```python
    from pages.BasePage import BasePageHelper
    from pages.CatalogPage import CatalogPageHelper
    from pages.ComparePage import ComparePageHelper
    from pages.SearchPage import SearchPageHelper
    ```
  - Add the project root to `PYTHONPATH`:
    ```bash
    export PYTHONPATH=$PYTHONPATH:/Users/dmitrijzajkov/PycharmProjects/promUItest
    ```
  - In PyCharm, add the project root to the Python interpreter paths:
    - File > Settings > Project > Python Interpreter > Show All > Add Content Root.

- **ModuleNotFoundError: No module named 'core'**:
  - The `browser` fixture is defined in `tests/conftest.py`. Ensure imports in test files use:
    ```python
    from conftest import browser
    ```

## Contributing

Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m "Add your feature"`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Create a Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For questions or suggestions, contact the project maintainer at [GitHub Issues](https://github.com/zajkovdd/promUItest/issues).
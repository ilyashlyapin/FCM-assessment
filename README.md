# FCM assessment with Sauce Demo Automated Test

This project contains FCM assessment with automated test for the Sauce Demo application using Python, Playwright, and pytest.

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## Installation and test run

### Step 1: Clone the repository

```sh
git clone https://github.com/ilyashlyapin/FCM-assessment.git
cd FCM-assessment
```

### Step 2: Create and activate a virtual environment

```sh
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Step 3: Install required libraries

```sh
pip install -r requirements.txt
playwright install
```

### Step 4: Run the tests

```sh
pytest --html=report.html test/test_saucedemo.py
```

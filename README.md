# AI Test Automation Framework

This is a tool for automating UI tests using AI-powered tools like Google Gemini and browser automation. The framework is designed to be **modular**, **scalable**, and **easy to use**, with support for running individual tests or a suite of tests, and generating detailed reports.

---

## 🔧 Features

- **AI-Powered Testing**: Uses Google Gemini for natural language processing and task execution.  
- **Browser Automation**: Integrates with browser automation tools to perform UI tasks.  
- **Modular Design**: Tests are organized into separate files for easy maintenance.  
- **Reporting**: Generates JSON, CSV, and HTML reports for test results.  
- **Dynamic Test Execution**: Supports running individual tests without modifying the code.  
- **Asynchronous Execution**: Uses `asyncio` for efficient task execution.

---

## 🧱 Prerequisites

- Python 3.8 or higher  
- Pip (Python package manager)

---

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/sourcefuse/sourcefuse-ai-automation.git
cd sourcefuse-ai-automation

# Set up a virtual environment (optional but recommended)
python3 -m venv .venv
source .venv/bin/activate    # On macOS/Linux
.venv\Scripts\activate       # On Windows

# Install dependencies
pip install -r requirements.txt

# Set up environment variables:
Create a .env file in the root directory and add your Gemini API key:

Gemini_API_Key=your_api_key_here

# Project Structure

project/
│
├── engine/
│   ├── base.py            # Base framework class
│   └── reporter.py        # Reporting functionality
│
├── tests/
│   ├── test_login.py         # Login test case
│   ├── test_add_to_cart.py   # Add to cart test case
│   ├── test_remove_from_cart.py  # Remove from cart test case
│   └── __init__.py
│
├── reports/              # Directory for generated reports
├── config.py             # Configuration settings
├── run.py                # Main script to run all tests
├── run_single_test.py    # Script to run a single test
├── requirements.txt      # List of dependencies

🚀 Usage

**Run All Tests**

    python3 run.py

This will execute all test cases in the tests/ directory and generate JSON, CSV, and HTML reports in the reports/ folder.

**Run a Single Test**

    python3 run_single_test.py tests.test_login LOGIN_TASK
    
This will execute only the LOGIN_TASK from the tests/test_login.py file.

🧪 Example Test Case

Login Test (tests/test_login.py):

LOGIN_TASK = (
    'Important : I am UI Automation tester validating the tasks '
    'Open website https://www.saucedemo.com/ '
    'Login with username and password '
    'Verify user gets logged in to the website'
)

📊 Reporting

Reports are generated in the reports/ directory:

 - JSON Report: Detailed results in JSON format
 - CSV Report: Tabular view of results
 - HTML Report: Visually formatted summary

➕ Adding New Tests

1. Create a new file in tests/ (e.g., tests/test_checkout.py)

2. Define a new task:

CHECKOUT_TASK = (
    'Important : I am UI Automation tester validating the tasks '
    'Open website https://www.saucedemo.com/ '
    'Login with username and password '
    'Proceed to checkout '
    'Verify checkout is successful'
)

Run the new test:

    python3 run_single_test.py tests.test_checkout CHECKOUT_TASK

🛠 Troubleshooting

1. ModuleNotFoundError
 Make sure dependencies are installed:

    pip install -r requirements.txt

2. API Key Not Found
 Ensure .env contains your Gemini API key:

    Gemini_API_Key=your_api_key_here
    
3. Test Not Found
 Double-check the test module and task name when using run_single_test.py.

🤝 Contributing
Contributions are welcome!
To contribute:
Fork the repository

Create a new branch

Submit a pull request with a detailed description

📬 Contact
Name: Ankit Aswal
Email: ankit.aswal@sourcefuse.com
GitHub: ankit0412


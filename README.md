**AI Test Automation Framework**
This is a tool for automating UI tests using AI-powered tools like Google Gemini and 
browser automation. The framework is designed to be modular, scalable, and easy to use, with support for 
running individual tests or a suite of tests and generating detailed reports.

**Features**
* AI-Powered Testing: Uses Google Gemini for natural language processing and task execution.
* Browser Automation: Integrates with browser automation tools to perform UI tasks.
* Modular Design: Tests are organized into separate files for easy maintenance.
* Reporting: Generates JSON, CSV, and HTML reports for test results.
* Dynamic Test Execution: Supports running individual tests without modifying the code.
* Asynchronous Execution: Uses asyncio for efficient task execution.

**Prerequisites**
* Python 3.8 or higher
* Pip (Python package manager)

Installation: 
Clone the repository: 
git clone https://github.com/sourcefuse/sourcefuse-ai-automation.git 
cd your-repo-name 
Set up a virtual environment (optional but recommended): 

python3 -m venv .venv
source .venv/bin/activate  # On macOS/Linux
.venv\Scripts\activate     # On Windows

Install dependencies:

pip install -r requirements.txt
Set up environment variables:
Create a .env file in the root directory and add your Gemini API key:

Gemini_API_Key=your_api_key_here

**Project Structure**

project/

engine/
 - base.py           # Base framework class
 - reporter.py       # Reporting functionality
tests/
 - test_login.py     # Login test case
 - test_add_to_cart.py  # Add to cart test case
 - test_remove_from_cart.py  # Remove from cart test case
    - __init__.py
reports/              # Directory for generated reports
config.py             # Configuration settings
run.py                # Main script to run all tests
run_single_test.py    # Script to run a single test
requirements.txt      # List of dependencies

**Usage** 
Running All Tests 
To run all tests, use the run.py script: 
python3 run.py 

This will execute all test cases defined in the tests/ directory and generate JSON, CSV, and HTML reports in the reports/ folder.

Running a Single Test 
To run a single test, use the run_single_test.py script. Provide the test module and task name as arguments: 
python3 run_single_test.py tests.test_login LOGIN_TASK 
This will execute only the LOGIN_TASK from the tests/test_login.py file. 

Example Test Cases 
Login Test (tests/test_login.py) 

LOGIN_TASK = ( 
    'Important : I am UI Automation tester validating the tasks' 
    'Open website https://www.saucedemo.com/' 
    'Login with username and password' 
    'Verify user gets logged in to the website' 
) 

**Reporting** 
The framework generates the following reports in the reports/ directory: 
* JSON Report: Contains detailed test results in JSON format. 
* CSV Report: Provides a tabular view of test results. 
* HTML Report: Offers a visually appealing summary of test results. 


**Adding New Tests** 
Create a new file in the tests/ directory (e.g., tests/test_checkout.py). 

Define a new task in the file: 

CHECKOUT_TASK = ( 
    'Important : I am UI Automation tester validating the tasks' 
    'Open website https://www.saucedemo.com/' 
    'Login with username and password' 
    'Proceed to checkout' 
    'Verify checkout is successful' 
) 

Run the new test using the run_single_test.py script: 

python3 run_single_test.py tests.test_checkout CHECKOUT_TASK 

**Troubleshooting** 
Common Issues
1. ModuleNotFoundError:
Ensure all dependencies are installed by running:
pip install -r requirements.txt

2. API Key Not Found:
Verify that the .env file contains the correct Gemini_API_Key.

3. Test Not Found:
Double-check the test module and task name when running a single test.

Contributing
Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Submit a pull request with a detailed description of your changes.

**Contact**
For questions or feedback, please contact:

**Name**: Ankit Aswal
**Email**: ankit.aswal@sourcefuse.com
**GitHub**: ankit0412

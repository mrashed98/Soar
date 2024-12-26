# E2E Web Automation with Playwright

Automated end-to-end testing framework using Python Playwright for web application testing with integrated logging and reporting.

## Features
- Page Object Model architecture
- Detailed logging system
- Cross-browser testing support
- Test reporting
- Configurable test execution

## Setup

1. Clone the repository:

```bash
git clone <repository-url>
cd E2E\ Automation\ Test
```

2. Create and activate virtual environment:


```bash
python -m venv venv
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Install Playwright browsers:

```bash
playwright install
```

## Running Tests

### Basic Usage

```bash
pytest                           # Run all tests
pytest --headed                  # Run with visible browser
pytest -v                       # Verbose output
```

### Browser Configuration

```bash
pytest --browser firefox        # Run on Firefox
pytest --browser webkit        # Run on Safari
pytest --slowmo 1000          # Slow down execution
pytest --headless false       # Run in headed mode
```

## Test Selection

```bash
pytest tests/test_basket.py    # Run specific test file
pytest -k "test_checkout"      # Run tests matching pattern
pytest -m "smoke"             # Run smoke tests
```

## Project Structure

```
├── pages/                  # Page Object Models
│   ├── base_page.py       # Base page class
│   ├── basket_page.py     # Basket page actions
│   └── home_page.py       # Home page actions
├── tests/                 # Test files
│   ├── conftest.py       # Test configuration
│   └── test_*.py         # Test modules
├── utils/                # Utilities
│   └── logger.py        # Logging configuration
├── logs/                # Test execution logs
├── reports/             # Test reports
└── requirements.txt     # Project dependencies
```

## Logging
Logs are automatically generated for each test run:

- Location: `logs/test_run_YYYYMMDD_HHMMSS.log`
- Contains: Actions, validations, errors
- View logs: `cat logs/<latest>.log`

## Test Reports
Generate HTML report:

```bash
pytest --html=reports/report.html
```

## Configuration
Browser options in `conftest.py`:

```python
pytest_addoption(parser):
    parser.addoption("--browser", default="chromium")
    parser.addoption("--headless", default=True)
    parser.addoption("--slowmo", default=0)
```

## Debugging
1. Add breakpoint:

```python
import pdb; pdb.set_trace()
```

2. Run with debugging:

```bash
pytest --pdb
```

## Dependencies

- Python 3.7+
- Playwright
- Pytest
- Pytest-Playwright
- Pytest-HTML


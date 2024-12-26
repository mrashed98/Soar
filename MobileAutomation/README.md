# Wikipedia Android App Automation Testing

This project contains automated tests for the Wikipedia Android application using Python, Appium, and Selenium. The tests cover various functionalities including menu navigation, search, and settings management.

## Project Structure

```
MobileAutomation/
├── apk/
│   └── WikipediaSample.apk
├── pages/
│   ├── base_page.py
│   ├── home_page.py
│   ├── search_page.py
│   └── settings_page.py
├── tests/
│   ├── test_task1_menu_navigation.py
│   ├── test_task2_search.py
│   └── test_task3_app_settings.py
└── README.md
```

## Prerequisites

- Python 3.x
- Appium Server
- Android SDK
- Android Emulator or Physical Device
- Required Python packages (install via pip):
  ```bash
  pip install appium-python-client
  pip install selenium
  pip install unittest
  ```

## Setup

1. Clone the repository
2. Start the Appium server
3. Start your Android emulator or connect your Android device
4. Update the device capabilities in the test files if needed

## Test Cases

### 1. Menu Navigation Test (`test_task1_menu_navigation.py`)
Tests the navigation between different menus in the Wikipedia app:
- Explore menu
- My lists menu
- History menu
- Nearby menu

### 2. Search Functionality Test (`test_task2_search.py`)
Validates the search functionality:
- Click on search container
- Enter search text
- Verify search results

### 3. Settings Test (`test_task3_app_settings.py`)
Tests the settings functionality:
- Navigate to settings
- Toggle all switches OFF
- Verify switches state
- Navigate to About page
- Verify About page elements

## Page Objects

### Base Page (`base_page.py`)
Contains common methods and utilities used across all page objects:
- Element finding
- Clicking
- Text input
- Presence verification

### Home Page (`home_page.py`)
Handles interactions with the main page:
- Menu navigation
- Search functionality
- Navigation menu interactions

### Search Page (`search_page.py`)
Manages search-related functionality:
- Search input
- Results handling
- Search suggestions

### Settings Page (`settings_page.py`)
Controls settings-related operations:
- Toggle switches
- About page navigation
- Settings verification

## Running Tests

To run all tests:
```bash
python -m unittest discover -s tests -p "test_*.py"
```

To run a specific test:
```bash
python -m unittest tests/test_task1_menu_navigation.py
python -m unittest tests/test_task2_search.py
python -m unittest tests/test_task3_app_settings.py
```

## Test Reports

Test results will be displayed in the console with:
- Number of tests run
- Test execution time
- Success/failure status
- Error details (if any)

## Common Issues and Solutions

1. **Appium Connection Issues**
   - Ensure Appium server is running
   - Verify port configuration
   - Check device/emulator connection

2. **Element Not Found**
   - Increase implicit wait time
   - Verify element locators
   - Check app state/screen

3. **Test Failures**
   - Review app version compatibility
   - Check device OS version
   - Verify test prerequisites

## Best Practices

1. **Code Organization**
   - Use Page Object Model
   - Maintain clear separation of concerns
   - Keep tests independent

2. **Test Reliability**
   - Add appropriate waits
   - Handle dynamic elements
   - Include proper assertions

3. **Maintenance**
   - Update locators when app changes
   - Keep dependencies updated
   - Document changes

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request


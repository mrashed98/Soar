# Performance and Load Testing Project

## Overview
This project contains performance and load testing scripts designed to evaluate system behavior under various conditions. The tests are implemented using both Artillery for API load testing and Locust for Python-based performance testing, with additional BDD testing using Behave.

## Project Structure
```
PerfermanceAndLoad/
├── README.md
├── Apptim Report.pdf
└── Web/
    ├── artillery/
    │   ├── config.yml      # Artillery test configuration
    │   └── functions.js    # Custom JavaScript functions for Artillery
    ├── features/          # Behave BDD test features
    ├── flask-app/         # Test application
    ├── locustfile.py      # Locust load testing scenarios
    ├── requirements.txt   # Python dependencies
    ├── package.json       # Node.js dependencies
    └── behave.ini        # Behave configuration
```

## Requirements

### Python Dependencies
```
locust==2.15.1
behave==1.2.6
faker==19.3.0
requests==2.31.0
```

### Node.js Dependencies
- Artillery and related plugins (defined in package.json)

## Installation

1. Clone the repository:
   ```bash
   git clone [repository-url]
   cd PerfermanceAndLoad
   ```

2. Install Python dependencies:
   ```bash
   cd Web
   pip install -r requirements.txt
   ```

3. Install Node.js dependencies:
   ```bash
   npm install
   ```

## Usage

### Locust Tests

The project includes a Locust test file (`locustfile.py`) that simulates user behavior for registration and login flows:

1. Start the Locust server:
   ```bash
   cd Web
   locust -f locustfile.py
   ```

2. Access the Locust web interface at http://localhost:8089

Key Features:
- Registration flow (weight: 3)
- Login flow (weight: 2)
- Realistic data generation using Faker
- Configurable wait times between requests (1-3 seconds)

Example test scenario:
```python
@task(3)
def test_registration(self):
    data = {
        'fullName': fake.name(),
        'userName': fake.user_name(),
        'email': fake.email(),
        'password': fake.password(),
        'phone': fake.phone_number()
    }
    self.client.post("/client_registeration", data=data)
```

### Artillery Tests

The project includes Artillery configuration (`artillery/config.yml`) for API load testing:

1. Run the Artillery tests:
   ```bash
   cd Web
   artillery run artillery/config.yml
   ```

Test Phases:
1. Warm up (30s): 1-5 users/second
2. Load test (60s): 5-10 users/second
3. Stress test (30s): 10-20 users/second

Key Features:
- Client Registration Flow (weight: 3)
- Client Login Flow (weight: 2)
- Custom data generation
- Response validation
- Token capture

Example configuration:
```yaml
config:
  target: "http://localhost:5001"
  phases:
    - name: "Warm up"
      duration: 30
      arrivalRate: 1
      rampTo: 5
    - name: "Load test"
      duration: 60
      arrivalRate: 5
      rampTo: 10
```

## Test Types and Implementation

### 1. Load Testing
- Implemented in both Locust and Artillery
- Gradual ramp-up of users
- Realistic data generation
- Response validation

### 2. Stress Testing
- Artillery: Dedicated stress test phase (10-20 users/second)
- Locust: Configurable user count and spawn rate

### 3. Endurance Testing
- Long-running tests possible with both tools
- Customizable duration and user loads

## Analyzing Results

### Locust Results
- Real-time metrics via web interface
- Request statistics
- Response time distributions
- Error rates

### Artillery Results
- JSON reports
- Response time metrics
- Custom metrics via processors
- Success/failure rates


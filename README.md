# VMware Avi Load Balancer – Python Test Automation Framework
## Overview
This project is a Python-based modular test automation framework designed to interact with a mock VMware Avi Load Balancer API.  
The framework demonstrates configuration-driven automation, parallel execution, and a structured validation workflow.

---
## Features
- YAML-driven configuration (API endpoints, credentials, test data)
- Modular framework design
- Parallel test execution
- Mock SSH and RDP automation components
- Authenticated REST API interaction
- Pre-Fetch, Pre-Validation, Task Execution, and Post-Validation stages

---
```
## Project Structure
avi_test_framework/
│
├── config/
│ ├── api_config.yaml
│ ├── test_cases.yaml
│
├── core/
│ ├── api_client.py
│ ├── prefetcher.py
│ ├── validator.py
│ ├── executor.py
│
├── mocks/
│ ├── ssh.py
│ ├── rdp.py
│
├── runner.py
├── requirements.txt
└── README.md
```
---
## Setup Instructions
### 1. Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate
```

### 2. Install Dependencies
```
pip install -r requirements.txt
```

### 3.Configuration
```
config/api_config.yaml
Update with your registered credentials:
base_url: https://semantic-brandea-banao-dc049ed0.koyeb.app
username: your_username
password: your_password
```
```
config/test_cases.yaml
Defines test cases and target Virtual Service:
test_cases:
  - name: Disable Backend Virtual Service
    target_vs_name: backend-vs-t1r_1000-1
```

Execution
```
Run the test framework using:
python runner.py
```

Execution Workflow
- Pre-Fetcher: Fetch tenants, virtual services, and service engines
- Pre-Validation: Validate target Virtual Service is enabled
- Task Execution: Disable Virtual Service using PUT API
- Post-Validation: Verify Virtual Service is disabled

Notes
- SSH and RDP operations are mocked for extensibility
- Framework supports parallel execution using ThreadPoolExecutor
- Designed for easy extension to real infrastructure automation

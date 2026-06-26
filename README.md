# Tichi QA Automation

Automation testing project developed as part of the QA Intern Technical Assignment.

# Document of Testcase

https://docs.google.com/spreadsheets/d/1BPi436bteFdm948Hgw67BOKdnaqH_nV0svNx5nArGZ8/edit?usp=sharing

# Document of Automation Execution Report

https://docs.google.com/document/d/1bzKkTS8Y2nPcNQkZ5RHeJ3C7ycvbicgt-lt8tZqP5iM/edit?usp=sharing


**Tichi Web Application**

https://tichi-app-webapp-stage.web.app

---

## Tech Stack

- Python 3.11.4
- Selenium WebDriver
- Google Chrome
- ChromeDriver

---

## Project Structure

```text
tichi/
│
├── tichi-qa-automation/
│   │
│   ├── login/
│   │   ├── login_page.py
│   │   └── test_login.py
│   │
│   ├── signup/
│   │   ├── signup_page.py
│   │   └── test_signup.py
│   │
│   ├── requirements.txt
│   └── README.md
│
└── venv/
```

---

## Automated Login Test Scenarios

| Test Case ID | Scenario |
|--------------|-----------|
| TC_LOGIN_001 | Login with valid credentials |
| TC_LOGIN_002 | Login with invalid password |
| TC_LOGIN_003 | Login with invalid email |
| TC_LOGIN_004 | Login with empty email |
| TC_LOGIN_005 | Login with empty password |

---

## Automated Signup Test Scenarios

| Test Case ID | Scenario |
|--------------|-----------|
| TC_SIGNUP_001 | Signup with valid details |
| TC_SIGNUP_002 | Password mismatch validation |
| TC_SIGNUP_003 | Password policy validation |
| TC_SIGNUP_004 | Invalid email validation |
| TC_SIGNUP_005 | Terms and Conditions validation |

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd tichi-qa-automation
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / Mac

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Execute Login Automation

```bash
cd login
python test_login.py
```

---

## Execute Signup Automation

```bash
cd signup
python test_signup.py
```

---

## Expected Results

### Login

- Valid users should be able to log in successfully.
- Invalid credentials should display appropriate validation messages.
- Empty mandatory fields should not allow login.

### Signup

- Users should be able to register with valid details.
- Password validation rules should be enforced.
- Password and Confirm Password should match.
- Users should be redirected to the Verify Account page after successful signup.
- Verification email should be displayed correctly.
- Resend Verification option should be available.

---

## Sample Test Output

```text
Running Login Automation Tests

TC_LOGIN_001 PASSED
TC_LOGIN_002 PASSED
TC_LOGIN_003 PASSED
TC_LOGIN_004 PASSED
TC_LOGIN_005 PASSED

Execution Completed
```

---

## Assignment Deliverables

- Test Case Document
- Defect Report
- Selenium Automation Source Code
- Automation Execution Report

---

## Author

Abishek Durao

QA Intern Technical Assignment

# Tichi QA Automation

Automation testing project developed as part of the QA Intern Technical Assignment.

## Application Under Test

**Tichi Web Application**

https://tichi-app-webapp-stage.web.app

---

## Tech Stack

- Python 3.11.4
- Selenium WebDriver
- Google Chrome
- ChromeDriver

---

## Project Structure

```text
tichi/
│
├── tichi-qa-automation/
│   │
│   ├── login/
│   │   ├── login_page.py
│   │   └── test_login.py
│   │
│   ├── signup/
│   │   ├── signup_page.py
│   │   └── test_signup.py
│   │
│   ├── requirements.txt
│   └── README.md
│
└── venv/
```

---

## Automated Login Test Scenarios

| Test Case ID | Scenario |
|--------------|-----------|
| TC_LOGIN_001 | Login with valid credentials |
| TC_LOGIN_002 | Login with invalid password |
| TC_LOGIN_003 | Login with invalid email |
| TC_LOGIN_004 | Login with empty email |
| TC_LOGIN_005 | Login with empty password |

---

## Automated Signup Test Scenarios

| Test Case ID | Scenario |
|--------------|-----------|
| TC_SIGNUP_001 | Signup with valid details |
| TC_SIGNUP_002 | Password mismatch validation |
| TC_SIGNUP_003 | Password policy validation |
| TC_SIGNUP_004 | Invalid email validation |
| TC_SIGNUP_005 | Terms and Conditions validation |

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd tichi-qa-automation
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / Mac

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Execute Login Automation

```bash
cd login
python test_login.py
```

---

## Execute Signup Automation

```bash
cd signup
python test_signup.py
```

---

## Expected Results

### Login

- Valid users should be able to log in successfully.
- Invalid credentials should display appropriate validation messages.
- Empty mandatory fields should not allow login.

### Signup

- Users should be able to register with valid details.
- Password validation rules should be enforced.
- Password and Confirm Password should match.
- Users should be redirected to the Verify Account page after successful signup.
- Verification email should be displayed correctly.
- Resend Verification option should be available.

---

## Sample Test Output

```text
Running Login Automation Tests

TC_LOGIN_001 PASSED
TC_LOGIN_002 PASSED
TC_LOGIN_003 PASSED
TC_LOGIN_004 PASSED
TC_LOGIN_005 PASSED

Execution Completed
```

---

## Assignment Deliverables

- Test Case Document
- Defect Report
- Selenium Automation Source Code
- Automation Execution Report

---

## Author

Abishek Durai

QA Intern Technical Assignment
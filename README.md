![Python](https://img.shields.io/badge/Python-3.9-blue?logo=python)
![pytest](https://img.shields.io/badge/pytest-8.1.1-blue?logo=pytest)
![Tests](https://img.shields.io/badge/tests-40%20passing-brightgreen)
![ISTQB](https://img.shields.io/badge/ISTQB-CTFL%20v4.0-orange)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

# QA Automation Portfolio — API Testing with Python & pytest

A professional API test automation framework built with Python and pytest, targeting the [ReqRes](https://reqres.in) REST API. This project demonstrates real-world QA engineering practices including test organization, fixtures, markers, parametrization, and HTML reporting.

---

## Tech Stack

| Tool          | Purpose                                |
| ------------- | -------------------------------------- |
| Python 3.9    | Core language                          |
| pytest        | Test framework                         |
| requests      | HTTP client for API calls              |
| pytest-html   | HTML report generation                 |
| python-dotenv | Secure environment variable management |

---

## Project Structure

## Project Structure

```
qa-automation-portfolio/
├── tests/
│   ├── conftest.py           # Shared fixtures (session scope)
│   └── api/
│       ├── test_users.py     # GET user endpoints
│       ├── test_crud.py      # POST, PUT, DELETE operations
│       ├── test_auth.py      # Login and Register endpoints
│       └── test_parametrize.py  # Parametrized test scenarios
├── utils/
│   └── api_client.py         # Centralized HTTP client with auth headers
├── reports/
│   └── report.html           # Auto-generated HTML test report
├── .env                      # API key (not committed to version control)
├── .gitignore
├── pytest.ini                # Marker registration
└── requirements.txt
```

---

## Setup

**1. Clone the repository**

```bash
git clone https://github.com/Maab-7/qa-automation-portfolio.git
cd qa-automation-portfolio
```

**2. Create and activate virtual environment**

```bash
python3 -m venv venv
source venv/bin/activate
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Configure environment variables**

Create a `.env` file in the project root:
REQRES_API_KEY=your_api_key_here

Get your free API key at [app.reqres.in/api-keys](https://app.reqres.in/api-keys).

---

## Running Tests

**Run all tests**

```bash
python -m pytest tests/ -v
```

**Run smoke tests only** (critical path)

```bash
python -m pytest tests/ -v -m smoke
```

**Run regression tests only** (full coverage)

```bash
python -m pytest tests/ -v -m regression
```

**Run a single test class**

```bash
python -m pytest tests/api/test_auth.py::TestLogin -v
```

**Run a single test method**

```bash
python -m pytest tests/api/test_auth.py::TestLogin::test_login_returns_200 -v
```

**Generate HTML report**

```bash
python -m pytest tests/ -v --html=reports/report.html --self-contained-html
```

---

## Test Coverage

| File                | Scope                             | Tests  |
| ------------------- | --------------------------------- | ------ |
| test_users.py       | GET /users, GET /users/{id}       | 5      |
| test_crud.py        | POST, PUT, DELETE /users          | 13     |
| test_auth.py        | POST /login, POST /register       | 9      |
| test_parametrize.py | Multi-scenario parametrized tests | 13     |
| **Total**           |                                   | **40** |

### Markers

- `smoke` — Core functionality, fast feedback. Run before every deployment.
- `regression` — Full suite, broader coverage. Run on scheduled builds.

---

## Key Concepts Demonstrated

- **Page Object pattern equivalent** — centralized `api_client.py` decouples HTTP logic from test logic
- **Session-scoped fixtures** — API calls made once per session, not once per test
- **Parametrization** — single test method covering multiple data scenarios
- **Negative testing** — explicit validation of error responses and edge cases
- **Secure credential management** — API keys loaded from `.env`, never committed to version control
- **Environment isolation** — virtual environment ensures reproducible test runs

---

## Author

**Marco Antonio Alfaro Bustillos**  
QA Engineer | Santa Cruz, Bolivia  
[LinkedIn](https://linkedin.com/in/marco-alfaro-bustillos) | [GitHub](https://github.com/Maab-7)

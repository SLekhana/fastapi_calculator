````markdown
# FastAPI Calculator Application

## Project Overview
This is a FastAPI-based web calculator application that supports basic arithmetic operations and is fully tested with unit, integration, and end-to-end tests. The project also implements logging and is set up with GitHub Actions for continuous integration (CI).

## Features
- **Arithmetic Operations:** Addition, Subtraction, Multiplication, Division (handles divide-by-zero errors gracefully)
- **Testing:** Unit tests for `operations.py`, Integration tests for API endpoints, End-to-End tests with Playwright
- **Logging:** Tracks operations and errors in `app.log`
- **CI/CD:** GitHub Actions workflow automatically runs tests and enforces 90% test coverage

## Installation
1. **Clone the repository**  
```bash
git clone https://github.com/YOUR_USERNAME/fastapi_calculator.git
cd fastapi_calculator
````

2. **Create and activate a virtual environment**

```bash
python3 -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
pip install playwright
playwright install
```

## Running the Application

Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

Open your browser and navigate to:

```
http://127.0.0.1:8000/docs
```

You will see the interactive API documentation (Swagger UI).

## Testing

* **Unit and Integration Tests:**

```bash
pytest -v
```

* **End-to-End Tests:** (ensure the FastAPI server is running)

```bash
pytest tests/test_e2e_playwright.py -v
```

* **Coverage:**

```bash
pytest --cov=app --cov-fail-under=90
```

## Logging

All operations and errors are logged in `app.log`. You can customize logging settings in `logging_config.py` if needed.

## GitHub Actions CI

The workflow is defined in `.github/workflows/python-app.yml`. It automatically sets up Python, installs dependencies, runs tests with coverage, and fails if coverage is below 90%.

## Screenshots

* **GitHub Actions successful workflow run:** *(Add screenshot here)*
* **Application running in browser:** *(Add screenshot here)*

## Folder Structure

```
fastapi_calculator/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── operations.py
│   └── logging_config.py
├── tests/
│   ├── test_main.py
│   ├── test_operations.py
│   └── test_e2e_playwright.py
├── .github/workflows/python-app.yml
├── requirements.txt
├── README.md
└── app.log
```

## Notes

* Ensure the server is running before running end-to-end tests.
* Use Python 3.10+ for best compatibility.
* Follow proper Git practices: commit frequently with descriptive messages.

## Author

Your Name / GitHub: [YOUR_USERNAME](https://github.com/SLekhana)

```


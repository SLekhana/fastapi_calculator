# tests/test_e2e_playwright.py
import pytest
from playwright.sync_api import sync_playwright

@pytest.mark.skip(reason="Requires FastAPI server to be running separately")
def test_homepage_loads():
    """
    End-to-end test for FastAPI docs page.
    Skipped during CI unless server is running.
    """
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        try:
            page.goto("http://127.0.0.1:8000/docs", timeout=5000)
            assert "Swagger UI" in page.title()
        finally:
            browser.close()


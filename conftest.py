
import pytest
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage



@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://authorized-partner.vercel.app/?branch=demo/login")

        # page.goto("https://authorized-partner.vercel.app/login")
    
        yield page
        browser.close()
        

@pytest.fixture
def login_in_page(page):
    login = LoginPage(page)
    login.login("amritbhusal806@gmail.com", "Nepal@123")
    return page

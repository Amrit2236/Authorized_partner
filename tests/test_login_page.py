


from pages.login_page import LoginPage
def test_valid_login(page):
    login = LoginPage(page)

    login.navigate()
    login.login("amritbhusal806@gmail.com", "Nepal@123")
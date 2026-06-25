

from pages.sign_up import SignupPage
def test_signup(page):
    signup = SignupPage(page)
    signup.navigate()
    signup.signup("icon", "module")

    signup.enter_details("Kamana", "Bhandari", "ranju@gmail.com", "9847518232", "Nepal@123")
    


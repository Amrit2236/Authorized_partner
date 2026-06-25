

from pages.user_payment import UserPaymentPage

def test_user_payment(login_in_page):
    user_payment = UserPaymentPage(login_in_page)
    user_payment.user_payment("icon", "module")
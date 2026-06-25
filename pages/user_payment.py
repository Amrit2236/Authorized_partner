








from conftest import page
from playwright.sync_api import expect

class UserPaymentPage :
    def __init__(self, page):
        self.page = page
        
    def user_payment(self, icon, module):
        self.page.set_viewport_size({"width": 1366, "height": 768})
        self.page.get_by_role("heading",name="Amrit Bhusal",exact=True).click()
        self.page.wait_for_timeout(1000)

# edit Payment Details

        self.page.get_by_text("payment").click()
        self.page.wait_for_timeout(1000)
        section = self.page.locator("text=Payment Details").locator("..")
        section.get_by_role("button", name="Edit").click()
        self.page.wait_for_timeout(3000) 
        self.page.locator("input[name='account_holder_name']").fill("Asmita")
        self.page.locator("input[name='account_number']").fill("9847345166")
        self.page.locator("input[name='bank_name']").fill("Nabil Bank")
        self.page.locator("input[name='branch_name']").fill("Koteshwor")
        self.page.get_by_text("Save").click()



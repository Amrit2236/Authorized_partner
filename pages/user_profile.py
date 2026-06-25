





from conftest import page
from playwright.sync_api import expect

class UserProfilePage :
    def __init__(self, page):
        self.page = page
        
    def user_profile(self, icon, module):
        self.page.set_viewport_size({"width": 1366, "height": 768})
        self.page.get_by_role("heading",name="Amrit Bhusal",exact=True).click()
        self.page.wait_for_timeout(1000)

# edit imported product

        section = self.page.locator("text=Personal Information").locator("..")
        section.get_by_role("button", name="Edit").click()
        self.page.wait_for_timeout(3000) 
        self.page.locator("input[name='firstName']").fill("Kamana")
        self.page.locator("input[name='lastName']").fill("Khanal")
        self.page.locator("input[name='phoneNumber']").fill("9847518332")
        self.page.get_by_text("Save").click()

# Agency Details
        section = self.page.locator("text=Agency Details").locator("..")
        section.get_by_role("button", name="Edit").click()
        self.page.wait_for_timeout(3000) 
        self.page.locator("input[name='agency_name']").fill("Mega")
        self.page.locator("input[name='role_in_agency']").fill("Bank")
        self.page.locator("input[name='agency_email']").fill("mega@123")
        self.page.locator("input[name='agency_website']").fill("megabank.com")
        self.page.locator("input[name='agency_address']").fill("Kathmandu,Nepal")
        self.page.get_by_role("combobox").click()
        self.page.locator("text='United States of America'").first.click(force=True)
        self.page.get_by_text("Save").click()
        self.page.wait_for_timeout(3000)
# Lead Form URL
        section = self.page.locator("text=Lead Form URL").locator("..")
        section.get_by_role("button", name="Edit").click()
        self.page.get_by_text("Save").click()
        self.page.wait_for_timeout(3000)



        

        # role="combobox"
        # self.page.locator("select[name='status']").select_option("United States of America")
        self.page.wait_for_timeout(1000)


        # self.page.locator("input[name='role_in_agency']").fill("Bank")
        # self.page.locator("input[name='role_in_agency']").fill("Bank")

        # self.page.locator("input[name='phoneNumber']").fill("9847518332")
        # self.page.get_by_text("Save").click()

       


class SignupPage:
    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto("https://authorized-partner.vercel.app/?branch=demo/login")

        
    def signup(self, icon, module):
        self.page.locator("a:has-text('Login')").click()
        self.page.get_by_role("link", name="Sign Up").click()

        checkbox = self.page.get_by_role("checkbox")
        checkbox.check()
        self.page.get_by_role("button", name="Continue").click()
        self.page.wait_for_timeout(3000)

    # Provide your personal details.
    def enter_details(self, first_name, last_name, email, phone, password):
       
        self.page.get_by_placeholder("Enter Your First Name").fill("Amrit")
        self.page.get_by_placeholder("Enter Your Last Name").fill("Bhusal")
        self.page.get_by_placeholder("Enter Your Email Address").fill("amritbhusal806@gmail.com")
        self.page.get_by_placeholder("00-00000000").fill("9861997475")
        self.page.get_by_placeholder("******************").nth(0).fill("Nepal@123")
        self.page.get_by_placeholder("******************").nth(1).fill("Nepal@123")
        self.page.get_by_role("button", name="Next").click()
        self.page.wait_for_timeout(3000)


    # Email Verification code





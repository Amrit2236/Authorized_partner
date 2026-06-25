class LoginPage:
    def __init__(self, page):
        self.page = page

        # Locators
        self.email_input = page.get_by_placeholder("Enter your email")
        self.password_input = self.page.locator('input[type="password"]')
        self.signin_button = page.get_by_role("button", name="Log In")

    def navigate(self):
        self.page.goto("https://authorized-partner.vercel.app/?branch=demo/login")

    def login(self, email, password):
        self.page.locator("a:has-text('Login')").click()

        self.email_input.fill("amritbhusal806@gmail.com")
        self.password_input.fill("Nepal@123")
        self.signin_button.click()
        self.page.wait_for_timeout(3000)

        
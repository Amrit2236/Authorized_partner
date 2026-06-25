

from pages.user_profile import UserProfilePage

def test_user_profile(login_in_page):
    user_profile = UserProfilePage(login_in_page)
    user_profile.user_profile("icon", "module")




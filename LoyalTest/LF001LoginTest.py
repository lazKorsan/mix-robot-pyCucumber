# LF001LoginTest
# C:\Users\user\PycharmProjects\exantring\LoyalTest\LF001LoginTest.py

from pages.loyal_friend_pages import LoyalFriendCarePage
from properties import test_data

def test_login_with_valid_data():
    # LoyalFriendCarePage nesnesini oluştur
    lfPage=LoyalFriendCarePage()

    # WebDriver'ı başlat
    lfPage.set_up()

    # Ana sayfaya git
    lfPage.navigate_to_home_page(test_data.ly_URL)

    # geçerli bilgilerle siteye giriş yap
    lfPage.login_method_with_valid_data(lfPage.driver, test_data.ly_mail, test_data.ly_password)



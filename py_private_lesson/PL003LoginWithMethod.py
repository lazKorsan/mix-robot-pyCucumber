
from pages.prvateLessonsPage import PrivateLessonsPage
from properties import test_data




def test_login_with_method():
    # PrivateLessonsPage nesnesini oluştur
    pvPage=PrivateLessonsPage()

    # WebDriver'ı başlat
    pvPage.set_up()

    # Ana sayfaya git
    pvPage.navigate_to_homepage(test_data.pv_lessons_url)


    # geçerli bilgilerle siteye giriş yap
    pvPage.loginMethod(pvPage.driver, test_data.pv_lessons_userName, test_data.pv_lessons_password)

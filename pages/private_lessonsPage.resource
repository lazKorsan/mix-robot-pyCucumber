from selenium import webdriver
from utils.click_utils import click_utils
from utils.sendkey_utils import sendKey_utils

# XPath'ler sınıf dışında veya içinde tanımlanabilir
GIRIS_YAP_BUTTON = '//*[@class="btn btn-success fw-bold shadow-sm px-4"]'
USERNAME_BOX = '(//input[@class="form-control border-start-0 rounded-end-3"])[1]'
PASSWORD_BOX = '(//input[@class="form-control border-start-0 rounded-end-3"])[2]'
SUBMIT_BUTTON = '//button[@class="btn btn-login w-100"]'

class PrivateLessonsLibrary:
    """
    Robot Framework için özel Private Lessons kütüphanesi.
    """
    ROBOT_LIBRARY_SCOPE = 'SUITE'

    def __init__(self):
        self.driver = None

    def set_up_browser(self):
        """Tarayıcıyı başlatır ve maximize eder."""
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        return self.driver

    def navigate_to_homepage(self, url):
        """Belirtilen URL'e gider."""
        if self.driver:
            self.driver.get(url)
        else:
            raise Exception("Driver başlatılmadı! Lütfen önce 'Set Up Browser' keywordünü kullanın.")

    def login_with_credentials(self, username, password):
        """
        Kullanıcı adı ve şifre ile giriş yapar.
        Robot Framework içinde 'Login With Credentials' olarak çağrılır.
        """
        # Giriş yap butonuna tıkla
        click_utils(self.driver, GIRIS_YAP_BUTTON)

        # Kullanıcı adını gönder
        sendKey_utils(self.driver, USERNAME_BOX, username)

        # Şifreyi gönder
        sendKey_utils(self.driver, PASSWORD_BOX, password)

        # Submit butonuna tıkla
        click_utils(self.driver, SUBMIT_BUTTON)

    def close_browser_session(self):
        """Tarayıcıyı kapatır."""
        if self.driver:
            self.driver.quit()
# Driver.py
# C:\Users\user\PycharmProjects\immigrate123\driver.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.safari.options import Options as SafariOptions
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException, TimeoutException
import time
import os
from datetime import datetime
import logging
from typing import Optional, Dict, Any

class Colors:
    """Renkli konsol çıktıları için"""
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    GRAY = '\033[90m'

class DriverConfig:
    """Driver konfigürasyon ayarları"""
    # Varsayılan ayarlar
    DEFAULT_BROWSER = "chrome"
    DEFAULT_TIMEOUT = 30
    DEFAULT_WINDOW_SIZE = "1920x1080"
    DEFAULT_HEADLESS = False
    DEFAULT_DOWNLOAD_DIR = os.path.join(os.getcwd(), "downloads")
    
    # Browser path'leri (gerektiğinde düzenleyin)
    CHROME_DRIVER_PATH = None  # chromedriver otomatik bulunacak
    FIREFOX_DRIVER_PATH = None  # geckodriver otomatik bulunacak
    EDGE_DRIVER_PATH = None  # msedgedriver otomatik bulunacak

class DriverManager:
    """
    Gelişmiş WebDriver yönetimi ve konfigürasyonu
    """
    
    @staticmethod
    def setup_driver(
        browser: str = "chrome",
        headless: bool = False,
        window_size: str = "1920x1080",
        timeout: int = 30,
        download_dir: Optional[str] = None,
        proxy: Optional[str] = None,
        user_agent: Optional[str] = None,
        disable_notifications: bool = True,
        disable_images: bool = False,
        incognito: bool = False,
        experimental_options: Optional[Dict[str, Any]] = None,
        remote_url: Optional[str] = None,
        capabilities: Optional[Dict[str, Any]] = None
    ) -> webdriver.Remote:
        """
        WebDriver'ı yapılandırır ve başlatır.
        
        Args:
            browser: Tarayıcı tipi (chrome, firefox, edge, safari)
            headless: Headless mod
            window_size: Pencere boyutu (örn: "1920x1080")
            timeout: Varsayılan timeout (saniye)
            download_dir: İndirme dizini
            proxy: Proxy adresi (örn: "http://proxy:8080")
            user_agent: Özel User-Agent
            disable_notifications: Bildirimleri engelle
            disable_images: Resimleri engelle
            incognito: Gizli mod
            experimental_options: Deneysel seçenekler
            remote_url: Remote WebDriver URL (Selenium Grid için)
            capabilities: Özel capabilities
        
        Returns:
            WebDriver instance
        """
        print(f"{Colors.BLUE}{'='*60}{Colors.ENDC}")
        print(f"{Colors.BOLD}🚀 WEBDRIVER BAŞLATILIYOR...{Colors.ENDC}")
        print(f"{Colors.GRAY}Tarayıcı: {browser.upper()}")
        print(f"Headless: {'✅' if headless else '❌'}")
        print(f"Window Size: {window_size}")
        print(f"Timeout: {timeout}s{Colors.ENDC}")
        
        driver = None
        
        try:
            if remote_url:
                driver = DriverManager._setup_remote_driver(
                    remote_url, browser, capabilities
                )
            elif browser.lower() == "chrome":
                driver = DriverManager._setup_chrome_driver(
                    headless, window_size, download_dir, proxy, 
                    user_agent, disable_notifications, disable_images,
                    incognito, experimental_options
                )
            elif browser.lower() == "firefox":
                driver = DriverManager._setup_firefox_driver(
                    headless, window_size, download_dir, proxy,
                    user_agent, disable_notifications, disable_images,
                    incognito, experimental_options
                )
            elif browser.lower() == "edge":
                driver = DriverManager._setup_edge_driver(
                    headless, window_size, download_dir, proxy,
                    user_agent, disable_notifications, disable_images,
                    incognito, experimental_options
                )
            elif browser.lower() == "safari":
                driver = DriverManager._setup_safari_driver()
            else:
                raise ValueError(f"Desteklenmeyen tarayıcı: {browser}")
            
            # Timeout ayarları
            driver.implicitly_wait(timeout)
            driver.set_page_load_timeout(timeout)
            driver.set_script_timeout(timeout)
            
            # Pencereyi maximize et (headless değilse)
            if not headless:
                width, height = map(int, window_size.split('x'))
                driver.set_window_size(width, height)
                print(f"{Colors.GREEN}✅ Pencere boyutu ayarlandı: {window_size}{Colors.ENDC}")
            
            # Başarı mesajı
            print(f"{Colors.GREEN}✅ {browser.upper()} WebDriver başarıyla başlatıldı!{Colors.ENDC}")
            print(f"{Colors.BLUE}{'='*60}{Colors.ENDC}")
            
            return driver
            
        except Exception as e:
            print(f"{Colors.RED}❌ WebDriver başlatılamadı: {str(e)}{Colors.ENDC}")
            if driver:
                driver.quit()
            raise
    
    @staticmethod
    def _setup_chrome_driver(
        headless: bool,
        window_size: str,
        download_dir: Optional[str],
        proxy: Optional[str],
        user_agent: Optional[str],
        disable_notifications: bool,
        disable_images: bool,
        incognito: bool,
        experimental_options: Optional[Dict[str, Any]]
    ) -> webdriver.Chrome:
        """Chrome driver konfigürasyonu"""
        options = Options()
        
        # Temel ayarlar
        if headless:
            options.add_argument("--headless=new")  # Yeni headless mod
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
        
        if incognito:
            options.add_argument("--incognito")
        
        # Performans ayarları
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-software-rasterizer")
        options.add_argument("--disable-logging")
        options.add_argument("--log-level=3")
        
        # Güvenlik ve gizlilik
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        
        # Proxy
        if proxy:
            options.add_argument(f'--proxy-server={proxy}')
        
        # User-Agent
        if user_agent:
            options.add_argument(f'--user-agent={user_agent}')
        else:
            # Gerçekçi User-Agent
            options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
        
        # Bildirimleri engelle
        if disable_notifications:
            options.add_argument("--disable-notifications")
            options.add_experimental_option("prefs", {
                "profile.default_content_setting_values.notifications": 2
            })
        
        # İndirme dizini
        if download_dir:
            os.makedirs(download_dir, exist_ok=True)
            options.add_experimental_option("prefs", {
                "download.default_directory": download_dir,
                "download.prompt_for_download": False,
                "download.directory_upgrade": True,
                "safebrowsing.enabled": True
            })
        
        # Resimleri engelle
        if disable_images:
            options.add_experimental_option("prefs", {
                "profile.managed_default_content_settings.images": 2
            })
        
        # Deneysel seçenekler
        if experimental_options:
            for key, value in experimental_options.items():
                options.add_experimental_option(key, value)
        
        # Service ayarları
        service = Service(executable_path=DriverConfig.CHROME_DRIVER_PATH)
        
        # Driver oluştur
        driver = webdriver.Chrome(service=service, options=options)
        
        # Anti-bot bypass
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        
        return driver
    
    @staticmethod
    def _setup_firefox_driver(
        headless: bool,
        window_size: str,
        download_dir: Optional[str],
        proxy: Optional[str],
        user_agent: Optional[str],
        disable_notifications: bool,
        disable_images: bool,
        incognito: bool,
        experimental_options: Optional[Dict[str, Any]]
    ) -> webdriver.Firefox:
        """Firefox driver konfigürasyonu"""
        options = FirefoxOptions()
        
        if headless:
            options.add_argument("--headless")
        
        if incognito:
            options.add_argument("--private")
        
        # Proxy
        if proxy:
            options.set_preference("network.proxy.type", 1)
            options.set_preference("network.proxy.http", proxy.split(':')[0])
            options.set_preference("network.proxy.http_port", int(proxy.split(':')[1]))
        
        # User-Agent
        if user_agent:
            options.set_preference("general.useragent.override", user_agent)
        
        # İndirme dizini
        if download_dir:
            os.makedirs(download_dir, exist_ok=True)
            options.set_preference("browser.download.folderList", 2)
            options.set_preference("browser.download.dir", download_dir)
            options.set_preference("browser.download.useDownloadDir", True)
            options.set_preference("browser.helperApps.neverAsk.saveToDisk", 
                                  "application/pdf, application/octet-stream")
        
        # Bildirimler
        if disable_notifications:
            options.set_preference("dom.webnotifications.enabled", False)
        
        # Service ayarları
        service = Service(executable_path=DriverConfig.FIREFOX_DRIVER_PATH)
        
        return webdriver.Firefox(service=service, options=options)
    
    @staticmethod
    def _setup_edge_driver(
        headless: bool,
        window_size: str,
        download_dir: Optional[str],
        proxy: Optional[str],
        user_agent: Optional[str],
        disable_notifications: bool,
        disable_images: bool,
        incognito: bool,
        experimental_options: Optional[Dict[str, Any]]
    ) -> webdriver.Edge:
        """Edge driver konfigürasyonu"""
        options = EdgeOptions()
        
        if headless:
            options.add_argument("--headless")
        
        if incognito:
            options.add_argument("--inprivate")
        
        if user_agent:
            options.add_argument(f'--user-agent={user_agent}')
        
        # Service ayarları
        service = Service(executable_path=DriverConfig.EDGE_DRIVER_PATH)
        
        return webdriver.Edge(service=service, options=options)
    
    @staticmethod
    def _setup_safari_driver() -> webdriver.Safari:
        """Safari driver konfigürasyonu"""
        # Safari için özel ayarlar gerekmez
        return webdriver.Safari()
    
    @staticmethod
    def _setup_remote_driver(
        remote_url: str,
        browser: str,
        capabilities: Optional[Dict[str, Any]]
    ) -> webdriver.Remote:
        """Remote WebDriver (Selenium Grid) konfigürasyonu"""
        if capabilities is None:
            if browser == "chrome":
                capabilities = DesiredCapabilities.CHROME.copy()
            elif browser == "firefox":
                capabilities = DesiredCapabilities.FIREFOX.copy()
            elif browser == "edge":
                capabilities = DesiredCapabilities.EDGE.copy()
            else:
                capabilities = DesiredCapabilities.CHROME.copy()
        
        return webdriver.Remote(
            command_executor=remote_url,
            desired_capabilities=capabilities
        )
    
    @staticmethod
    def take_screenshot(driver: webdriver.Remote, filename: Optional[str] = None) -> str:
        """
        Ekran görüntüsü alır
        
        Args:
            driver: WebDriver instance
            filename: Kaydedilecek dosya adı (None ise otomatik oluşturulur)
        
        Returns:
            Screenshot dosya yolu
        """
        try:
            if filename is None:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"screenshot_{timestamp}.png"
            
            # Screenshots klasörü oluştur
            screenshot_dir = os.path.join(os.getcwd(), "screenshots")
            os.makedirs(screenshot_dir, exist_ok=True)
            
            filepath = os.path.join(screenshot_dir, filename)
            driver.save_screenshot(filepath)
            
            print(f"{Colors.CYAN}📸 Screenshot kaydedildi: {filepath}{Colors.ENDC}")
            return filepath
            
        except Exception as e:
            print(f"{Colors.YELLOW}⚠️  Screenshot alınamadı: {str(e)}{Colors.ENDC}")
            return ""

class BrowserUtils:
    """Tarayıcı yardımcı metodları"""
    
    @staticmethod
    def wait_for_page_load(driver: webdriver.Remote, timeout: int = 30) -> bool:
        """Sayfanın tamamen yüklenmesini bekler"""
        try:
            WebDriverWait(driver, timeout).until(
                lambda d: d.execute_script("return document.readyState") == "complete"
            )
            return True
        except TimeoutException:
            print(f"{Colors.YELLOW}⚠️  Sayfa {timeout}s içinde yüklenemedi{Colors.ENDC}")
            return False
    
    @staticmethod
    def switch_to_new_tab(driver: webdriver.Remote, close_old: bool = False) -> bool:
        """Yeni açılan tab'a geçiş yapar"""
        try:
            original_window = driver.current_window_handle
            windows = driver.window_handles
            
            if len(windows) > 1:
                for window in windows:
                    if window != original_window:
                        driver.switch_to.window(window)
                        if close_old:
                            driver.switch_to.window(original_window)
                            driver.close()
                            driver.switch_to.window(window)
                        print(f"{Colors.GREEN}✅ Yeni tab'a geçildi{Colors.ENDC}")
                        return True
            return False
        except Exception as e:
            print(f"{Colors.RED}❌ Tab değiştirilemedi: {str(e)}{Colors.ENDC}")
            return False
    
    @staticmethod
    def scroll_to_element(driver: webdriver.Remote, element) -> bool:
        """Elemente scroll yapar"""
        try:
            driver.execute_script(
                "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
                element
            )
            time.sleep(0.5)
            return True
        except Exception as e:
            print(f"{Colors.YELLOW}⚠️  Scroll başarısız: {str(e)}{Colors.ENDC}")
            return False
    
    @staticmethod
    def highlight_element(driver: webdriver.Remote, element, color: str = "red", duration: float = 2) -> bool:
        """Elementi vurgular"""
        try:
            original_style = element.get_attribute("style")
            driver.execute_script(
                "arguments[0].setAttribute('style', arguments[1]);",
                element,
                f"{original_style}; border: 3px solid {color}; background-color: yellow;"
            )
            time.sleep(duration)
            driver.execute_script(
                "arguments[0].setAttribute('style', arguments[1]);",
                element,
                original_style
            )
            return True
        except Exception as e:
            print(f"{Colors.YELLOW}⚠️  Highlight başarısız: {str(e)}{Colors.ENDC}")
            return False

# Kolay erişim için kısayollar
def create_driver(
    browser: str = "chrome",
    headless: bool = False,
    window_size: str = "1920x1080",
    timeout: int = 30,
    **kwargs
) -> webdriver.Remote:
    """WebDriver oluşturmak için kısayol fonksiyonu"""
    return DriverManager.setup_driver(
        browser=browser,
        headless=headless,
        window_size=window_size,
        timeout=timeout,
        **kwargs
    )

def quick_chrome(headless: bool = False) -> webdriver.Chrome:
    """Hızlı Chrome driver oluşturma"""
    return create_driver("chrome", headless=headless)

def quick_firefox(headless: bool = False) -> webdriver.Firefox:
    """Hızlı Firefox driver oluşturma"""
    return create_driver("firefox", headless=headless)

def close_driver(driver: webdriver.Remote):
    """Driver'ı kapatır"""
    if driver:
        try:
            driver.quit()
            print(f"{Colors.GREEN}✅ WebDriver başarıyla kapatıldı{Colors.ENDC}")
        except Exception as e:
            print(f"{Colors.YELLOW}⚠️  Driver kapatılırken hata: {str(e)}{Colors.ENDC}")

# Örnek kullanım
if __name__ == "__main__":
    # Basit kullanım
    driver = create_driver()
    
    # Gelişmiş kullanım
    advanced_driver = create_driver(
        browser="chrome",
        headless=False,
        window_size="1366x768",
        timeout=20,
        incognito=True,
        disable_notifications=True,
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    )
    
    # Test işlemleri...
    
    # Driver'ı kapat
    close_driver(driver)
    close_driver(advanced_driver)
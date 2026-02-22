import logging
import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

from properties import test_data
from utils.click_utils import click_utils
from utils.sendkey_utils import sendKey_utils

logger = logging.getLogger(__name__)


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.new_webinar_button = (By.XPATH, '//a[contains(@class, "btn-primary") and contains(@href, "new")]')
    # adım1: Kullanici login sayfasina gider
    def navigate_to_login(self, url):
        logger.info(f"--- SAYFAYA GİDİLİYOR: {url} ---")
        self.driver.get(url)
        logger.info("--- LOGIN SAYFASINA BAŞARIYLA ULAŞILDI ---")

    def login_method(self, email, password):
        # emailBox
        # adim2 : Kullanici gecerli mail adresini girer
        emailBox_ID = '//input[@id="email"]'
        sendKey_utils(self.driver, emailBox_ID, test_data.login_mail)
        logging.info("Entered email address")

        # adım3 : Kullanici gecerli sifre girer
        # passwordBox
        passwordBox_ID = '//input[@id="password"]'
        sendKey_utils(self.driver, passwordBox_ID, test_data.instructor_password)
        logging.info("Entered password")

        # adım4 : Kullanici login butonuna tiklar
        # loginSubmitButton
        loginSubmitButton_Class = '//button[@class="btn btn-primary btn-block mt-20"]'
        click_utils(self.driver, loginSubmitButton_Class)

    def navigate_to_new_courses(self):

        # adım5: Kullanıcı dashboard uzerine hoover yapar
        # dashboard işlemleri
        DASHBOARD_XPATH = '//*[@id="panel-sidebar-scroll"]'

        # self.find_element yerine self.driver.find_element kullanmalısınız
        dasbord_menu_Button = self.driver.find_element(By.XPATH, DASHBOARD_XPATH)

        # ActionChains içine 'self' değil 'self.driver' almalı
        actions = ActionChains(self.driver)
        actions.move_to_element(dasbord_menu_Button).perform()

        # execute_script metodu da driver üzerinden çağrılmalı
        self.driver.execute_script("arguments[0].style.backgroundColor = 'green';", dasbord_menu_Button)

        self.driver.execute_script("""
            var dot = document.createElement('div');
            dot.style.width = '10px';
            dot.style.height = '10px';
            dot.style.backgroundColor = 'red';
            dot.style.borderRadius = '50%';
            dot.style.position = 'absolute';
            dot.style.top = (arguments[0].offsetTop + arguments[0].offsetHeight / 2 - 5) + 'px';
            dot.style.left = (arguments[0].offsetLeft + arguments[0].offsetWidth / 2 - 5) + 'px';
            document.body.appendChild(dot);
        """, dasbord_menu_Button)
        time.sleep(2)

        # adım6: Kullanıcı courses butona tıklar
        courses_button_Xpath ='(//*[@class="font-14 text-dark-blue font-weight-500"])[2]'
        click_utils(
            self.driver,
            courses_button_Xpath
        )

        # adım7: Kullanıcı new webinar butona tıklar
        new_webinar_button_Xpath='(//*[@href="/panel/webinars/new"])[3]'
        click_utils(
            self.driver,
            new_webinar_button_Xpath
        )

    def step1(
            self,
            title="mathematics",
            description="This is a mathematics course.",
            thumbnail_path="/store/2014/math1.jpg",
            cover_image_path="/store/2014/3d_difdenk.png",
            note_text="Kurs başlangıç tarihi ayın 24 dunde olacak"
    ):
        # adım8: Kullanıcı course cinsini seçer
        COURSTTPE_XPATH = '//select[@class="custom-select "]'
        courseTypeButton = self.driver.find_element(By.XPATH, COURSTTPE_XPATH)
        self.driver.execute_script("arguments[0].style.border='3px solid red'", courseTypeButton)
        courseTypeButton.click()
        print("Course type dropdown tıklandı.")

        SECOND_OPTION_XPATH = '//select[@class="custom-select "]/option[2]'
        secondOption = self.driver.find_element(By.XPATH, SECOND_OPTION_XPATH)
        self.driver.execute_script("arguments[0].style.backgroundColor = 'yellow'", secondOption)
        secondOption.click()
        print("İkinci seçenek seçildi.")

        # adım9 : Yeni kurs başlığı
        TITLEBOX_XPATH = '(//input[@class="form-control "])[1]'
        titleBox = self.driver.find_element(By.XPATH, TITLEBOX_XPATH)
        self.driver.execute_script("arguments[0].style.border='3px solid blue'", titleBox)
        titleBox.clear()
        titleBox.send_keys(title)
        print(f"Yeni kurs başlığı girildi: {title}")

        # adım10 : Kurs Açıklaması
        CEODESCRIPTION_XPATH = '//input[@name="seo_description"]'
        ceoDescriptionBox = self.driver.find_element(By.XPATH, CEODESCRIPTION_XPATH)
        self.driver.execute_script("arguments[0].style.border='3px solid green'", ceoDescriptionBox)
        ceoDescriptionBox.clear()
        ceoDescriptionBox.send_keys(description)
        print("SEO Description dolduruldu.")

        # adım11 : Thumbnail
        THUMBNAIL_XPATH = '//input[@id="thumbnail"]'
        thumbNailBox = self.driver.find_element(By.XPATH, THUMBNAIL_XPATH)
        self.driver.execute_script("arguments[0].style.border='3px solid orange'", thumbNailBox)
        thumbNailBox.send_keys(thumbnail_path)
        print("Thumbnail yüklendi.")

        # adım12 : Cover image
        COVERIMAGE_XPATH = '//input[@id="cover_image"]'
        coverImageBox = self.driver.find_element(By.XPATH, COVERIMAGE_XPATH)
        self.driver.execute_script("arguments[0].style.border='3px solid purple'", coverImageBox)
        coverImageBox.send_keys(cover_image_path)
        print("Cover image yüklendi.")

        # adım13 : Not alanı
        NOTE_EDIBTALE_XPATH = '//*[@class="note-editable card-block"]'
        noteEditableArea = self.driver.find_element(By.XPATH, NOTE_EDIBTALE_XPATH)
        self.driver.execute_script("arguments[0].style.border='3px solid pink'", noteEditableArea)
        noteEditableArea.click()
        noteEditableArea.clear()
        noteEditableArea.send_keys(note_text)
        print("Not alanı dolduruldu.")

        # adım14 : Next Step
        NEXT_STEP_BUTTON_XPATH = '//button[@id="getNextStep"]'
        nextStepButton = self.driver.find_element(By.XPATH, NEXT_STEP_BUTTON_XPATH)
        self.driver.execute_script("arguments[0].style.border='3px solid cyan'", nextStepButton)
        nextStepButton.click()
        print("Next step butonuna tıklandı.")

        # adım15 : Sayfa yüklenme beklemesi
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )

        # adım16–18 : URL & Webinar ID
        currentUrl = self.driver.current_url
        print("Yeni sayfanın URL'i:", currentUrl)

        webinar_id = currentUrl.split('/')[5]
        print("Webinar ID:", webinar_id)

        self.saved_webinar_id = webinar_id
        print(f"Kayıtlı Webinar ID: {self.saved_webinar_id}")

    # step2 başı
    def step2(self, capacity="50", duration="45", tags="math", category_value="956"):
        """
        Webinar oluşturma sürecindeki Step 2 alanlarını doldurur ve Step 3'e geçişi doğrular.
        """
        print("--- Step 2 İşlemleri Başladı ---")

        # adım19: Kullanıcı course kayıt olabilecek ogrenci sayısını belirler
        # 1. Capacity Box
        capacity_xpath = '//input[@name="capacity"]'
        capacity_box = self.driver.find_element(By.XPATH, capacity_xpath)
        self.driver.execute_script("arguments[0].style.border='3px solid green'", capacity_box)
        capacity_box.clear()
        capacity_box.send_keys(capacity)
        print(f"Capacity: {capacity} olarak girildi.")

        # 2. Duration Box (Özel JS korumalı yapı)
        try:
            # adım20: Kullanıcı ders saati suresini girer (--> Hocam burada inatçı box var aşağıdaki yontemler olmazsa giriş olmuyor
            duration_xpath = '//input[@name="duration"]'
            duration_box = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.XPATH, duration_xpath))
            )
            self.driver.execute_script("arguments[0].scrollIntoView(true);", duration_box)
            self.driver.execute_script("arguments[0].style.border='3px solid red'", duration_box)

            # Standart giriş dene, olmazsa JS ile zorla
            duration_box.clear()
            duration_box.send_keys(duration)

            if not duration_box.get_attribute('value'):
                self.driver.execute_script(f"arguments[0].value = '{duration}';", duration_box)
                self.driver.execute_script("arguments[0].dispatchEvent(new Event('change', { bubbles: true }));",
                                      duration_box)
            print(f"Duration: {duration} olarak girildi.")
        except Exception as e:
            print(f"Duration box doldurulurken hata: {e}")

        # adım21: Kullanıcı uzaktan destek alanlarını seçer
        # 3. Switch/Radio Butonları (Support, Certificate, Downloadable)
        switches = self.driver.find_elements(By.XPATH, '//*[@class="custom-control custom-switch"]')
        for i, switch in enumerate(switches[:3]):  # İlk 3 switch'i tıkla
            self.driver.execute_script("arguments[0].click();", switch)
            print(f"Switch {i + 1} aktif edildi.")
        # adım22: Kullanıcı etiketi girer
        # 4. Tags Box
        tags_xpath = '//input[@placeholder="Type tag name and press enter (Max : 5)"]'
        tags_box = self.driver.find_element(By.XPATH, tags_xpath)
        tags_box.send_keys(tags)
        print(f"Etiket: {tags} eklendi.")

        # adım23: Kullanıcı kategoriyi seçer
        # 5. Category Dropdown
        category_xpath = '//select[@id="categories"]'
        category_element = self.driver.find_element(By.XPATH, category_xpath)
        select = Select(category_element)
        select.select_by_value(category_value)
        print(f"Kategori ID {category_value} seçildi.")

        # adım24: Kullanıcı Next Step butonuna tıklar
        # 6. Next Step ve Doğrulama
        next_step_btn = self.driver.find_element(By.ID, "getNextStep")
        next_step_btn.click()
        print("Next Step butonuna tıklandı. URL doğrulanıyor...")

        # adım24: Kullanıcı step3 icin succes rapor cıktısı hazırlar
        WebDriverWait(self.driver, 10).until(EC.url_contains("step/3"))
        if "step/3" in self.driver.current_url:
            print("------------------------------------------")
            print("BAŞARILI: Step 2 tamamlandı, Step 3'e geçildi.")
            print("------------------------------------------")
            return True
        else:
            print("HATA: Step 3'e geçilemedi!")
            return False

        # step3 başı

    def step3(self, access_days="10", price="0"):
        """
        Step 3: Pricing & Subscription ayarlarını yapar ve Step 4'e geçişi doğrular.
        """
        print("\n--- Step 3 (Pricing) İşlemleri Başladı ---")

        try:
            # adım25: Kullancı subscription secenegini işaretler
            # 1. Subscription Switch (Label üzerinden tıklama)
            SUB_LABEL_XPATH = '//label[@for="subscribeSwitch"]'
            sub_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, SUB_LABEL_XPATH))
            )
            # Elementi ortala ve border ekle
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", sub_button)
            self.driver.execute_script("arguments[0].style.border='3px solid purple'", sub_button)
            time.sleep(1)

            # JS Tıklaması (En güvenli yöntem)
            self.driver.execute_script("arguments[0].click();", sub_button)
            print("✅ Subscription butonu tıklandı.")

            # adım25: Kullanıcı course bitiminde videolara erisim gununu belirler
            # 2. Access Days (Erişim Gün Sayısı)
            period_days_box = self.driver.find_element(By.NAME, "access_days")
            self.driver.execute_script("arguments[0].style.border='3px solid green'", period_days_box)
            period_days_box.clear()
            period_days_box.send_keys(access_days)
            print(f"✅ Erişim günü: {access_days}")

            # adım26: Kullanıcı kurs fiyatını belirler (--> hocam price sıfır olmak zorunda)
            # 3. Price (Fiyat)
            price_box = self.driver.find_element(By.NAME, "price")
            self.driver.execute_script("arguments[0].style.border='3px solid red'", price_box)
            price_box.clear()
            price_box.send_keys(price)
            print(f"✅ Fiyat: {price}")

            # adım27: Kullanıcı Next Step butonuna tıklar
            # 4. Next Step Butonu
            next_btn = self.driver.find_element(By.ID, "getNextStep")
            self.driver.execute_script("arguments[0].style.border='3px solid yellow'", next_btn)
            next_btn.click()
            print("🚀 Next Step butonuna tıklandı.")

            # adım28: step3 icin basarı mesajı hazırlar ve consola yazdırırır

            # 5. Başarı Doğrulaması (URL Kontrolü)
            WebDriverWait(self.driver, 15).until(EC.url_contains("step/4"))
            if "step/4" in self.driver.current_url:
                print("=" * 50)
                print("⭐ STEP 3 BAŞARIYLA TAMAMLANDI, STEP 4'E GEÇİLDİ.")
                print("=" * 50 + "\n")
                return True

        except Exception as e:
            print(f"❌ Step 3 sırasında hata oluştu: {str(e)}")
            return False

        # step4 başı

    def complete_step4_section(self, title_text="Yeni Bölüm Başlığı"):
        print("\n--- Step 4: Bölüm Oluşturma İşlemi Başladı ---")
        try:
            # adım29: Kullanıcı New Section butonuna tıklar
            # 1. 'New Section' Butonuna Tıkla
            new_section_btn = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "js-add-chapter")]'))
            )
            new_section_btn.click()
            time.sleep(2)  # Modalın animasyonu için bekleme

            # adım30: Kullanıcı başlığı girer
            # 2. Title Box (Java'daki gibi 2. index)
            AJAX_BOX_XPATH = "(//input[@name='ajax[chapter][title]'])[2]"
            ajax_box = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, AJAX_BOX_XPATH))
            )
            # HighLight & Slow Send Keys
            self.driver.execute_script("arguments[0].style.border='3px solid red'", ajax_box)
            ajax_box.clear()
            for char in title_text:
                ajax_box.send_keys(char)
                time.sleep(0.1)
            print(f"✅ Başlık girildi: {title_text}")

            # adım31: Kullanıcı Save butonuna tıklar
            # 3. Save Butonu (Java'daki [2] index ve forceClickWithJS mantığı)
            # Sınıf isimlerini Java'daki gibi tam eşleşme veya contains ile alıyoruz
            SEC_SAVE_BUTTON_XPATH = "(//button[contains(@class, 'save-chapter')])[2]"
            sec_save_button = self.driver.find_element(By.XPATH, SEC_SAVE_BUTTON_XPATH)

            # Actions: MoveToElement (Java'daki hover işlemi)
            actions = ActionChains(self.driver)
            actions.move_to_element(sec_save_button).perform()
            time.sleep(1)  # Hover sonrası kısa stabilizasyon

            # JavaScript ile Force Click (Java'daki ClickUtils.forceClickWithJS)
            self.driver.execute_script("arguments[0].style.border='3px solid yellow'", sec_save_button)
            self.driver.execute_script("arguments[0].click();", sec_save_button)
            print("✅ Save butonuna JS ile zorlanarak tıklandı.")
            # adım32: Kullanıcı modalın kapanmasını bekler
            # 4. Modalın kapanmasını bekle (Java'daki uzun bekleme yerine dinamik kontrol)
            WebDriverWait(self.driver, 15).until(EC.invisibility_of_element_located((By.CLASS_NAME, "swal2-container")))
            print("⭐ Bölüm başarıyla kaydedildi.")
            return True

        except Exception as e:
            print(f"❌ Step 4 Save İşleminde Hata: {e}")
            return False

    def step4(self, title_text="Yeni Bölüm Başlığı"):
        """
        Step 4: New Section oluşturur ve bir sonraki adıma (Step 5) geçişi kutlar.
        """
        print("\n" + "🚀" * 15)
        print("STEP 4: MACERA BAŞLIYOR...")
        print("🚀" * 15)

        try:
            # adım33: Kullanıcı New Section butonuna tıklar
            # 1. 'New Section' Butonuna Tıkla
            new_section_btn = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "js-add-chapter")]'))
            )
            new_section_btn.click()
            time.sleep(2)  # Modal animasyonu için bekleme

            # adım34: Kullanıcı başlığı girer
            # 2. Title Box (Java'daki gibi 2. index)
            # HTML'de birden fazla aynı isimli input olduğu için [2] kritik!
            AJAX_BOX_XPATH = "(//input[@name='ajax[chapter][title]'])[2]"
            ajax_box = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, AJAX_BOX_XPATH))
            )

            # adım35: Kullanıcı başlığı girer
            # HighLight & Yazma (Java: slowSendKeys simülasyonu)
            self.driver.execute_script("arguments[0].style.border='3px solid red'", ajax_box)
            ajax_box.clear()
            for char in title_text:
                ajax_box.send_keys(char)
                time.sleep(0.05)
            print(f"✅ Bölüm başlığı '{title_text}' başarıyla girildi.")

            # adım36: Kullanıcı Save butonuna tıklar
            # 3. Save Butonu (Java: Force Click JS & Index [2])
            SEC_SAVE_BUTTON_XPATH = "(//button[contains(@class, 'save-chapter')])[2]"
            sec_save_button = self.driver.find_element(By.XPATH, SEC_SAVE_BUTTON_XPATH)

            # Actions: Hover (Java: moveToElement)
            ActionChains(self.driver).move_to_element(sec_save_button).perform()
            time.sleep(1)

            # JS Force Click
            self.driver.execute_script("arguments[0].style.border='3px solid yellow'", sec_save_button)
            self.driver.execute_script("arguments[0].click();", sec_save_button)
            print("✅ Save butonuna JavaScript ile 'ZORLA' basıldı!")

            # adım37: Kullanıcı modalın kapanmasını bekler
            # 4. Modalın Kapanışını Bekle
            WebDriverWait(self.driver, 15).until(EC.invisibility_of_element_located((By.CLASS_NAME, "swal2-container")))

            # adım38: Kullanıcı Next Step butonuna tıklar
            # 5. Büyük Final: Next Step ve Kutlama
            next_button = self.driver.find_element(By.ID, "getNextStep")
            self.driver.execute_script("arguments[0].style.border='5px solid gold'", next_button)
            next_button.click()

            # adım39: Kullanıcı step4 icin guclu bir basarı mesajı yayınlar
            # ( --> Hocam testin en zor kısımlarından birisi olduğu için basarı mesajı guclu gerekiyor
            # Step 5'e geçiş doğrulaması
            WebDriverWait(self.driver, 15).until(EC.url_contains("step/5"))

            # --- GÖVDE GÖSTERİSİ BÖLÜMÜ ---
            print("\n" + "⭐" * 50)
            print("🏆 ZAFER! STEP 4 CANAVARI ETKİSİZ HALE GETİRİLDİ!")
            print(f"🔗 YENİ KONUM: {self.driver.current_url}")
            print("📝 İŞLEM: Dinamik Modal aşıldı ve New Section başarıyla eklendi.")
            print("🔥 SONUÇ: Step 5 (Media/Video) kapıları sonuna kadar açıldı!")
            print("⭐" * 50 + "\n")

            return True

        except Exception as e:
            print(f"\n❌ MAALESEF BİR ENGELLE KARŞILAŞTIK: {e}")
            return False

    def step5(self, search_text="SDET"):
        print("\n" + "🛡️" * 15)
        print("STEP 5: PREREQUISITES GÖREVİ BAŞLADI")
        print("🛡️" * 15)

        try:
            # adım40: Kullanıcı New Prerequisite butonuna tıklar
            # 1. New Prerequisite Butonuna Tıkla
            new_pre_btn = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "webinarAddPrerequisites"))
            )
            new_pre_btn.click()
            time.sleep(1)
            print("✅ New Prerequisite butonu tıklandı.")

            # adım41: Kullanıcı Select2 container açar
            # 2. Container'ı aç (Java'daki select2-container mantığı)
            container = self.driver.find_element(By.CLASS_NAME, "select2-selection__placeholder")
            self.driver.execute_script("arguments[0].style.border='3px solid red'", container)
            container.click()
            print("✅ Select2 container açıldı.")

            # adım42: Kullanıcı arama kutucuğunu doldurur
            # 3. Arama Kutusuna Yaz (Dinamik input)
            # Select2 genellikle 'select2-search__field' class'ını kullanır
            search_field = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "select2-search__field"))
            )
            search_field.send_keys(search_text)
            time.sleep(2)  # Sonuçların listelenmesi için bekleme

            # adım43: Kullanıcı arama sonucuna tıklar (--> hocam buraya sonra donecegiz . robotik yapacagız aklımda)
            # ( --> simdilik boyle olsun
            # 4. Ofset Tıklama (30 Piksel Aşağı) - Java'daki Actions mantığı
            print(f"🎯 '{search_text}' için 30 piksel altına tıklanıyor...")
            actions = ActionChains(self.driver)
            # Arama kutusunun tam ortasından 30 piksel aşağıya
            actions.move_to_element(search_field).move_by_offset(0, 30).click().perform()


            # adım44: Kullanıcı Save butonuna tıklar
            # 5. Save İşlemi
            save_btn = self.driver.find_element(By.CLASS_NAME, "js-save-prerequisite")
            self.driver.execute_script("arguments[0].style.border='3px solid orange'", save_btn)
            save_btn.click()

           # adım45 : Kullanıcı next butonuna tıklar
            time.sleep(3)
            next_btn = self.driver.find_element(By.ID, "getNextStep")
            self.driver.execute_script("arguments[0].style.border='3px solid green'", next_btn)
            next_btn.click()

            # adım46: Kullanıcı step5 icin basarı mesajı yayınlar
            print("\n" + "🎊" * 20)
            print("KAZANDIK! Step 5 Prerequisites başarıyla kaydedildi!")
            print("🎊" * 20 + "\n")
            return True

        except Exception as e:
            print(f"❌ Step 5'te bir engel çıktı: {e}")
            return False

    def step6(self, faq_question="Ogretmenler ile gorusme sıklıgı",
              faq_answer="Ogrencilerimiz 2 haftada 1 15 dk zoom gorusmesi yapabilirler"):
        """
        Step 6: FAQ (Sıkça Sorulan Sorular) bölümünü doldurur ve Step 7'ye geçişi doğrular.
        """
        print("\n" + "❓" * 15)
        print("STEP 6: FAQ (SSS) OLUŞTURMA BAŞLADI")
        print("❓" * 15)

        try:
            # adım47: Kullanıcı New FAQ butonuna tıklar
            # 1. New FAQ Butonuna Tıkla
            nwFAQButton_Xpath = '//button[@id="webinarAddFAQ"]'
            nwFAQButton = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, nwFAQButton_Xpath))
            )
            self.driver.execute_script("arguments[0].style.border='3px solid red'", nwFAQButton)
            nwFAQButton.click()
            time.sleep(1)
            print("✅ New FAQ butonu tıklandı.")

            # adım48: Kullanıcı Soru  girer
            # 2. Title (Soru) Box
            titleBox_Xpath = '//input[@name="ajax[new][title]"]'
            titleBox = self.driver.find_element(By.XPATH, titleBox_Xpath)
            self.driver.execute_script("arguments[0].style.border='3px solid green'", titleBox)
            titleBox.clear()
            titleBox.send_keys(faq_question)
            print(f"✅ Soru girildi: {faq_question}")

            # adım49: Kullanıcı Cevap girer
            # 3. Answer (Cevap) Box
            answerBox_Xpath = '//textarea[@name="ajax[new][answer]"]'
            answerBox = self.driver.find_element(By.XPATH, answerBox_Xpath)
            self.driver.execute_script("arguments[0].style.border='3px solid blue'", answerBox)
            answerBox.clear()
            answerBox.send_keys(faq_answer)
            print(f"✅ Cevap girildi: {faq_answer}")

            # adım50: Kullanıcı Save butonuna tıklar
            # 4. Save Button
            saveButton_Xpath = '//button[@class="js-save-faq btn btn-sm btn-primary"]'
            saveButton = self.driver.find_element(By.XPATH, saveButton_Xpath)
            self.driver.execute_script("arguments[0].style.border='3px solid yellow'", saveButton)
            saveButton.click()
            print("✅ FAQ kaydedildi.")

            # Modalın kapanması için kısa bir bekleme
            time.sleep(2)

            # adım51: Kullanıcı Next Step butonuna tıklar
            # 5. Next Step Button
            nextStepButton_Xpath = '//button[@id="getNextStep"]'
            nextStepButton = self.driver.find_element(By.XPATH, nextStepButton_Xpath)
            self.driver.execute_script("arguments[0].scrollIntoView();", nextStepButton)
            self.driver.execute_script("arguments[0].style.border='3px solid orange'", nextStepButton)
            nextStepButton.click()
            print("🚀 Next Step butonuna tıklandı. URL kontrol ediliyor...")

            # adım52: Kullanıcı step6 icin basarı mesajı yayınlar
            # 6. URL Doğrulaması (Step 7'ye geçtik mi?)
            WebDriverWait(self.driver, 15).until(EC.url_contains("step/7"))

            if "step/7" in self.driver.current_url:
                print("\n" + "✨" * 30)
                print("BAŞARILI: FAQ eklendi ve Step 7'ye (Final) ulaşıldı!")
                print(f"Mevcut URL: {self.driver.current_url}")
                print("✨" * 30 + "\n")
                return True
            else:
                print("❌ HATA: Step 7'ye geçilemedi!")
                return False

        except Exception as e:
            print(f"❌ Step 6 sırasında bir hata oluştu: {e}")
            return False

    def step7(self, quiz_title="Certifica alma sınavı", exam_time="45", attempt_count="3"):
        """
        Step 7: Quiz oluşturur, ayarları yapılandırır ve kursu incelemeye gönderir.
        """
        print("\n" + "=" * 50)
        print("🚀 STEP 7: QUIZ OLUŞTURMA VE YAYINLAMA BAŞLATILDI")
        print("=" * 50)

        try:
            # adım53: Kullanıcı New Quiz butonuna tıklar
            # newQuizButton
            newQuizButton_Xpath = '//button[@id="webinarAddQuiz"]'
            newQuizButton = self.driver.find_element(By.XPATH, newQuizButton_Xpath)
            self.driver.execute_script("arguments[0].style.border='3px solid red'", newQuizButton)
            newQuizButton.click()
            time.sleep(1)

            # adım54 : Kullanıcı quiz icin title girer
            # 1. Quiz Title (Zaten doğru çalışıyor ama index [1] önemli)
            quizTitleBox_Xpath = '(//input[@name="ajax[new][title]"])[1]'
            quizTitleBox = self.driver.find_element(By.XPATH, quizTitleBox_Xpath)
            quizTitleBox.clear()
            quizTitleBox.send_keys(quiz_title)

            # adım55 : Kullanıcı exam time girer
            # 2. Exam Time
            ExamTimeBox_Xpath = '//input[@name="ajax[new][time]"]'
            ExamTimeBox = self.driver.find_element(By.XPATH, ExamTimeBox_Xpath)
            ExamTimeBox.clear()
            ExamTimeBox.send_keys(exam_time)
            time.sleep(1)

            # adım56 : Kullanıcı attempt count girer (--> Hocam burası da zor bir asama )
            # 3. Number of Attempts
            attemptBox_Xpath = '//input[@name="ajax[new][attempt]"]'
            attemptBox = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, attemptBox_Xpath))
            )

            # --- ETKİLİ KAYDIRMA VE GİRİŞ ---
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", attemptBox)
            time.sleep(1)

            # Görsel olarak doğrula
            self.driver.execute_script("arguments[0].style.border='4px solid yellow'", attemptBox)

            # İçeriği sil ve yeni değeri gir
            attemptBox.send_keys(Keys.CONTROL + "a")
            attemptBox.send_keys(Keys.BACKSPACE)
            attemptBox.send_keys(attempt_count)
            time.sleep(1)

            print("✅ Attempt sayısı başarıyla girildi!")

            # adım57 : Kullanıcı pass mark girer
            # passMarkBox
            passMarkBox_Xpath = '(//input[@class="js-ajax-pass_mark form-control "])[1]'
            passMarkBox = self.driver.find_element(By.XPATH, passMarkBox_Xpath)
            self.driver.execute_script("arguments[0].style.border='3px solid orange'", passMarkBox)
            passMarkBox.clear()
            passMarkBox.send_keys("50")
            time.sleep(1)

            # adım58 : Kullanıcı expires day girer
            # expiresDayBox
            expiresDayBox_Xpath = '//input[@name="ajax[new][expiry_days]"]'
            expiresDayBox = self.driver.find_element(By.XPATH, expiresDayBox_Xpath)
            self.driver.execute_script("arguments[0].style.border='3px solid purple'", expiresDayBox)
            expiresDayBox.clear()
            expiresDayBox.send_keys("15")
            time.sleep(1)

            # adım59: Kullaıcı soru tiplerini kaynaktan secer
            # selectQuestionBankRadioButton
            selectQuestionBankRadioButton_Xpath = '(//label[@class="custom-control-label"])[1]'
            selectQuestionBankRadioButton = self.driver.find_element(By.XPATH, selectQuestionBankRadioButton_Xpath)
            self.driver.execute_script("arguments[0].style.border='3px solid pink'", selectQuestionBankRadioButton)
            selectQuestionBankRadioButton.click()
            time.sleep(1)

            # adım60: Kullanıcı certificate secer
            # selectCertificateButton
            selectCertificateButton_Xpath = '(//*[@class="custom-control custom-switch"])[2]'
            selectCertificateButton = self.driver.find_element(By.XPATH, selectCertificateButton_Xpath)
            self.driver.execute_script("arguments[0].style.border='3px solid cyan'", selectCertificateButton)
            selectCertificateButton.click()
            time.sleep(1)

            # adım61: Kullanıcı active quiz secer
            # selectActiveQuizRadioButton
            selectActiveQuizRadioButton_Xpath = '(//label[@class="custom-control-label"])[3]'
            selectActiveQuizRadioButton = self.driver.find_element(By.XPATH, selectActiveQuizRadioButton_Xpath)
            self.driver.execute_script("arguments[0].style.border='3px solid brown'", selectActiveQuizRadioButton)
            selectActiveQuizRadioButton.click()
            time.sleep(7)

            # adım62: Kullanıcı createButton
            # createButton
            createButton_Xpath = '(//button[@class="js-submit-quiz-form btn btn-sm btn-primary"])[1]'
            createButton = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, createButton_Xpath))
            )
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", createButton)
            time.sleep(1)

            self.driver.execute_script("arguments[0].style.border='3px solid gray'", createButton)
            createButton.click()
            time.sleep(4)

            # adım63: Kullanıcı publishButton a basarak kursu yayınlar
            # publishButton
            publishButton_Xpath = '//button[@id="sendForReview"]'
            publishButton = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, publishButton_Xpath))
            )

            actions = ActionChains(self.driver)
            actions.move_to_element(publishButton).perform()  # Hover yap
            time.sleep(1)

            self.driver.execute_script("arguments[0].style.border='3px solid black'", publishButton)
            publishButton.click()
            time.sleep(7)

            print("✅ İşlemler tamamlandı!")

            # adım64: Kullanıcı step7 icin basarı mesajı yayınlar
            WebDriverWait(self.driver, 15).until(EC.url_contains("panel/webinars"))

            print("\n" + "⭐" * 60)
            print("                KURS OLUŞTURMA TEST RAPORU                ")
            print("⭐" * 60)
            print(f"📊 Test Durumu      : BAŞARILI ✅")
            print(f"🔗 Son Durak URL    : {self.driver.current_url}")
            print(f"📝 İşlem Özeti      : Step 7 Quiz tanımlandı ve onay için gönderildi.")
            print(f"⏰ Bitiş Zamanı     : {time.strftime('%H:%M:%S')}")
            print(f"🏆 Sonuç            : Kurs listenize başarıyla eklendi.")
            print("⭐" * 60 + "\n")

            return True

        except Exception as e:
            print(f"\n❌ STEP 7 HATASI: {e}")
            return False










        courses_button_Xpath=''











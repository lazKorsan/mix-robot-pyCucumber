import time



from pages.login_page import LoginPage
import properties.test_data as test_data




def test_navigate_loginPage(driver):

    # //<!-- todo login Sayfa nesnesini oluştur
    login_pg = LoginPage(driver)

    # //<!-- todo Metodu çağır (Loglar bu metodun içinden gelecek)
    login_pg.navigate_to_login(test_data.login_url)

    # Doğrulama (Opsiyonel ama iyi bir pratik)
    assert "login" in driver.current_url

    # //<!-- todo gecerli bilgilerle sayfaya giris yapılıyor
    login_pg.login_method(test_data.login_mail, test_data.instructor_password)

    # //<!-- todo new courses sayfasına gitme işlemi
    login_pg.navigate_to_new_courses()

    # //<!-- todo newcourses step1
    login_pg.step1()
    time.sleep(3)

    # //<!-- todo newcourses step2
    login_pg.step2(capacity="60", duration="90", tags="test", category_value="956")
    time.sleep(3)

    # //<!-- todo newcourses step3
    login_pg.step3(access_days="15", price="100")
    time.sleep(3)

    # //<!-- todo newcourses step4
    login_pg.step4(title_text="Yeni Bölüm Başlığı")
    time.sleep(3)

    # //<!-- todo newcourses step5
    login_pg.step5(search_text="SDET")
    time.sleep(3)

    # //<!-- todo newcourses step6
    login_pg.step6(faq_question="Ogretmenler ile gorusme sıklıgı", faq_answer="Ogrencilerimiz 2 haftada 1 15 dk zoom gorusmesi yapabilirler")
    time.sleep(3)

    # //<!-- todo newcourses step7
    login_pg.step7(quiz_title="Certifica alma sınavı", exam_time="45", attempt_count="3")
    time.sleep(3)
















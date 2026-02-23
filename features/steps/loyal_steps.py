from behave import given, then, when
from pages.loyal_friend_pages import LoyalFriendCarePage
from properties.test_data import ly_URL, ly_mail, ly_password


@given(u'Kullanici loyalfriendCare sayfasini acar')
def step_impl(context):
    context.loyal_friend_care_page = LoyalFriendCarePage()
    context.loyal_friend_care_page.set_up()
    context.driver.implicitly_wait(10)

@then(u'Kullanici login sayfasina gider')
def step_impl(context):
    context.loyal_friend_care_page.navigate_to_home_page(ly_URL)

@when(u'Kullanici siteye giriş yapar')
def step_impl(context):
    context.loyal_friend_care_page.login_method_with_valid_data(
        context.driver,
        ly_mail,
        ly_password
    )

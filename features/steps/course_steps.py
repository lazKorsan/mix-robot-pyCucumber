from behave import given, when, then
from pages.login_page import LoginPage
from properties import test_data


@given('the instructor is logged in with valid credentials')
def step_login(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.navigate_to_login(test_data.login_url)
    context.login_page.login_method(
        test_data.login_mail,
        test_data.instructor_password
    )


@given('the instructor navigates to the new course creation page')
def step_navigation(context):
    context.login_page.navigate_to_new_courses()


@when('the instructor completes Step 1: Basic Information')
def step_1(context):
    row = context.table[0]
    context.login_page.step1(
        title=row['title'],
        description=row['description']
    )


@when('the instructor completes Step 2: Extra Information')
def step_2(context):
    row = context.table[0]
    context.login_page.step2(
        capacity=row['capacity'],
        duration=row['duration'],
        tags=row['tags'],
        category_value=row['category']
    )


@when('the instructor completes Step 3: Pricing')
def step_3(context):
    row = context.table[0]
    context.login_page.step3(
        price=row['price'],
        access_days=row['days']
    )


@when('the instructor completes Step 4: Creating a Section')
def step_4(context):
    row = context.table[0]
    context.login_page.step4(
        title_text=row['section_title']
    )


@when('the instructor completes Step 5: Prerequisites')
def step_5(context):
    row = context.table[0]
    context.login_page.step5(
        search_text=row['search_text']
    )


@when('the instructor completes Step 6: FAQ')
def step_6(context):
    row = context.table[0]
    context.login_page.step6(
        faq_question=row['question'],
        faq_answer=row['answer']
    )


@then('the instructor completes Step 7: Quiz and Publishes')
def step_7(context):
    row = context.table[0]
    context.login_page.step7(
        quiz_title=row['quiz_title'],
        attempt_count=row['attempts']
    )

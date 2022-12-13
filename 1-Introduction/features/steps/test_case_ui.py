from selenium import webdriver
from behave import given, when, then


@given('user navigates to "{url}"')
def goto_url(context, url):
    context.driver = webdriver.Chrome('../../chromedriver.exe')
    context.driver.get(url)


@then('title of the page is "{expected_title}"')
def verify_title(context, expected_title):
    assert context.driver.title == expected_title, \
        f"\"Expected {expected_title}\" but got \"{context.driver.title}\""

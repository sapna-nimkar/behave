import time

import requests
from selenium import webdriver
from behave import given, when, then


@given('user enters "{email}" and "{password}"')
def enter_email_password(context, email, password):
    print(email, password)
    url = "https://reqres.in/api/login"
    body = {'email': email, 'password': password}
    response = requests.post(url, data=body)
    context.actual_status_code = response.status_code


@then('user should get response status code "{status_code}"')
def verify_success_status_code(context, status_code):
    expected_status_code = int(status_code)
    assert context.actual_status_code == expected_status_code, \
        f"Expected {expected_status_code} but got {context.actual_status_code}"

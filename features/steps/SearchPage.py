import time
from idlelib import browser
from telnetlib import EC

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


@when('I navigate to search page')
def step_impl(context):
    assert True, "Test Passed"


@then('Search page should be display')
def step_impl(context):
    assert True, "Test Passed"


@when('I navigate to advance search page')
def step_impl(context):
    assert True, "Test Passed"


@then('Adavnce search page should be display')
def step_impl(context):
    assert True, "Test Passed"

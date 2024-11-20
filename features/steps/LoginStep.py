import time
from idlelib import browser
from telnetlib import EC

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


@Then('Enter UserName "{userName}" and Password "{password}"')
def userNameandPassword(context, userName,password):
    user=context.driver.find_element(By.XPATH, "//input[@name='username']")
    user.send_keys(userName)
    pw = context.driver.find_element(By.XPATH, "//input[@name='password']")
    pw.send_keys(password)

@then('Click on Login Button')
def clickLoginButton(context):
    context.driver.find_element(By.XPATH, "//div[@class='oxd-form-actions orangehrm-login-action']").click()
    time.sleep(5)

@then('User successfully login to the dashboard page')
def step_impl(context):
    try:
        dash = context.driver.find_element(By.XPATH, "//span/h6[text()='Dashboard']")
    except:
        assert False, "Test is Failed"

    if dash.text=="Dashboard":
        assert True, "Test is Passed"
        #assert dash.is_displayed() is True;


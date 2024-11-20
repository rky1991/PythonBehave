import time
from idlelib import browser
from telnetlib import EC

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


@Given('launch Crome Browser')
def launchBrowser(context):
    context.driver= webdriver.Chrome()
    context.driver.maximize_window()
    #context.driver=webdriver.chrome(executable_path="./drivers/chromedriver.exe")


@When('open Orange HRM homepage')
def homePageVerification(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")
    time.sleep(5)
    # wait = WebDriverWait(browser, 20)
    # wait.until(EC.istitle())



@then('verify that the logo present on page')
def logoVerfication(context):
    context.driver.implicitly_wait(20)
    status=context.driver.find_element(By.XPATH,"//div[@class='orangehrm-login-branding']/img").is_displayed()
    print("Status Value ---->>>>"+str(status))
    assert status is True

@then('close Browser')
def closeBrowser(context):
    context.driver.close()






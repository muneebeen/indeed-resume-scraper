from time import sleep
# import scrapy
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import re

if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--window-size=1880,1300")
    options.add_argument("--disable-notifications")
    driver = webdriver.Chrome(options=options)
    # driver.maximize_window()
    driver.get('https://www.indeed.com/')
    sleep(1)
    driver.find_element(By.CSS_SELECTOR,'a#EmployersPostJob').click()
    sleep(1)
    driver.find_element(By.CSS_SELECTOR, 'a[data-gnav-element-name="SignIn"]').click()
    sleep(1)
    for ch in 'muneebahmed.753@gmail.com':
        driver.find_element(By.CSS_SELECTOR, 'input#ifl-InputFormField-3').send_keys(ch)
        sleep(0.2)
    sleep(1)
    driver.find_element(By.CSS_SELECTOR, 'button[data-tn-element ="auth-page-email-submit-button"]').click()
    sleep(2)
    driver.find_element(By.ID, 'auth-page-google-password-fallback').click()
    sleep(1)
    for ch in 'qwertyuiop1234567890':
        driver.find_element(By.CSS_SELECTOR, 'input[type = "password"]').send_keys(ch)
        sleep(0.2)
    sleep(1)
    driver.find_element(By.CSS_SELECTOR, 'button[ data-tn-element = "auth-page-sign-in-password-form-submit-button"]').click()
    sleep(3)
    captcha = driver.find_element(By.CSS_SELECTOR, 'div.pass-Captcha')
    if captcha:
        pass
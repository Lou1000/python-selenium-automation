from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.chrome.service import Service

# driver = webdriver.Chrome(executable_path='/Users/loulouangibeau/Documents/QA-Automation/python-selenium-automation/chromedriver')
service = Service('/Users/loulouangibeau/Documents/QA-Automation/python-selenium-automation/chromedriver')
driver = webdriver.Chrome(service=service)

driver.get('https://www.amazon.com/')

driver.find_element(By.XPATH, "//a[@id='nav-orders']").click()
driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo']")
driver.find_element(By.ID, "ap_email")

expected_result = '"table"'
actual_result = driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text
print(actual_result)

assert expected_result == actual_result, f'Expected {expected_result} but got actual {actual_result}'
print('Test case passed')

driver.quit()
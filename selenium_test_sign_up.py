import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import unittest;
import string
import random
class TestLoginduplicate(unittest.TestCase):
  def setUp(self):
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications" : 2}
    chrome_options.add_experimental_option("prefs",prefs)
    self.driver = webdriver.Chrome("drivers/chromedriver",chrome_options=chrome_options)
    self.vars = {}
  
  def tearDown(self):
    self.driver.close()
  
  def test_signup_duplicate(self):
    self.driver.get("http://localhost:3001/activations")
    self.driver.set_window_size(1600, 900)
    element = self.driver.find_element(By.CSS_SELECTOR, ".AppBar__menu-item")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()
    element = self.driver.find_element(By.CSS_SELECTOR, ".AppBar__menu-item")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, ".AppBar__menu-item")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
    self.driver.find_element(By.CSS_SELECTOR, ".AppBar__menu-item").click()
    self.driver.find_element(By.CSS_SELECTOR, ".LoginDialog__title--clickable").click()
    element = self.driver.find_element(By.CSS_SELECTOR, "button:nth-child(1) > div > div > div > span")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".Tabs > div > button:nth-child(1) > div").click()
    self.driver.find_element(By.XPATH, "//div[@id=\'content\']/div/div/div[2]/div/div/div/div/div/div[4]/div/div[3]/div/form/div/div/div/input").click()
    self.driver.find_element(By.XPATH, "//div[@id=\'content\']/div/div/div[2]/div/div/div/div/div/div[4]/div/div[3]/div/form/div/div/div/input").send_keys("12345654321@gmail.com")
    self.driver.find_element(By.XPATH, "//div[@id=\'content\']/div/div/div[2]/div/div/div/div/div/div[4]/div/div[3]/div/form/div/div[2]/div/input").click()
    self.driver.find_element(By.XPATH, "//div[@id=\'content\']/div/div/div[2]/div/div/div/div/div/div[4]/div/div[3]/div/form/div/div[2]/div/input").send_keys("password")
    self.driver.find_element(By.XPATH, "//div[2]/div/div/button/div/div/span").click()
    WebDriverWait(self.driver, 1000).until(expected_conditions.presence_of_element_located((By.XPATH, "//form/div/div/div/div[3]")))
    elements = self.driver.find_elements(By.XPATH, "//form/div/div/div/div[3]")
    assert len(elements) > 0
    assert self.driver.find_element(By.XPATH,"//form/div/div/div/div[3]").text == "User with this e-mail address has been already registered"

  def test_signup(self, email = None):
    self.driver.get("http://localhost:3001/activations")
    self.driver.set_window_size(1600, 900)
    self.driver.find_element(By.CSS_SELECTOR, ".AppBar__menu-item").click()
    self.driver.find_element(By.CSS_SELECTOR, ".LoginDialog__title--clickable").click()
    self.driver.find_element(By.CSS_SELECTOR, ".Tabs > div > button:nth-child(1) > div").click()
    self.driver.find_element(By.XPATH, "//div[@id=\'content\']/div/div/div[2]/div/div/div/div/div/div[4]/div/div[3]/div/form/div/div/div/input").click()
    letters = string.ascii_letters
    if(email == None):
      email = ''.join(random.choice(letters) for i in range(10)) + "@gmail.com"
    self.driver.find_element(By.XPATH, "//div[@id=\'content\']/div/div/div[2]/div/div/div/div/div/div[4]/div/div[3]/div/form/div/div/div/input").send_keys(email)
    self.driver.find_element(By.XPATH, "//div[@id=\'content\']/div/div/div[2]/div/div/div/div/div/div[4]/div/div[3]/div/form/div/div[2]/div/input").click()
    self.driver.find_element(By.XPATH, "//div[@id=\'content\']/div/div/div[2]/div/div/div/div/div/div[4]/div/div[3]/div/form/div/div[2]/div/input").send_keys("passworod")
    self.driver.find_element(By.XPATH, "//div[@id=\'content\']/div/div/div[2]/div/div/div/div/div/div[4]/div/div[3]/div/form/div[2]/div/div/button/div/div/span").click()
    self.driver.find_element(By.XPATH, "//div[@id=\'content\']/div/div/div[2]/div/div/div/div/div/div[4]/div/div[3]/div/form").click()
    WebDriverWait(self.driver, 5000).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@id=\'content\']/div/div/div[2]/div/div/div/div/div/div[4]/div/div[3]/div/form/div[2]")))
    elements = self.driver.find_elements(By.XPATH, "//div[@id=\'content\']/div/div/div[2]/div/div/div/div/div/div[4]/div/div[3]/div/form/div[2]")
    assert len(elements) > 0
    time.sleep(3)
    assert self.driver.find_element(By.XPATH, "//div[@id=\'content\']/div/div/div[2]/div/div/div/div/div/div[4]/div/div[3]/div/form/div[2]").text == "The confirmation letter was sent to your e-mail"
  
  def test_signupwithwrongemailformat(self):
    self.driver.get("http://localhost:3001/activations")
    self.driver.set_window_size(1600, 900)
    self.driver.find_element(By.CSS_SELECTOR, ".AppBar__menu-item").click()
    self.driver.find_element(By.CSS_SELECTOR, ".LoginDialog__title--clickable").click()
    self.driver.find_element(By.XPATH, "//div[@id=\'content\']/div/div/div[2]/div/div/div/div/div/div[4]/div/div[3]/div[2]/form/div/div/div/input").click()
    letters = string.ascii_letters
    random_wrong_format_email = ''.join(random.choice(letters) for i in range(10)) + "gmail.com"
    self.driver.find_element(By.XPATH, "//div[@id=\'content\']/div/div/div[2]/div/div/div/div/div/div[4]/div/div[3]/div[2]/form/div/div/div/input").send_keys(random_wrong_format_email)
    self.driver.find_element(By.XPATH, "//div[@id=\'content\']/div/div/div[2]/div/div/div/div/div/div[4]/div/div[3]/div[2]/form/div/div[2]/div/input").click()
    self.driver.find_element(By.XPATH, "//div[@id=\'content\']/div/div/div[2]/div/div/div/div/div/div[4]/div/div[3]/div[2]/form/div/div[2]/div/input").send_keys("password")
    self.driver.find_element(By.XPATH, "//div[@id=\'content\']/div/div/div[2]/div/div/div/div/div/div[4]/div/div[3]/div[2]/form/div[2]/div/div/button/div/div/span").click()
    WebDriverWait(self.driver, 1000).until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@id=\'content\']/div/div/div[2]/div/div/div/div/div/div[4]/div/div[3]/div[2]/form/div/div/div/div[3]")))
    assert self.driver.find_element(By.XPATH, "//div[@id=\'content\']/div/div/div[2]/div/div/div/div/div/div[4]/div/div[3]/div[2]/form/div/div/div/div[3]").text == "Invalid login or password"
  

  def test_signupwithverylongemail(self):
    self.driver.get("http://localhost:3001/activations")
    self.driver.set_window_size(1600, 900)
    self.driver.find_element(By.CSS_SELECTOR, ".AppBar__menu-item").click()
    self.driver.find_element(By.CSS_SELECTOR, ".LoginDialog__title--clickable").click()
    self.driver.find_element(By.XPATH, "//div[@id=\'content\']/div/div/div[2]/div/div/div/div/div/div[4]/div/div[3]/div[2]/form/div/div/div/input").click()
    letters = string.ascii_letters
    random_very_long_email = ''.join(random.choice(letters) for i in range(100)) + "gmail.com"
    self.driver.find_element(By.XPATH, "//div[@id=\'content\']/div/div/div[2]/div/div/div/div/div/div[4]/div/div[3]/div[2]/form/div/div/div/input").send_keys(random_very_long_email)
    self.driver.find_element(By.XPATH, "//div[@id=\'content\']/div/div/div[2]/div/div/div/div/div/div[4]/div/div[3]/div[2]/form/div/div[2]/div/input").click()
    self.driver.find_element(By.XPATH, "//div[@id=\'content\']/div/div/div[2]/div/div/div/div/div/div[4]/div/div[3]/div[2]/form/div/div[2]/div/input").send_keys("password")
    self.driver.find_element(By.XPATH, "//div[@id=\'content\']/div/div/div[2]/div/div/div/div/div/div[4]/div/div[3]/div[2]/form/div[2]/div/div/button/div/div/span").click()
    WebDriverWait(self.driver, 1000).until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@id=\'content\']/div/div/div[2]/div/div/div/div/div/div[4]/div/div[3]/div[2]/form/div/div/div/div[3]")))
    time.sleep(3)
    assert self.driver.find_element(By.XPATH, "//div[@id=\'content\']/div/div/div[2]/div/div/div/div/div/div[4]/div/div[3]/div[2]/form/div/div/div/div[3]").text == "Invalid login or password"
  
  def test_signupwithverylongpassword(self):
    self.driver.get("http://localhost:3001/activations")
    self.driver.set_window_size(1600, 900)
    self.driver.find_element(By.CSS_SELECTOR, ".AppBar__menu-item").click()
    self.driver.find_element(By.CSS_SELECTOR, ".LoginDialog__title--clickable").click()
    self.driver.find_element(By.XPATH, "//div[@id=\'content\']/div/div/div[2]/div/div/div/div/div/div[4]/div/div[3]/div[2]/form/div/div/div/input").click()
    letters = string.ascii_letters
    email = ''.join(random.choice(letters) for i in range(10)) + "@gmail.com"
    random_very_long_password = ''.join(random.choice(letters) for i in range(100))
    self.driver.find_element(By.XPATH, "//div[@id=\'content\']/div/div/div[2]/div/div/div/div/div/div[4]/div/div[3]/div[2]/form/div/div/div/input").send_keys(email)
    self.driver.find_element(By.XPATH, "//div[@id=\'content\']/div/div/div[2]/div/div/div/div/div/div[4]/div/div[3]/div[2]/form/div/div[2]/div/input").click()
    self.driver.find_element(By.XPATH, "//div[@id=\'content\']/div/div/div[2]/div/div/div/div/div/div[4]/div/div[3]/div[2]/form/div/div[2]/div/input").send_keys(random_very_long_password)
    self.driver.find_element(By.XPATH, "//div[@id=\'content\']/div/div/div[2]/div/div/div/div/div/div[4]/div/div[3]/div[2]/form/div[2]/div/div/button/div/div/span").click()
    WebDriverWait(self.driver, 1000).until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@id=\'content\']/div/div/div[2]/div/div/div/div/div/div[4]/div/div[3]/div[2]/form/div/div/div/div[3]")))
    time.sleep(3)
    assert self.driver.find_element(By.XPATH, "//div[@id=\'content\']/div/div/div[2]/div/div/div/div/div/div[4]/div/div[3]/div[2]/form/div/div/div/div[3]").text == "Invalid login or password"
  

if __name__ == '__main__':
  unittest.main()
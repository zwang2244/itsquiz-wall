# Generated by Selenium IDE
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

class TestSignin(unittest.TestCase):
  def setUp(self):
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications" : 2}
    chrome_options.add_experimental_option("prefs",prefs)
    self.driver = webdriver.Chrome("drivers/chromedriver",options=chrome_options)
    self.vars = {}
  
  def tearDown(self):
    self.driver.close()
  
  def test_signin(self):
    self.driver.get("http://localhost:3001/activations")
    self.driver.set_window_size(1600, 900)
    self.driver.find_element(By.CSS_SELECTOR, ".AppBar__menu-item").click()
    self.driver.find_element(By.CSS_SELECTOR, ".LoginDialog__title--clickable").click()
    self.driver.find_element(By.XPATH, "//div[@id=\'content\']/div/div/div[2]/div/div/div/div/div/div[4]/div/div[3]/div[2]/form/div/div/div/input").click()
    self.driver.find_element(By.XPATH, "//div[@id=\'content\']/div/div/div[2]/div/div/div/div/div/div[4]/div/div[3]/div[2]/form/div/div/div/input").send_keys("zhilinw3@illinois.edu")
    self.driver.find_element(By.XPATH, "//div[@id=\'content\']/div/div/div[2]/div/div/div/div/div/div[4]/div/div[3]/div[2]/form/div/div[2]/div/input").click()
    self.driver.find_element(By.XPATH, "//div[@id=\'content\']/div/div/div[2]/div/div/div/div/div/div[4]/div/div[3]/div[2]/form/div/div[2]/div/input").send_keys("password")
    self.driver.find_element(By.XPATH, "//div[@id=\'content\']/div/div/div[2]/div/div/div/div/div/div[4]/div/div[3]/div[2]/form/div[2]/div/div/button/div/div/span").click()
    time.sleep(3)
    self.driver.find_element(By.XPATH, "//div[3]/div/img").click()
    self.driver.find_element(By.XPATH, "//div[@id=\'content\']/div/div/div/div[2]/div[3]/div/div/div/div/div[3]/div[2]/div/button/div/div/span").click()
  

  def test_signinwithwrongpassword(self):
    self.driver.get("http://localhost:3001/activations")
    self.driver.set_window_size(1600, 900)
    self.driver.find_element(By.CSS_SELECTOR, ".AppBar__menu-item").click()
    self.driver.find_element(By.CSS_SELECTOR, ".LoginDialog__title--clickable").click()
    self.driver.find_element(By.CSS_SELECTOR, ".LoginForm .TextField:nth-child(1) hr:nth-child(1)").click()
    self.driver.find_element(By.XPATH, "//div[@id=\'content\']/div/div/div[2]/div/div/div/div/div/div[4]/div/div[3]/div[2]/form/div/div/div/input").click()
    self.driver.find_element(By.XPATH, "//div[@id=\'content\']/div/div/div[2]/div/div/div/div/div/div[4]/div/div[3]/div[2]/form/div/div/div/input").send_keys("zhilinw3@illinois.edu")
    self.driver.find_element(By.XPATH, "//div[@id=\'content\']/div/div/div[2]/div/div/div/div/div/div[4]/div/div[3]/div[2]/form/div/div[2]/div/input").click()
    self.driver.find_element(By.XPATH, "//div[@id=\'content\']/div/div/div[2]/div/div/div/div/div/div[4]/div/div[3]/div[2]/form/div/div[2]/div/input").send_keys("123")
    self.driver.find_element(By.XPATH, "//div[@id=\'content\']/div/div/div[2]/div/div/div/div/div/div[4]/div/div[3]/div[2]/form").click()
    self.driver.find_element(By.XPATH, "//div[@id=\'content\']/div/div/div[2]/div/div/div/div/div/div[4]/div/div[3]/div[2]/form/div[2]/div/div/button/div/div/span").click()
    WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".TextField:nth-child(1) div:nth-child(4)")))
    assert self.driver.find_element(By.CSS_SELECTOR, ".TextField:nth-child(1) div:nth-child(4)").text == "Invalid login or password"
  
  def test_signinwithunactivated(self):
    self.driver.get("http://localhost:3001/activations")
    self.driver.set_window_size(1600, 900)
    self.driver.find_element(By.CSS_SELECTOR, ".AppBar__menu-item").click()
    self.driver.find_element(By.CSS_SELECTOR, ".LoginDialog__title--clickable").click()
    self.driver.find_element(By.XPATH, "//div[@id=\'content\']/div/div/div[2]/div/div/div/div/div/div[4]/div/div[3]/div[2]/form/div/div/div/input").click()
    self.driver.find_element(By.XPATH, "//div[@id=\'content\']/div/div/div[2]/div/div/div/div/div/div[4]/div/div[3]/div[2]/form/div/div/div/input").send_keys("12345654321@gmail.com")
    self.driver.find_element(By.XPATH, "//div[@id=\'content\']/div/div/div[2]/div/div/div/div/div/div[4]/div/div[3]/div[2]/form/div/div[2]/div/input").click()
    self.driver.find_element(By.XPATH, "//div[@id=\'content\']/div/div/div[2]/div/div/div/div/div/div[4]/div/div[3]/div[2]/form/div/div[2]/div/input").send_keys("password")
    self.driver.find_element(By.XPATH, "//div[@id=\'content\']/div/div/div[2]/div/div/div/div/div/div[4]/div/div[3]/div[2]/form/div[2]/div/div/button/div/div/span").click()
    WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".TextField:nth-child(1) div:nth-child(4)")))
    assert self.driver.find_element(By.CSS_SELECTOR, ".TextField:nth-child(1) div:nth-child(4)").text == "This account is not active"
  
  def test_signinwithunactivatedincorrect(self):
    self.driver.get("http://localhost:3001/activations")
    self.driver.set_window_size(1600, 900)
    self.driver.find_element(By.CSS_SELECTOR, ".AppBar__menu-item").click()
    self.driver.find_element(By.CSS_SELECTOR, ".LoginDialog__title--clickable").click()
    self.driver.find_element(By.XPATH, "//div[@id=\'content\']/div/div/div[2]/div/div/div/div/div/div[4]/div/div[3]/div[2]/form/div/div/div/input").click()
    self.driver.find_element(By.XPATH, "//div[@id=\'content\']/div/div/div[2]/div/div/div/div/div/div[4]/div/div[3]/div[2]/form/div/div/div/input").send_keys("12345654321@gmail.com")
    self.driver.find_element(By.XPATH, "//div[@id=\'content\']/div/div/div[2]/div/div/div/div/div/div[4]/div/div[3]/div[2]/form/div/div[2]/div/input").click()
    self.driver.find_element(By.XPATH, "//div[@id=\'content\']/div/div/div[2]/div/div/div/div/div/div[4]/div/div[3]/div[2]/form/div/div[2]/div/input").send_keys("123")
    self.driver.find_element(By.XPATH, "//div[@id=\'content\']/div/div/div[2]/div/div/div/div/div/div[4]/div/div[3]/div[2]/form/div[2]/div/div/button/div/div/span").click()
    WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".TextField:nth-child(1) div:nth-child(4)")))
    time.sleep(3)
    assert self.driver.find_element(By.CSS_SELECTOR, ".TextField:nth-child(1) div:nth-child(4)").text == "Invalid login or password"
  

if __name__ == '__main__':
  unittest.main()
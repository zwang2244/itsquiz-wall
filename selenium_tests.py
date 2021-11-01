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
class TestLoginduplicate(unittest.TestCase):
  def setUp(self):
    self.driver = webdriver.Chrome("drivers/chromedriver")
    self.vars = {}
  
  def teardown_method(self):
    self.driver.quit()
  
  def test_loginduplicate(self):
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
    WebDriverWait(self.driver, NaN).until(expected_conditions.presence_of_element_located((By.XPATH, "//form/div/div/div/div[3]")))
    elements = self.driver.find_elements(By.XPATH, "//form/div/div/div/div[3]")
    assert len(elements) > 0
  
if __name__ == '__main__':
  unittest.main()
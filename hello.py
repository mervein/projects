from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

class Oylesine():
   def __init__(self):
       print("öylesine")
class Methods():
   def __init__(self):
       self.driver = webdriver.Chrome(ChromeDriverManager().install())
       self.action = ActionChains(self.driver)
       self.driver.maximize_window()
       self.driver.set_page_load_timeout(10)
       self.driver.get("http://www.amazon.com")
       print("Page is loaded.")
       self.run_all_tests()
   def run_all_tests(self):
       self.login_amazon()
   def login_amazon(self):
       item = self.driver.find_element_by_css_selector("#nav-link-accountList")
       self.action.move_to_element(item).click().perform()
       item = self.driver.find_element_by_css_selector("#ap_email").send_keys("janiya16m_p900z@vcbox.pro")
       item = self.driver.find_element_by_css_selector("#ap_password").send_keys("16m_p900z")
       item = self.driver.find_element_by_css_selector("#signInSubmit")
       self.action.move_to_element(item).click().perform()
       sleep(5)
if  __name__ == "__main__":
   Methods()
   Oylesine()
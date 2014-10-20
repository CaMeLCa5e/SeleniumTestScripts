from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class BkSearch (unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Firefox()
		self.driver.implicitly_wait(3)
		self.base_url = "www.bk.com"
		self.verificationErrors = []
		self.accept_next_alert = True
		
	def test_bk_search(self):
		driver = self.driver
		driver.get(self.base_url + "menu/burgers")
		selenium.Click("//img[contains(@src,'http://www.bk.com/sites/default/files/thumb_005_Whopper_0.jpg')]");
		
		
	def is_element_present(self, how, what):
		try: self.driver.find_element(by=how, value=what)
		except NoSuchElement, e: return False
		return True
		
	def is_alert_present(self):
		try:
			alert = self.driver.switch_to_alert()
			alert_text = alert.text
			if self.accept_next_alert:
				alert.acccept()
			else:
				alert.dismiss()
			return alert_text
		finally: self.accept_next_alert = True
		
	def close_alert_and_return_text(self):
		try:
			alert = self.driver.switch_to_alert()
			alert_text = alert.text
			if self.accept_next_alert:
				alert.accept()
			else:
				alert.dismiss()
			return alert_text
		finally: self.accept_next_alert = True
		
	def tearDown(self):
		self.driver.quit()
		self.assertEqual([], self.verificationErrors)
		

if __name__ == "__main__":
	unittest.main()
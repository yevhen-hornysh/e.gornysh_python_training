# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class add_contact(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver(capabilities={"marionette": False})
        self.wd.implicitly_wait(60)
    
    def test_add_contact(self):
        success = True
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd)
        self.create_contact(wd)
        self.logout(wd)
        self.assertTrue(success)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def create_contact(self, wd, first_name="Eugene", middle_name="Mykolayovich", last_name="Gornysh", nickname="Gorn",
                       title="Title test", company="Company test", address="Address test", home_phone="+123456789",
                       mobile_phone="+123456789", work_phone="+987654321", fax="+654321987", email1="test@test.te",
                       email2="mail@test.te", email3="mail2@test.te", homepage_link="Homepage test",
                       birthday_day="//div[@id='content']/form/select[1]//option[3]",
                       birthday_month="//div[@id='content']/form/select[2]//option[2]", birthday_year="1981",
                       anniversary_day="//div[@id='content']/form/select[3]//option[4]",
                       anniversary_month="//div[@id='content']/form/select[4]//option[3]", anniversary_year="1992",
                       secondary_address="Secondary address", home_phone2="Home test", notes="Notest test"):
        # Click "Add new" - going to creation form
        wd.find_element_by_link_text("add new").click()
        # Fill in general information
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(first_name)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(middle_name)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(last_name)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(nickname)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(title)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(address)
        # Fill in telephones information
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(home_phone)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(mobile_phone)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(work_phone)
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(fax)
        # Fill in emails and other
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(email1)
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(email2)
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(email3)
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(homepage_link)
        if not wd.find_element_by_xpath(birthday_day).is_selected():
            wd.find_element_by_xpath(birthday_day).click()
        if not wd.find_element_by_xpath(birthday_month).is_selected():
            wd.find_element_by_xpath(birthday_month).click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(birthday_year)
        if not wd.find_element_by_xpath(anniversary_day).is_selected():
            wd.find_element_by_xpath(anniversary_day).click()
        if not wd.find_element_by_xpath(anniversary_month).is_selected():
            wd.find_element_by_xpath(anniversary_month).click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(anniversary_year)
        # Fill in secondary information
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(secondary_address)
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(home_phone2)
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(notes)
        # Click Enter (create a contact)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def login(self, wd):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/index.php")

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()

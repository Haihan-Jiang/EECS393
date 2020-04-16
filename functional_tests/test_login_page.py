from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
import time


class TestLoginPage(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome('functional_tests/chromedriver.exe')

    def tearDown(self):
        self.browser.close()

    def test_login_page_is_displayed(self):
        self.browser.get(self.live_server_url)
        alert = self.browser.find_element_by_class_name('login-form')
        self.assertEquals(
            alert.find_element_by_tag_name('p').text,
            'Username:'
        )

    def test_login_button_redirects_to_login(self):
        self.browser.get(self.live_server_url)
        login_url = self.live_server_url + reverse('login')
        self.browser.find_element_by_tag_name('a').click()
        self.assertEquals(
            self.browser.current_url[:-7],
            login_url
        )

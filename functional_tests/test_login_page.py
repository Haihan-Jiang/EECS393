from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
from bookinghub.models import User
import time


class TestPostListPage(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome('functional_tests/chromedriver.exe')

    def tearDown(self):
        self.browser.close()

    def test_no_login_page_alert_is_displayed(self):
        self.browser.get(self.live_server_url)
        # user requests the page for the first time
        alert = self.browser.find_element_by_class_name('login-form')
        self.assertEquals(
            alert.find_element_by_tag_name('h3').text,
            'no login page detected --'
        )
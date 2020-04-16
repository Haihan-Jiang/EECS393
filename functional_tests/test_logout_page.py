from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
import time


class TestLogoutPage(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome('functional_tests/chromedriver.exe')

    def tearDown(self):
        self.browser.close()

    def test_logout_button_redirects_to_logout_page(self):
        self.browser.get(self.live_server_url)
        logout_url = self.live_server_url + reverse('logout')
        self.browser.find_element_by_tag_name('a').click()
        self.assertEquals(
            self.browser.current_url[:-14] + reverse('logout'),
            logout_url
        )
        time.sleep(1)
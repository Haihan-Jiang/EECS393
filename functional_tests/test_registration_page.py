from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
import time


class TestRegistrationPage(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome('functional_tests/chromedriver.exe')

    def tearDown(self):
        self.browser.close()
    
    def test_signup_button_redirects_to_register(self):   
        self.browser.get(self.live_server_url)
        register_url = self.live_server_url + reverse('register')
        self.browser.find_element_by_tag_name('a').click()
        self.assertEquals(
            self.browser.current_url[:-14] + reverse('register'),
            register_url
        )
        time.sleep(1)
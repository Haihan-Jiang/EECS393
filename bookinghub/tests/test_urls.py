from django.test import SimpleTestCase
from django.urls import reverse, resolve
from django.test import Client
from bookinghub.views import user_login


class TestUrls(SimpleTestCase):

    def test_login_url_is_resolved(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func, user_login)

    def test_logout_url_is_resolved(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func, user_login)

# static method should be called in a static context for testing
    def print_status_code(self):
        c = Client()
        response = c.post('/login', {'username': 'EECS393', 'password': 'EECS393'})
        print(response.status_code)
        response = c.get('/reservation')
        response.content


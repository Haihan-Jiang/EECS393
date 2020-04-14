from django.test import SimpleTestCase
from django.urls import reverse, resolve
from bookinghub.views import post_list, user_login, dashboard, reservation, confirmation, register


class TestURLS(SimpleTestCase):

    '''
    def test_login_url_is_resolved(self):
        url = reverse('login')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, LoginView)

    def test_logout_url_is_resolved(self):
        url = reverse('logout')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, LogoutView)
    '''

    def test_dashboard_url_is_resolved(self):
        url = reverse('dashboard')
        print(resolve(url))
        self.assertEquals(resolve(url).func, dashboard)

    def test_reservation_url_is_resolved(self):
        url = reverse('reservation')
        print(resolve(url))
        self.assertEquals(resolve(url).func, reservation)

    def test_confirmation_url_is_resolved(self):
        url = reverse('confirmation')
        print(resolve(url))
        self.assertEquals(resolve(url).func, confirmation)

    def test_register_url_is_resolved(self):
        url = reverse('register')
        print(resolve(url))
        self.assertEquals(resolve(url).func, register)
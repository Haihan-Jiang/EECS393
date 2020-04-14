# views (uses reverse)
from django.test import TestCase, Client
from django.urls import reverse
from bookinghub.models import PublishedManager, Post, User, reservation, room, hotel, hotelStaff
import json


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.login_url = reverse('login')
        self.dashboard_url = reverse('dashboard')
        self.reservation_url = reverse('reservation')
        self.confirmation_url = reverse('confirmation')
        self.register_url = reverse('register')
        '''
    def test_user_login_GET(self):
        client = Client()
        response = self.client.get(self.login_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/login.html')

    def test_dashboard_GET(self):
        client = Client()
        response = self.client.get(self.dashboard_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/dashboard.html')

    def test_reservation(self):
        client = Client()
        response = self.client.get(self.reservation_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/reservation.html')   
        '''

    def test_confirmation(self):
        client = Client()
        response = self.client.get(self.confirmation_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/confirmation.html')

    def test_register(self):
        client = Client()
        response = self.client.get(self.register_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/register.html')
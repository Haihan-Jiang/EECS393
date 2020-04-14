# views (uses reverse)
from django.test import TestCase, Client
from django.urls import reverse
from bookinghub.models import PublishedManager, Post, User, reservation, room, hotel, hotelStaff
import json


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.list_url = reverse('list')
        self.login_url = reverse('login')

    def test_post_list_GET(self):
        client = Client()
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookinghub/post/list.html')

    def test_user_login(self):
        client = Client()
        response = self.client.get(self.login_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/login.html')

    def test_dashboard(self):
        pass

    def test_reservation(self):
        pass

    def test_confirmation(self):
        pass

    def test_register(self):
        pass
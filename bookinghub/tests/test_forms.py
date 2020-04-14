from django.test import SimpleTestCase
from bookinghub.forms import LoginForm, UserRegistrationForm


class TestForms(SimpleTestCase):

    def test_login_form_with_valid_data(self):
        form = LoginForm(data = {
            'username': 'EECS393',
            'password': 'EECS393'
        })
        self.assertTrue(form.is_valid())

    def test_login_form_no_data(self):
        form = LoginForm(data = {})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)

    def test_user_registration_form_with_valid_data(self):
        user_form = UserRegistrationForm(data = {
            'password': 'EECS393',
            'password2': 'EECS393'
        })
        self.assertFalse(user_form.is_valid())

    def test_user_registration_form_no_data(self):
        user_form = UserRegistrationForm(data = {})
        self.assertFalse(user_form.is_valid())
        self.assertEquals(len(user_form.errors), 3)
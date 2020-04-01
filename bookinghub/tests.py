from django.test import TestCase
from whatever.models import Whatever
from django.utils import timezone
from django.core.urlresolvers import reverse
from whatever.forms import WhateverForm

# models test

class WhateverTest(TestCase):

    def create_whatever(self, title="only a test", body="yes, this is only a test"):
        return Whatever.objects.create(title=title, body=body, created_at=timezone.now())

    def test_whatever_creation(self):
        w = self.create_whatever()
        self.assertTrue(isinstance(w, Whatever))
        self.assertEqual(w.__unicode__(), w.title)

    def test_whatever_list_view(self):
        w = self.create_whatever()
        url = reverse("whatever.views.whatever")
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)
        self.assertIn(w.title, resp.content)

    def test_valid_form(self):
        w = Whatever.objects.create(title='Foo', body='Bar')
        data = {'title': w.title, 'body': w.body, }
        form = WhateverForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        w = Whatever.objects.create(title='Foo', body='')
        data = {'title': w.title, 'body': w.body, }
        form = WhateverForm(data=data)
        self.assertFalse(form.is_valid())

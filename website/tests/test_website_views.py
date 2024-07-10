from django.test import TestCase
from django.urls import reverse, resolve
from .record_model_base import RecordModelBase
from website import views


class CRMViewsTest(TestCase, RecordModelBase):

    def test_record_home_views_function_is_correct(self):
        home_view_url = resolve(reverse('crm:home'))
        self.assertIs(home_view_url.func, views.home)

    def test_record_logout_views_function_is_correct(self):
        logout_view_url = resolve(reverse('crm:logout'))
        self.assertIs(logout_view_url.func, views.logout_user)

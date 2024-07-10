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

    def test_record_register_user_views_function_is_correct(self):
        register_view_url = resolve(reverse('crm:register'))
        self.assertIs(register_view_url.func, views.register_user)

    def test_record_customer_records_views_function_is_correct(self):
        customer_records_view_url = resolve(reverse('crm:record', kwargs={'pk': self.record_maker().id}))
        self.assertIs(customer_records_view_url.func, views.customer_records)

    def test_delete_record_records_views_function_is_correct(self):
        delete_record_view_url = resolve(reverse('crm:delete_record', kwargs={'pk': self.record_maker().id}))
        self.assertIs(delete_record_view_url.func, views.delete_record)

    def test_add_record_records_views_function_is_correct(self):
        add_record_view_url = resolve(reverse('crm:add_record'))
        self.assertIs(add_record_view_url.func, views.add_record)

    def test_update_record_records_views_function_is_correct(self):
        update_record_view_url = resolve(reverse('crm:update_record', kwargs={'pk': self.record_maker().id}))
        self.assertIs(update_record_view_url.func, views.update_record)







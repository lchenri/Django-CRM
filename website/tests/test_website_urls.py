from django.test import TestCase
from django.urls import reverse


class WebsiteUrlsTest(TestCase):
    def test_the_pytest_is_ok(self):
        assert 1 == 1

    def test_website_home_url_is_ok(self):
        url = reverse('crm:home')
        self.assertEqual(url, '/',
                         msg="Ocorreu um erro ao obter a URL da home")

    def test_website_logout_url_is_ok(self):
        url = reverse('crm:logout')
        self.assertEqual(url, '/logout/',
                         msg="Ocorreu um erro ao obter a URL de logout")

    def test_website_register_url_is_ok(self):
        url = reverse('crm:register')
        self.assertEqual(url, '/register/',
                         msg="Ocorreu um erro ao obter a URL de registro")

    def test_website_record_url_is_ok(self):
        url = reverse('crm:record', kwargs={'pk': 1})
        self.assertEqual(url, '/record/1',
                         msg="Ocorreu um erro ao obter a URL de record")

    def test_website_add_record_url_is_ok(self):
        url = reverse('crm:add_record')
        self.assertEqual(url, '/add_record/',
                         msg="Ocorreu um erro ao obter a URL de add_record")

    def test_website_delete_record_url_is_ok(self):
        url = reverse('crm:delete_record', kwargs={'pk': 1})
        self.assertEqual(url, '/delete_record/1',
                         msg="Ocorreu um erro ao obter a URL de delete_record")

    def test_website_update_record_url_is_ok(self):
        url = reverse('crm:update_record', kwargs={'pk': 1})
        self.assertEqual(url, '/update_record/1',
                         msg="Ocorreu um erro ao obter a URL de update_record")

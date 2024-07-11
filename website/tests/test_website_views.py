from django.test import TestCase, Client
from django.urls import reverse, resolve
from .record_model_base import RecordModelBase
from django.contrib.auth.models import User
from ..forms import SignUpForm
from website import views
from django.contrib.messages import get_messages


class CRMViewsTest(TestCase, RecordModelBase):

    def test_record_home_views_function_is_correct(self):
        home_view_url = resolve(reverse('crm:home'))
        self.assertIs(home_view_url.func, views.home)

    def test_record_home_loads_correct_template(self):
        response = self.client.get(reverse('crm:home'))
        self.assertTemplateUsed(response, 'website/pages/home.html')

    def test_record_home_views_if_post(self):
        client = Client()
        user = User.objects.create_user(username='testuser', password='208090sol')
        url = reverse('crm:home')

        response = client.post(url, {
            'username': 'testuser',
            'password': '208090sol',
        })

        self.assertIn('_auth_user_id', client.session)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0].message), "Logado com sucesso!.")
        self.assertRedirects(response, url)

    def test_record_home_views_if_user_is_not_none(self):
        self.client = Client()
        self.user = User.objects.create_user(username='teste', password='208030Pl@')
        response = self.client.post(reverse('crm:home'), {
            'username': 'teste293',
            'password': '283019lp@',
        })

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0].message), "Usuário ou senha inválidos.")
        self.assertRedirects(response, reverse('crm:home'))

    def test_record_logout_views_function_is_correct(self):
        logout_view_url = resolve(reverse('crm:logout'))
        self.assertIs(logout_view_url.func, views.logout_user)

    def test_record_register_user_loads_correct_template(self):
        response = self.client.get(reverse('crm:register'))
        self.assertTemplateUsed(response, 'website/pages/register.html')

    def test_record_register_user_views_if_post(self):
        self.client = Client()
        form_data_sign_up_form = {
            'username': 'testuser',
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john@doe.com',
            'password1': '208030Pl@',
            'password2': '208030Pl@'
        }
        #form = SignUpForm(form_data_sign_up_form)
        #form.full_clean()
        #form.save()

        response = self.client.post(reverse('crm:register'), form_data_sign_up_form)
        self.assertTrue(User.objects.filter(username='testuser').exists())
        user = User.objects.get(username='testuser')
        self.assertEqual(int(self.client.session['_auth_user_id']), user.id)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0].message), "Você foi cadastrado com sucesso.")
        self.assertRedirects(response, reverse('crm:home'))

    def test_record_register_user_views_if_form_is_not_valid(self):
        self.client = Client()
        form_data_sign_up_form = {}
        response = self.client.post(reverse('crm:register'), form_data_sign_up_form)
        self.assertTemplateUsed(response, 'website/pages/register.html')

    def test_record_logout_user_is_working(self):
        response = self.client.get(reverse('crm:logout'))
        self.assertNotIn('_auth_user_id', self.client.session)

        msg_expected = "Você saiu."
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(messages[0].message, msg_expected)
        self.assertRedirects(response, reverse('crm:home'))

    def test_record_register_user_views_function_is_correct(self):
        register_view_url = resolve(reverse('crm:register'))
        self.assertIs(register_view_url.func, views.register_user)

    def test_record_customer_records_views_function_is_correct(self):
        customer_records_view_url = resolve(reverse('crm:record', kwargs={'pk': self.record_maker().id}))
        self.assertIs(customer_records_view_url.func, views.customer_records)

    def test_record_customer_views_if_request_user_is_authenticated(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='208030Pl@')
        self.client.login(username='testuser', password='208030Pl@')
        response = self.client.get(reverse('crm:record', kwargs={'pk': self.record_maker().id}))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'João Ternário')

    def test_record_customer_views_if_request_user_is_not_authenticated(self):
        self.client = Client()

        response = self.client.get(reverse('crm:record', kwargs={'pk': self.record_maker().id}))

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), "Você deve estar logado para visualizar esta página.")
        self.assertRedirects(response, reverse('crm:home'))

    def test_delete_record_records_views_function_is_correct(self):
        delete_record_view_url = resolve(reverse('crm:delete_record', kwargs={'pk': self.record_maker().id}))
        self.assertIs(delete_record_view_url.func, views.delete_record)

    def test_add_record_records_views_function_is_correct(self):
        add_record_view_url = resolve(reverse('crm:add_record'))
        self.assertIs(add_record_view_url.func, views.add_record)

    def test_update_record_records_views_function_is_correct(self):
        update_record_view_url = resolve(reverse('crm:update_record', kwargs={'pk': self.record_maker().id}))
        self.assertIs(update_record_view_url.func, views.update_record)

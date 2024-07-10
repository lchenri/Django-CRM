from django.test import TestCase
from .record_model_base import RecordModelBase




class WebSiteModelTest(TestCase, RecordModelBase):
    def setUp(self):
        self.record = self.record_maker()
        return super().setUp()

    def test_website_record_model_string_representation(self):
        needed = "João Ternário"
        self.assertEqual(
            str(self.record), needed,
            msg=f"Representação da string do modelo deveria ser {needed} porém está como {self.record}"
        )
from ..models import Record
from django.test import TestCase


class WebSiteModelTest(TestCase):
    def setUp(self):
        self.record = self.record_maker()
        return super().setUp()

    def record_maker(self):
        record = Record.objects.create(
            first_name="João",
            last_name="Ternário",
            email="joao@ternario.com",
            phone="32999990000",
            address="rua abacateira, 22",
            city="Jardim das Glórias",
            state="Minas Gerais",
            zipcode="36000001"
        )
        return record

    def test_website_record_model_string_representation(self):
        needed = "João Ternário"
        self.assertEqual(
            str(self.record), needed,
            msg=f"Representação da string do modelo deveria ser {needed} porém está como {self.record}"
        )
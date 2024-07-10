from ..models import Record


class RecordModelBase:
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
import factory

from notepad.models.note import Note
from faker import Faker


class NoteFactory(factory.DjangoModelFactory):
    content = factory.LazyAttribute(lambda t: f'Note {t}: {Faker().text(20)}')


    # to tell Pycharm the type of created object.
    def __new__(cls, *args, **kwargs) -> Note:
        return super().__new__(*args, **kwargs)

    class Meta:
        model = Note

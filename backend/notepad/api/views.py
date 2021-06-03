from rest_framework.viewsets import ModelViewSet

from notepad.api.note.serializers.note import NoteSerializer
from notepad.models.note import Note


class NoteViewSet(ModelViewSet):
    queryset = Note.objects.order_by('id')
    serializer_class = NoteSerializer

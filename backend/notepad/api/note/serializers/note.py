from rest_framework import serializers

from notepad.models.note import Note


class NoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Note
        fields = [
            'id',
            'content',
        ]


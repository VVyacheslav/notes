from django.contrib import admin

from notepad.models.note import Note


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    """Project admin"""
    fields = ('id', 'content')
    list_display = ('id', 'content')


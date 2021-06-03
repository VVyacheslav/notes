<template>
  <div id="app">
    <NoteList :notes="notes" @add-note="addNote"/>
  </div>
</template>

<script>

import NoteList from "./components/NoteList";

export default {
  name: 'Globaldots-testwork',
  components: {NoteList},
  data() {
    return {
      notes: [],
    }
  },
  methods: {
    async addNote(content) {
      if (!content) {
        return
      }
      let newNote = this.createNote(content);
      const error = await this.sendNoteToServer(content);
      this.removeNewNoteIfSendingFailed(error, newNote);
      this.newNoteContent = ''
    },
    createNote(content) {
      const newNote = {
        id: '',
        content: content,
      };
      this.notes.push(newNote)
      return newNote;
    },

    async sendNoteToServer(content) {
      const [error,] = await this.$api.notes.add({content})
      return error;
    },

    removeNewNoteIfSendingFailed(error, newNote) {
      if (error) {
        var index = this.notes.indexOf(newNote);
        if (index !== -1) {
          this.notes.splice(index, 1);
        }
      }
    },

    addNote1: function (event) {
      // `event`  нативное событие DOM
      if (event) {
        alert(event.target.tagName)
      }
    }
  },
  async created() {
    const [error, loadedNotes] = await this.$api.notes.get();
    if (!error) {
      this.notes = loadedNotes;
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>

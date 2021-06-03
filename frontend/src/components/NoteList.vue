<template>
  <div id="note-list">
    <form @submit.prevent="onSubmit">
      <h1>Add Note</h1>
      <textarea
          class="textarea"
          id="new-note"
          v-model="newNoteContent"
          rows="5"
          placeholder="Put note in here..."
      />
      <div>
        <button class="button">Add</button>
      </div>
    </form>
    <ul class="notes__list">
      <li
          is="NoteItem"
          v-for="(note, index) in notes"
          :key="`${index}-note`"
          :note="note"
      >
      </li>
    </ul>
  </div>
</template>

<script>

import NoteItem from "./NoteItem";

export default {
  components: {NoteItem},
  props: {
    notes: {
      type: Array,
    },
  },
  data() {
    return {
      newNoteContent: ''
    }
  },
  methods: {
    onSubmit() {
      this.$emit('add-note', this.newNoteContent)
      this.newNoteContent = ''
    }
  },
}
</script>

<style scoped>
.notes__list {
  margin-left: auto;
  margin-right: auto;
  list-style-type: none; /* Remove bullets */
  padding: 0;
  width: 100%;
  max-width: 40rem;
}

.notes__item:nth-child(odd) {
  background: #f9f9f9;
}

.notes__item:hover {
  background: #ddd;
}

.textarea {
  width: 100%;
  max-width: 40rem;
  padding: 0.75rem 1rem;
  box-sizing: border-box;
  font-size: 0.875rem;
}

.button {
  border-radius: 0.25rem;
  cursor: pointer;
  height: 1.875rem;
  width: 5rem;
}


</style>

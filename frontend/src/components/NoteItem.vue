<template>
  <li class="notes__item">
    {{ note.content }}
  </li>
</template>

<script>
export default {
  props: {
    note: {type: Object, required: true},
  },
}
</script>

<style scoped>
.notes__item {
  padding: 12px 8px 12px 40px;
  background: #eee;
  font-size: 18px;
}


</style>

<template>
  <div v-if="showCommentaar" class="modal-overlay" v-on:click.self="closeModal">
    <div class="modal-window">
      <h2>Commentaar</h2>
      <p>{{ message }}</p>
      <button @click="closeModal">Close</button>
    </div>
  </div>
</template>

<script>
import '/src/app.css';
export default {
  name: 'MyModal',
  props: ['message'],
  data() {
    return {
      showCommentaar: false,
    };
  },
  methods: {
    toggleModal() {
      this.showCommentaar = !this.showCommentaar;
      document.body.classList.toggle("open-modal");
    },
    closeModal() {
      this.showCommentaar = false;
      document.body.classList.remove("open-modal");
    },
  }
};
</script>
<template>
  <v-container>
    <div v-if="isTokenValid">
      <h1>Welcome</h1>
      <p>Name: {{ firstName }} {{ lastName }}</p>
      <p>Email: {{ email }}</p>
      <v-btn>Face Login Enroll</v-btn>
      <v-btn @click="logout">Logout</v-btn>
    </div>
    <div v-else>Redirecting .....</div>
  </v-container>
</template>

<script>
import { isTokenValid } from '../auth';

export default {
  data() {
    return {
      firstName: '',
      lastName: '',
      email: '',
    };
  },
  computed: {
    isTokenValid() {
      return isTokenValid();
    },
  },
  watch: {
    isTokenValid(value) {
      if (!value) {
        this.$router.push('/');
      }
    },
  },
  mounted() {
    if (this.isTokenValid) {
      const firstName = localStorage.getItem('userFirstName');
      const lastName = localStorage.getItem('userLastName');
      const email = localStorage.getItem('userEmail');
      this.firstName = firstName ? JSON.parse(firstName) : '';
      this.lastName = lastName ? JSON.parse(lastName) : '';
      this.email = lastName ? JSON.parse(email) : '';
    } else {
      this.$router.push('/');
    }
  },
  methods: {
    logout() {
      localStorage.removeItem('token');
      localStorage.removeItem('userFirstName');
      localStorage.removeItem('userLastName');
      localStorage.removeItem('userEmail');
      this.$router.push('/');
    },
  },
};
</script>

<style scoped></style>

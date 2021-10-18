<template>
  <div id="app" class="app">
    <!-- <div class="header">
      <h1>ssacg | galería</h1>

      <nav>
        <button v-if="is_auth">Home</button>
        <button v-if="is_auth">Account</button>
        <button v-if="is_auth">Log out</button>
        <button v-on:click="loadSignUp" v-if="!is_auth">Sign up</button>
      </nav>
    </div> -->

    <div class="main-component">
      <router-view
        v-on:completedLogIn="completedLogIn"
        v-on:completedSignUp="completedSignUp"
        v-on:back2login="back2login"
      >
      </router-view>
    </div>
  </div>
</template>

<script>
import * as strings from "@/strings";

export default {
  name: "App",

  data: function() {
    return {
      is_auth: false,
    };
  },

  components: {},
  methods: {
    verifyAuth: function() {
      if (this.is_auth == false) this.$router.push({ name: "logIn" });
    },

    loadLogIn: function() {
      this.$router.push({ name: "logIn" });
    },

    loadSignUp: function() {
      this.$router.push({ name: "signUp" });
    },

    completedLogIn: function(data) {
      alert("completed log in!");
      this.is_auth = true;
      document.title = strings.pagetitle.main;
    },
    completedSignUp: function(data) {
      alert("succesfully signup");
    },
    back2login: function() {
      
    }
  },
  created: function() {
    this.verifyAuth();
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  background-color:  black;
}


.header {
  /* margin: 0; */
  padding: 0 15px 0 15px;
  /* width: 100%; */
  height: 7vh;
  /* min-height: 100px; */
  margin: 5px;
  background-color: rgba(0, 0, 0, 0);
  border: 1px solid black;
  border-radius: 15px;


  color: white;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

/* .header h1 {
  width: 20%;
  text-align: center;
}  */
</style>

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
    <header>
      <div class="header">
        <img
          style="border-radius: 10px; height: 60px"
          src="./assets/logo-ssacg-singleline.png"
          alt=""
        />
        <nav class="nav">
          <button @click="loadMainPage()">Inicio</button>
          <button @click="loadCategoriesSectionInMainPage()">Categorías</button>
          <button v-if="!is_auth" @click="loadLogIn()">Iniciar Sesión</button>
          <button v-if="!is_auth" @click="loadSignUp()">Registrarse</button>
        </nav>
      </div>
    </header>

    <div class="main-component">
      <router-view
        v-on:completedLogIn="completedLogIn"
        v-on:completedSignUp="completedSignUp"
        v-on:alreadyLogged="alreadyLogged"
        v-on:verifyAuth="verifyAuth"
        v-on:back2login="back2login"
        v-on:logOut="logOut"
      >
      </router-view>
    </div>
    <footer>
      <div class="info-links">
        <a href="#">nosotros</a>
        <a href="#">contacto</a>
      </div>
      <div class="brand">
        <strong>ssacg | galería</strong>
      </div>
      <div class="footer-social-networks">
        <a href="https://www.facebook.com/"> <i class="bi bi-facebook"></i></a>
        <a href="https://www.instagram.com/">
          <i class="bi bi-instagram"></i
        ></a>
        <a href="https://www.twitter.com/"> <i class="bi bi-twitter"></i></a>
        <a href="https://www.whatsapp.com/"> <i class="bi bi-whatsapp"></i></a>
      </div>
    </footer>
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
    
    // footer buttons listeners-start
    loadMainPage: function() {
      this.$router.push({ name: "mainPage" });
      window.scroll(0, 0);
    },

    loadCategoriesSectionInMainPage: function() {
      this.$router.push({
        name: "mainPage",
        params: { toCategoriesSection: "true" },
      });
      window.scrollTo(window.scrollX, window.scrollY + 650);
    },

    loadLogIn: function() {
      this.$router.push({ name: "logIn" });
    },

    loadSignUp: function() {
      this.$router.push({ name: "signUp" });
    },

    // footer buttons listeners-end

    logOut: function() {
      localStorage.clear();
      this.verifyAuth();
    },
    verifyAuth: function() {
      this.is_auth = localStorage.getItem("isAuth") || false;

      if (this.is_auth == false) this.$router.push({ name: "logIn" });
      else
        this.$router.push({
          name: "products",
          params: { tokenStr: localStorage.getItem("token_access") },
        });
    },

    alreadyLogged: function() {
      this.$router.push({
        name: "products",
        params: { tokenStr: localStorage.getItem("token_access") },
      });
    },

    completedLogIn: function(data) {
      localStorage.setItem("token_refresh", data.token_refresh);
      localStorage.setItem("token_access", data.token_access);
      localStorage.setItem("isAuth", true);
      this.is_auth = true;
      this.$router.push({
        name: "products",
        params: { email: data.email, tokenStr: data.token_access },
      });
    },

    back2login: function() {
      this.$router.push({ name: "logIn" });
    },
  },
  created: function() {
    // this.verifyAuth();
    this.loadMainPage();
  },
};
</script>

<style scoped>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /* text-align: center; 
  color: #2c3e50;
  background-color:  black; */
  /* height: 100%; */
}
/* header start */
.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 5px 5px 5px 5px;
  background-color: black;
  border-bottom: 1px solid white;

  width: 100%;
  top: 0;
  left: 0;
  position: fixed;
  z-index: 950;
}

.nav {
  display: flex;
  justify-content: space-evenly;
}

.nav button {
  color: rgb(235, 231, 231);
  background-color: black;
  margin: auto 10px auto 10px;

  border: 0;
  border-radius: 5px;
  cursor: pointer;
  text-align: center;

}
/* header end */
/* --- footer start ---*/
.brand {
  font-size: 20px;
}

.info-links a {
  color: white;
  margin: auto 15px auto 5px;
}
i {
  margin: auto 10px auto 10px;
  font-size: 2rem;
  color: white;
}
footer {
  font-family: Arial, Helvetica, sans-serif;
  font-size: 13px;
  align-items: center;
  text-align: center;
  display: flex;
  justify-content: space-evenly;

  color: rgb(235, 231, 231);
  padding: 25px 5px 25px 5px;
  background-color: black;

  width: 100%;
  bottom: 0;
  left: 0;
}

/* --- footer end --- */
.hedader {
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
</style>

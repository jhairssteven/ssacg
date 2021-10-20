<template>
  <div class="container">
    <div class="login-page">
      <table>
        <tr>
          <td>
            <img
              class="logo"
              src="../assets/logo-anillo-ssacg-multicolor.png"
              alt="logo"
            />
          </td>
          <td style="padding: 0vw 0vw 0vw 18.5vw;">
            <table>
              <tr>
                <td>
                  <form v-on:submit.prevent="processLogInUser">
                    <input
                      class="field-input"
                      placeholder="Correo..."
                      type="text"
                      v-model="user.email"
                    /><br />
                    <input
                      class="field-input"
                      placeholder="Contraseña..."
                      type="password"
                      v-model="user.password"
                    /><br />
                    <button class="login-btn" type="submit">Ingresar</button>
                    <br /><p class="alert-msg">{{ alert_msg }}</p> <br />
                    <button class="signup-btn" v-on:click="loadSignUp">
                      Registrarse
                    </button>
                  </form>
                </td>
              </tr>
            </table>
          </td>
        </tr>
      </table>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import * as strings from "@/strings";

export default {
  name: "logIn",

  data: function() {
    return {
      alert_msg: "",
      user: {
        email: "",
        password: "",
      },
    };
  },

  methods: {
    processLogInUser: function() {
      axios.get(strings.URLs.existsEmail + this.user.email + "/")
      .then((response) => {
            axios.post(strings.URLs.logIn, this.user, { headers: {} })
            .then((result) => {
              let dataLogIn = {
                token_access: result.data.access,
                token_refresh: result.data.refresh,
              };
              this.alert_msg = ""
              this.$emit("completedLogIn", dataLogIn);
            })
            .catch((error) => {
              if (error.response.status == "401")
                // alert("ERROR 401: Unauthorized, incorrect credentials maybe!");
                this.alert_msg = "¡Contraseña incorrecta!"
            });
      })
      .catch((error) => {
        if(error.response.status == "404") {
          this.alert_msg = "!Este correo no está registrado!"
        }
      });
    },

    loadSignUp: function() {
      this.$router.push({ name: "signUp" });
    },
  },

  created: function() {
    document.title = strings.pagetitle.logIn;
    if(localStorage.getItem("isAuth") || false)
      this.$emit("alreadyLogged");
  },
};
</script>

<style>
.login-page {
  margin-top: 25vh;
  display: flex;
  justify-content: center;
}

* {
  font-family: Verdana, Geneva, Tahoma, sans-serif;
}
.logo {
  border-radius: 25px;
}

.field-input {
  width: 225px;
  margin: 1px 1px 15px 1px;
  padding: 10px 15px 10px 15px;
  border-radius: 5px;
  border: 0.25px solid rgb(163, 163, 163);
}

.field-input:focus {
  box-shadow: 0px 0px 8px rgb(199, 196, 196);
  outline: none;
}

button {
  border: 0;
  border-radius: 5px;
  cursor: pointer;
  text-align: center;
}

.login-btn {
  width: 255px;
  padding: 10px 1px 10px 1px;
  margin: 25px auto 10px auto;
  background-color: #4384f4; /* 4384F4*/
  color: white;
}

.login-btn:hover {
  background-color: #3b77df;
}

.login-btn:active {
  background-color: #356ac7;
}
.signup-btn {
  width: 120px;
  padding: 7px 1px 7px 1px;
  background-color: #ffa093; /* F89E90 */
  color: black;
}
.signup-btn:hover {
  background-color: #f1968a;
}
.signup-btn:active {
  background-color: #e48f83;
}

</style>

<template>
  <div class="page-container">
        <!-- <table>
            <tr>
                <td><img class="logo" src="../assets/logo-anillo-ssacg-multicolor.png" alt=""></td>
                <td style="padding: 0vw 0vw 0vw 18.5vw;"> -->
                    <table style="margin-bottom: 4vh">
                        <tr><td>
                            <form v-on:submit.prevent="processSignUpUser">
                                <input class="field-input" v-model="user.name" type="text" placeholder="Nombre de usuario"><br>
                                <!-- <div class="field-input-required"> -->
                                    <input class="field-input" v-model="user.email" type="text" placeholder="Correo"><br>
                                    <input class="field-input" v-model="user.password" type="password" placeholder="Contraseña"><br>
                                    <input class="field-input" v-model="checkPass" type="password" placeholder="Confirmar contraseña"><br>
                                <!-- </div> -->
                                <p class="alert-msg">{{alert_msg}}</p>
                                <button class="signup-btn-signup-page">Crear cuenta</button><br>
                                <router-link class="i-have-account" :to="{name: 'logIn'}">Ya tengo una cuenta</router-link>
                            </form>
                        </td></tr>                        
                    </table>
                <!-- </td>
            </tr>
        </table> -->
    </div>
</template>

<script>
    import axios from "axios";
    import * as strings from "@/strings"

    export default {
        name: "signUp",
        data: function() {
            return {
                alert_msg: "",
                user: {
                    name: "",
                    email: "",
                    password: "",
                },
                checkPass: "",
            };
        },
        methods: {
            processSignUpUser: function () {
                if(this.user.password == "" || this.user.email == "" || this.user.name == ""){
                    this.alert_msg = "Usuario, correo y contraseña son campos obligatorios";
                } else {
                    if (this.checkPass != this.user.password)
                        this.alert_msg = "¡Las contraseñas no coinciden!";
                    else {
                        axios.get(strings.URLs.existsEmail + this.user.email + "/")
                        .then((response) => {
                            // OK response, email exists, can't sign up
                            this.alert_msg = "¡Este correo se encuentra en uso!";
                        })
                        .catch((error1) => {
                            if(error1.response.status == "404") {
                                // 404 response, email isn't registered, can sign up with given on
                                axios.post(strings.URLs.signUpAdmin, this.user, { headers: {}})
                                .then((result) => {
                                    let dataSignUp = {
                                        token_acess: result.data.access,
                                        token_refresh: result.data.refresh
                                    };
                                    // this.$emit("completedSignUp", dataSignUp);
                                    alert("succesfully signup");
                                    this.$router.push({name: "logIn"});
                                }).catch((error) => {
                                        alert("Unkown error:\n"
                                            + JSON.stringify(error.response.data))
                                });
                            }
                        })   
                    }
                }
            }, 
            back2login: function () {
                // this.$router.push({name: 'logIn'})
                this.$emit("back2login");
            }
        },
        created: function() {
            document.title = strings.pagetitle.signUp;
        }
    };
</script>

<style scoped>
.i-have-account {
    width: 15vw;
    margin-left: 5vw;
    text-align: center;

    white-space: normal;
    word-wrap: break-word;
}

.page-container {
    margin-top: 25vh;
    margin-bottom: 12.5vh;
    display: flex;
    justify-content: center;
}

.logo {
  border-radius: 25px;
}
.field-input {
  width: 20vw;
  margin: 1px 1px 15px 1px;
  padding: 10px 15px 10px 15px;
  border-radius: 5px;
  border: 0.25px solid rgb(163, 163, 163);
}

.field-input:focus {
  box-shadow: 0px 0px 8px rgb(199, 196, 196);
  outline: none;
}

a {
    color: blue;
    font-size: 15px;
}

button {
    width: 20vw;
    border: 0;
    border-radius: 5px;
    cursor: pointer;
    text-align: center;
}

.signup-btn-signup-page {

  padding: 10px 1px 10px 1px;
  margin: 25px auto 5px auto;
  background-color: #ffa093; /* F89E90 */
  color: black;

  
}
.signup-btn-signup-page:hover {
  background-color: #f1968a;
}
.signup-btn-signup-page:active {
  background-color: #e48f83;
}



</style>
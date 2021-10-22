<template>
  <div class="page-container">
        <table>
            <tr>
                <td><img class="logo" src="../assets/logo-anillo-ssacg-multicolor.png" alt=""></td>
                <td style="padding: 0vw 0vw 0vw 18.5vw;">
                    <table>
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
                                <a href="" v-on:click="back2login">Ya tengo una cuenta</a>
                            </form>
                        </td></tr>                        
                    </table>
                </td>
            </tr>
        </table>
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
                                    this.$emit("completedSignUp", dataSignUp);
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

<style>
.page-container {
    margin-top: 25vh;
    display: flex;
    justify-content: center;
}

.logo {
  border-radius: 25px;
}

.field-input {
    margin: 1px 1px 15px 1px;
}



a {
    color: blue;
    font-size: 15px;
}

.signup-btn-signup-page {
  width: 255px;
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
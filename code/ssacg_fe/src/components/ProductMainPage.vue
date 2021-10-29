<template>
  <div class="product-page-container">
    <section id="main-content">
      <article>
        <header>
          <h1>
            <br />
            {{ this.product.name }}
          </h1>
        </header>

        <div class="content">
          <div id="columnaImagen" class="col col1">
            <img
              :src="product.img_src"
              :alt="product.category + ':' + product.name"
            />
          </div>
          <div id="columnaTexto">
            <div class="infromacion">
              <!-- <div id="precio" class="col">
                <table border="0">
                  <tr>
                    <td>Precio:</td>
                    <td><input type="text" name="precioProducto" :placeholder="product.price"/></td>
                  </tr>
                  <tr>
                    <td>Stock:</td>
                    <td><input type="text" name="cantidadProducto" :placeholder="product.stock"/></td>
                  </tr>
                </table>
              </div> -->
              <div id="descripcion" class="col">
                <h3>Descripción</h3>
                <p>
                  {{this.product.description}}
                </p>
              </div>
              <div id="botones" class="col">
                <!-- <button class="bt">Publicar</button>
                <button class="bt">Cancelar</button> -->
              </div>
            </div>
          </div>
        </div>
      </article>
      <!-- /article -->
    </section>
    <!-- / #main-content -->
  </div>
</template>

<script>
import * as strings from "@/strings";
import axios from "axios";

export default {
  name: "productMainPage",

  data: function() {
    return {
      product_category: this.$route.params.category,
      product_id: this.$route.params.pid,
      product: {
        id:             "Not found",
        img_src:        "Not found",
        category:       "Not found",
        name:           "Not found",
        price:          "0.0",
        stock:          "0",
        description:    "Not found"
      },
    };
  },

  methods: {
    getProductData: async function(id) {
        axios.get(strings.URLs.get1Product + this.product_id + "/", {headers: {}})
        .then((result) => {
            this.product = {
                id:             result.data.id_product,
                // img_src:        "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ec/Mona_Lisa%2C_by_Leonardo_da_Vinci%2C_from_C2RMF_retouched.jpg/300px-Mona_Lisa%2C_by_Leonardo_da_Vinci%2C_from_C2RMF_retouched.jpg",
                img_src:        result.data.img_src,
                category:       result.data.category,
                name:           result.data.name,
                price:          result.data.unitary_price,
                stock:          result.data.stock,
                description:    result.data.description
            }
        })
        .catch((error) => {
            console.log(error, errorCodeLocationStr)
            alert("Error interno, ingresa nuevamente");
            // this.$router.push({name: "mainPage"});
        });
    },
    toStr(product) {
      return JSON.stringify(this.product);
    },
  },

  created: async function() {
    await this.getProductData(this.$route.params.pid);
  },
};
</script>

<style scoped>
.product-page-container {
  margin: 0;
  padding: 0;
  font-family: Helvetica, Arial, sans-serif;
  color: #666;
  font-size: 1em;
  line-height: 1.5em;
  background-image: url("../assets/fondo.jpg");
  background-attachment: fixed;
}

h1 {
  font-size: 2.3em;
  line-height: 1.3em;
  margin: 15px 0;
  text-align: center;
  font-weight: 300;
}
h2 {
  font-size: 1.5em;
  line-height: 1.3em;
  margin: 1px 0;
  text-align: center;
  font-weight: bolder;
  color: #666666;
}
h3 {
  color: #666666;
}
p {
  margin: 0 0 1.5em 0;
}
img {
  max-width: 315px;
  height: 450px;
}
#main-header {
  background: rgb(2, 2, 2);
  color: white;
  height: 80px;
  width: 100%; /* hacemos que la cabecera ocupe el ancho completo de la página */
  left: 0; /* Posicionamos la cabecera al lado izquierdo */
  top: 0; /* Posicionamos la cabecera pegada arriba */
  position: fixed; /* Hacemos que la cabecera tenga una posición fija */
}
#main-header a {
  color: white;
}
nav {
  float: right;
}
nav ul {
  margin: 0;
  padding: 0;
  list-style: none;
  padding-right: 20px;
}

nav ul li {
  display: inline-block;
  line-height: 80px;
}

nav ul li a {
  display: block;
  padding: 0 10px;
  text-decoration: none;
}
nav ul li a:hover {
  background: #0b76a6;
}

#main-content {
  background: white;
  width: 90%;
  max-width: 800px;
  margin: 20px auto;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}
.content {
  color: black;
  padding: 0;
  margin: 0;
  overflow: hidden;
  display: inline-flex;
  vertical-align: top;
  background-color: white;
}
#columnaImagen,
#columnaTexto {
  width: 50%;
}
#precio,
#descripcion {
  width: auto;
  margin-left: 85px;
}

.col {
  padding: 1em;
  text-align: justify;
}
#main-content header {
  padding: 40px 40px 0 40px;
}
#main-content .content {
  padding: 5px 40px 40px 40px;
}
#botones {
  text-align: center;
  width: auto;
}
.bt {
  width: 133px;
  margin: 0 10;
  height: 30px;
}

#main-footer {
  background: black;
  color: white;
  text-align: center;
  padding: 20px;
  margin-top: 40px;
}
#main-footer p {
  margin: 0;
}

#main-footer a {
  color: white;
}
</style>

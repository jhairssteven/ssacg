<template>
  <div class="product-list-by-cat" id="product-list-by-cat">
    <header>
      <div class="header">
        <img
          style="border-radius: 10px; height: 60px"
          src="../assets/logo-ssacg-singleline.png"
          alt=""
        />
        <nav class="nav">
          <button>Inicio</button>
          <button>Categorías</button>
          <button>Iniciar Sesión</button>
          <button>Registrarse</button>
        </nav>
      </div>
    </header>
    <div class="category-title">
      <h1>{{ product_category }}</h1>
    </div>
    <div class="container">
      <table class="table table-fluid" id="myTable">
        <thead style="display: none;">
          <!-- keeping headers but hidden to keep datatable properties -->
          <tr>
            <th>col1</th>
            <th>col2</th>
          </tr>
        </thead>
        <tbody>
          <!-- <tr v-for="(product, k) in product_list" :key="k"> -->
          <tr v-for="k in [...product_list].map((_,i)=>i).filter(i=>i%2===0)" :key="k">
                <td>
                    <div class="product-container">
                        <div class="image">
                            <a :href="`${pageDomain}${product_list[k].category}/product/${product_list[k].id}`">
                            <!-- <a v-on:click.prevent="changePage()" v-bind:href="href_link"> -->
                                <img
                                    class="image__img"
                                    :src="product_list[k].img_src"
                                    :alt="product_list[k].img_alt_txt"
                                />

                                <div class="image__overlay image__overlay--blur">
                                    <div class="product__title">
                                        {{product_list[k].title}}
                                    </div>
                                    <p class="product__price">
                                        {{formatPrice(product_list[k].unitary_price)}}
                                    </p>
                                </div>
                            </a>
                        </div>
                    </div>
                </td>
                <div v-if="product_list[k+1]">
                    {{this.set_second_colum_index(k + 1)}}
                </div>
                <div v-else>
                    {{this.set_second_colum_index(0)}}
                </div>
                <td>
                    <div class="product-container">
                        <div class="image">
                        <a :href="`${pageDomain}${product_list[second_colum_index].category}/product/${product_list[second_colum_index].id}`">
                            <img
                            class="image__img"
                            :src="product_list[second_colum_index].img_src"
                            :alt="product_list[second_colum_index].img_alt_txt"
                            />

                            <div class="image__overlay image__overlay--blur">
                            <div class="product__title">
                                {{ product_list[second_colum_index].title }}
                            </div>
                            <p class="product__price">
                                {{ formatPrice(product_list[second_colum_index].unitary_price) }}
                            </p>
                            </div>
                        </a>
                        </div>
                    </div>
                </td>
          </tr>
        </tbody>
      </table>
    </div>
    <div class="main-component">
      <router-view
        v-on:changePage="changePage"
      >
      </router-view>

  </div>
  </div>
</template>

<script>
import * as strings from "@/strings";
import axios from "axios";

// this.$router.push({name: "productMainPage", params: {category: "catt", pid: "11"}});
export default {
    name: "productListByCat",
  
  components: {},
  data: function() {
    return {
      pageDomain: strings.URLs.frontIndex,
      href_link: "",
      second_colum_index: 1,
      // product_category: "Nombre de la categoría",
      product_category: this.$route.params.category,
      product_list: [],
    };
  },

  mounted() {
    this.product_table_config();
  },

  methods: {
    changePafge: function() {
        this.$router.push({name: "logIn"});
    },
    set_second_colum_index: function (index) {
        this.second_colum_index = index;
    },
    formatPrice: function(value) {
      let val = "$ " + (value / 1).toFixed(2).replace(".", ",");
      return val.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ".");
    },
    product_table_config: function() {
      this.$nextTick(function() {
        $("#myTable").DataTable({
          searching: false,
          lengthChange: false,
          pageLength: 5, //number of rows to show per-table page
          language: {
            decimal: "",
            emptyTable: "No hay datos disponibles para la tabla",
            info: "Mostrando _START_ a _END_ de _TOTAL_ filas",
            infoEmpty: "Mostrando 0 a 0 de 0 filas",
            infoFiltered: "(Obtenido de _MAX_ filas totales)",
            infoPostFix: "",
            thousands: ",",
            lengthMenu: "Número de filas _MENU_",
            loadingRecords: "Cargando...",
            processing: "Procesando...",
            search: "Buscar:",
            zeroRecords: "No se encontraron registros coincidentes",
            paginate: {
              first: "Primero",
              last: "Último",
              next: "Siguiente",
              previous: "Anterior",
            },
            aria: {
              sortAscending: ": Organizar columna ascendente",
              sortDescending: ": Organizar columna descendente",
            },
          },
        });
      });
    },

    getAllProducts: async function() {
            // await this.checkIfLogged();
            let allProducts_list;
            axios.get(strings.URLs.getAllProducts, {headers: {}})
              .then((result) => {
                  for (let i = 0; i < result.data.length; i++) {
                    if(result.data[i].category == this.product_category) {
                      this.product_list.push(
                          {
                            id:             result.data[i].id_product,
                            img_src:        result.data[i].img_src,
                            // img_src:        "https://www.freeiconspng.com/uploads/no-image-icon-6.png",
                            img_alt_txt:    result.data[i].name,
                            category:       result.data[i].category,
                            title:          result.data[i].name,
                            unitary_price:  result.data[i].unitary_price,
                            // stock:          result.data[i].stock,
                            // description:    result.data[i].description
                          }
                      );
                    }
                    console.log(JSON.stringify(this.product_list));
                  }
              })
              .catch((error) => {
                  this.parseErrorForTokens(error, "error in getallproducts()")
              });
            
        },

  },
  created: async function() {
    this.getAllProducts();
  },
};
</script>

<style scoped>

.category-title h1 {
  margin: 30px 30px 30px 30px;
  text-align: center;
}
/* ---single-product-card-start-- */
.product-container {
  display: flex;
  align-items: center;
  justify-content: space-evenly;
  margin: 30px 30px 30px 30px;
}

.image {
  position: relative;
  height: 30vw;
  width: 30vw;
  border-radius: 15px;
}

.image__img {
  display: block;
  height: 400px;
  width: 100%;
  border-radius: 15px;
  /* border: 1px solid black; */
  box-shadow: 0px 0px 8px rgb(199, 196, 196);
}

td {
  /* border: 1px solid black; */
  padding: 1px;
}

.image__overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.6);
  color: #ffffff;
  font-family: "Quicksand", sans-serif;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  opacity: 0;
  transition: opacity 0.25s;
  border-radius: 15px;
}

.image__overlay--blur {
  backdrop-filter: blur(5px);
}

.image__overlay--primary {
  background: #009578;
}

.image__overlay > * {
  transform: translateY(20px);
  transition: transform 0.25s;
}

.image__overlay:hover {
  opacity: 1;
}

.image__overlay:hover > * {
  transform: translateY(0);
}

.product__title {
  font-size: 2em;
  font-weight: bold;
}

.product__description {
  font-size: 1.25em;
  margin-top: 0.25em;
}

/* ---product-end--- */
.container input {
  /* width: 100%; */
  /* padding: 12px 20px; */
  /* margin: 8px 0; */
  display: inline-block;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
}

.container input:focus {
  box-shadow: 0px 0px 8px rgb(199, 196, 196);
  outline: none;
}

.container select {
  border: 1px solid #ccc;
  border-radius: 4px;
}

.container select:focus {
  box-shadow: 0px 0px 8px rgb(199, 196, 196);
  outline: none;
}

.container {
  font-family: Avenir, Helvetica, Arial, sans-serif;
}

/* --- header start --- */
.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 5px 5px 5px 5px;
  background-color: black;
}

.nav {
  display: flex;
  justify-content: space-evenly;
}

.nav button {
  color: rgb(235, 231, 231);
  background-color: black;
  margin: auto 10px auto 10px;
}
/* --- header end --- */

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
}

/* --- footer end --- */
</style>

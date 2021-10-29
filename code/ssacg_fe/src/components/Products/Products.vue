<template>
<div class="page-container-products">
  <div class="upper-table">
    <table>
      <tr>
        <td>
          <!-- <img
            class="logo"
            src="../../assets/logo-anillo-ssacg-multicolor.png"
            alt="Logo"
          /> -->
          <!-- <br>
          <p>{{email}}</p> -->
        </td>
        <td style="padding: 0vw 0vw 0vw 9.25vw;">
            <h2 style="text-align: center;">
                    <strong>Listado de productos</strong>
            </h2>
            <table class="products-table" id="productsList-table">
                <thead>
                <tr>
                    <th>Imagen</th>
                    <th>id</th>
                    <th>Categoría</th>
                    <th>Nombre</th>
                    <th>Precio</th>
                    <th>Stock</th>
                    <th>Descripción</th>
                    
                    <th></th>
                </tr>
                </thead>
                <tbody>
                    <tr v-for="(product, k) in product_list" :key="k">
                        <td><img :src="product.img_src" :alt="product.nombre"></td>
                        <td>{{product.id}}</td>
                        <td>{{ product.category }}</td>
                        <td>{{ product.nombre }}</td>
                        <td>{{ product.precio }}</td>
                        <td>{{ product.stock }}</td>
                        <td>{{ product.description }}</td>
                        <td>
                            <a v-on:click="onEdit($event)">Editar</a>
                            <a v-on:click="onDelete(k, product)">Borrar</a>
                        </td>
                    </tr>
                </tbody>
            </table>
        </td>
      </tr>
    </table>
  </div>
  <div>
    <br />
    <table class="bottom-table"  style="border: 1px solid black;">
      <tr>
        <td>
          <textarea
            placeholder="URL de la imagen"
            name="img_src_TextArea"
            id="img_src_TextArea"
          ></textarea>
        </td>
        <td>
          <table>
            <tr>
              <td>
                <input type="text" id="categoryField" placeholder="Categoría" autocomplete="off" />
              </td>
              <td>
                <input type="text" id="nameField" placeholder="Nombre" autocomplete="off"/>
              </td>
            </tr>
            <tr>
              <td>
                <input
                  type="number" 
                  min ="0.000" 
                  step="0.1" 
                  oninput="(value >= 0)||(value='');"
                  id="priceField" 
                  placeholder="Precio - COP" autocomplete="off" 
                />
              </td>
              <td>
                <input type="number" min="1" oninput="validity.valid||(value='');" id="stockField" placeholder="Stock" autocomplete="off"/>
              </td>
            </tr>
          </table>
        </td>
        <td>
          <textarea
            placeholder="Descripción"
            name="descriptionTextArea"
            id="descriptionTextArea"
            v-on:input="OnInput($event)"
          ></textarea>
        </td>
      </tr>
    </table>
  </div>
  <div class="buttons-panel">
    <div class="CRUD-button-panel">
      <button v-on:click="onFormSubmit()" type="submit">Guardar</button>
      <button style="pointer-events: none; background-color: grey">Buscar</button>
    </div>
    <div class="account-button-panel">
      <button v-on:click="logOut()" >Cerrar sesión</button>
    </div>
  </div>
  </div>
</template>

<script src="@/components/Products/script.js"></script>

<style scoped src="@/components/Products/styles.css"></style>

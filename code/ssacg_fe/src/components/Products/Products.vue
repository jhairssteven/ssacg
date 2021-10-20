<template>

  <div class="upper-table">
    <table>
      <tr>
        <td>
          <img
            class="logo"
            src="../../assets/logo-anillo-ssacg-multicolor.png"
            alt="Logo"
          />
        </td>
        <td style="padding: 0vw 0vw 0vw 9.25vw;">
            <h2 style="text-align: center;">
                    <strong>Listado de productos</strong>
            </h2>
            <table class="products-table" id="productsList-table">
                <thead>
                <tr>
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
    <table class="bottom-table">
      <tr>
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
                  step="0.1"
                  id="priceField"
                  placeholder="Precio" autocomplete="off"
                />
              </td>
              <td>
                <input type="number" id="stockField" placeholder="Stock" autocomplete="off"/>
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
      <button >Buscar</button>
    </div>
    <div class="account-button-panel">
      <button>Cerrar sesión</button>
    </div>
  </div>
</template>

<script src="@/components/Products/script.js"></script>

<style scoped src="@/components/Products/styles.css"></style>

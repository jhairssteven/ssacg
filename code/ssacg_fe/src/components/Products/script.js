import * as strings from "@/strings";
import axios from "axios";

export default {
    name: "products",

    props: {
        email: {
            default: "user", 
            type: String
        },
        tokenStr : {
            default: "null",
            type: String
        }
    },

    data: function () {
        return {
            selectedRow: null,
            product_list: [
            ],
        };
    },

    methods: {
        logOut: function() {
            this.$emit("logOut");
        },

        onFormSubmit: async function () {
            // await this.checkIfLogged();
            if (this.validate()) {
                let formData = this.readFormData();
                if (this.selectedRow == null) {
                    this.insertNewRecord(formData);
                } else {
                    this.updateRecord(formData, this.selectedRow);
                }
                this.resetForm();
            }
        },

        updateRecord: async function (data, selRow) {
            // await this.checkIfLogged();
            let id_product = selRow.cells[1].innerHTML;

            let prodData2update = {
                img_src: data.img_src,
                category: data.category,
                name: data.name,
                unitary_price: data.price,
                stock: data.stock,
                description: data.description,
            }

            axios.put(strings.URLs.updateProduct + id_product + "/",
                prodData2update,
                {
                    headers:
                        { "Authorization": `Bearer ${this.tokenStr}` }
                }
            ).then((result) => {
                selRow.cells[2].innerHTML = result.data.category;
                selRow.cells[3].innerHTML = result.data.name;
                selRow.cells[4].innerHTML = result.data.unitary_price;
                selRow.cells[5].innerHTML = result.data.stock;
                selRow.cells[6].innerHTML = result.data.description;
                selRow.cells[0].innerHTML = result.data.img_src;
            })
            .catch((error) => {
                this.parseErrorForTokens(error, "error in updateProduct()");
            });

        },

        resetForm: function () {
            document.getElementById("categoryField").value = "";
            document.getElementById("nameField").value = "";
            document.getElementById("priceField").value = "";
            document.getElementById("stockField").value = "";
            document.getElementById("descriptionTextArea").value = "";
            document.getElementById("img_src_TextArea").value = "";
            this.selectedRow = null;
        },

        onDelete: function (k, product) {
            // this.checkIfLogged();
            let id_product = product.id;
            if (confirm('Por favor, confirme si desea eliminar este elemento')) {
                let prod_indx = this.product_list.indexOf(product);
                console.log(k, prod_indx);
                if (prod_indx > -1) {
                    axios.delete(
                        strings.URLs.deleteProduct + id_product + "/",
                        { headers: { "Authorization": `Bearer ${this.tokenStr}` } }
                    )
                    .then((result) => {
                        this.product_list.splice(prod_indx, 1);
                    })
                    .catch((error) => {
                        this.parseErrorForTokens(error, "error in onDelete()");
                    });
                }
                this.resetForm();
            }
        },

        onEdit: function (td) {
            this.selectedRow = td.target.parentElement.parentElement;
            document.getElementById("categoryField").value = this.selectedRow.cells[2].innerHTML;
            document.getElementById("nameField").value = this.selectedRow.cells[3].innerHTML;
            document.getElementById("priceField").value = this.selectedRow.cells[4].innerHTML;
            document.getElementById("stockField").value = this.selectedRow.cells[5].innerHTML;
            document.getElementById("descriptionTextArea").value = this.selectedRow.cells[6].innerHTML;
            document.getElementById("img_src_TextArea").value = this.selectedRow.cells[0].innerHTML;

        },

        insertNewRecord: function (data) {
            // this.checkIfLogged();
            let newProd = {
                img_src: data.img_src,
                category: data.category,
                name: data.name,
                unitary_price: data.price,
                stock: data.stock,
                description: data.description,
            }
            axios.post(strings.URLs.insertProduct, newProd,
                { headers: { "Authorization": `Bearer ${this.tokenStr}` } })
                .then((result) => {
                    // traer el id en la respuesta o todos sus datos
                    this.product_list.push({
                        id:             result.data.id_product,
                        img_src:        result.data.img_src,
                        category:       result.data.category,
                        nombre:         result.data.name,
                        precio:         result.data.unitary_price,
                        stock:          result.data.stock,
                        description:    result.data.description,
                    });
                })
                .catch((error) => {
                    if (error.response.status == "400" && 
                    (error.response.data.hasOwnProperty("unitary_price")
                    || error.response.data.hasOwnProperty("stock"))) {
                        // "Ensure this value is greater than or equal to 0.001."
                        // "Ensure this value is greater than or equal to 1."
                        alert("Revisa tus datos, \ningresaste un valor inválido")
                    } else {
                        this.parseErrorForTokens(error, "error on insertNewRecord()");
                    }
                })

        },

        readFormData: function () {
            let formData = {};
            formData["category"] = document.getElementById("categoryField").value;
            formData["name"] = document.getElementById("nameField").value;
            formData["price"] = document.getElementById("priceField").value;
            formData["stock"] = document.getElementById("stockField").value;
            formData["description"] = document.getElementById("descriptionTextArea").value;
            formData["img_src"] = document.getElementById("img_src_TextArea").value;

            return formData;
        },

        validate: function () {
            let nameFV_blank = document.getElementById("nameField").value == "";
            let priceFV_blank = document.getElementById("priceField").value == "";
            let stockFV_blank = document.getElementById("stockField").value == "";

            let nameF_classList = document.getElementById("nameField").classList;
            let priceF_classList = document.getElementById("priceField").classList;
            let stockF_classList = document.getElementById("stockField").classList;

            this.styleField4error(nameFV_blank, nameF_classList);
            this.styleField4error(priceFV_blank, priceF_classList);
            this.styleField4error(stockFV_blank, stockF_classList);

            return !(nameFV_blank || priceFV_blank || stockFV_blank);
        },

        styleField4error: function (blankField, field_classList) {
            if (blankField) {
                field_classList.add("required-field")
            } else {
                if (field_classList.contains("required-field"))
                    field_classList.remove("required-field")
            }
        },

        OnInput: function (e) {
            e.target.style.height = "auto";
            e.target.style.height = (e.target.scrollHeight) + "px";
        },

        getAllProducts: async function() {
            // await this.checkIfLogged();
            axios.get(strings.URLs.getAllProducts, 
                {headers: {
                    "Authorization": `Bearer ${this.tokenStr}`}})
                    .then((result) => {
                        for (let i = 0; i < result.data.length; i++) {
                            this.product_list.push(
                                {
                                    id:             result.data[i].id_product,
                                    img_src:        result.data[i].img_src,
                                    category:       result.data[i].category,
                                    nombre:         result.data[i].name,
                                    precio:         result.data[i].unitary_price,
                                    stock:          result.data[i].stock,
                                    description:    result.data[i].description
                                }
                            );
                        }
                    })
                    .catch((error) => {
                        this.parseErrorForTokens(error, "error in getallproducts()")
                    });
            
        },

        parseErrorForTokens: function(error, errorCodeLocationStr) {
            let alertMsg = "";
            if (error.response.status == "401" )
                alertMsg = "Tus credenciales han expirado,\n ingresa nuevamente";              
            else //other code status e.g: 500
                alertMsg = "Error interno, ingresa nuevamente";

            alert(alertMsg);
            console.log(error, errorCodeLocationStr)

            this.$emit("logOut"); 
        },

        // checkIfLogged: async function() {
        //     if(localStorage.getItem("token_refresh") === null 
        //         || localStorage.getItem("token_access") === null) {
        //             this.$emit("logOut");
        //             return;
        //         }
        //     return axios.post(strings.URLs.refreshToken,
        //             {refresh: localStorage.getItem("token_refresh")},
        //             {header:{}})
        //             .then((result) => {
        //                 localStorage.setItem("token_access", result.data.access);
        //             })
        //             .catch((error) => {
        //                 if (error.response.status == "401") {
        //                     this.$emit("logOut"); // refresh token expired
        //                     console.log("checkIfLogged 401")
        //                 }
        //                 else { //other code status e.g: 500
        //                     console.log(error, "checkIfLogged function error")
        //                     this.$emit("logOut");
        //                 }
        //             })
        // },


    },

    created: async function () {
        document.title = strings.pagetitle.products;
        // await this.checkIfLogged();
        this.getAllProducts();
    },
};
import * as strings from "@/strings";
import axios from "axios";

export default {
    name: "products",

    props: ['tokenStr'],

    data: function () {
        return {
            selectedRow: null,
            product_list: [
            ],
            // tokenStr: "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjM1MTkzMTk4LCJqdGkiOiI4ZWVjYzliNmQ5NjY0OGM0YTdlODAzZTY2YjMxNjdiYSIsImlkX3VzZXIiOjF9.iOREbRuAufBOZtjkUkjeFHAP5Sk1gr_zD0JG21qGJks",
        };
    },

    methods: {
        logOut: function() {
            localStorage.clear();
            this.$emit("verifyAuth");
            return;
        },

        onFormSubmit: function () {
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

        updateRecord: function (data, selRow) {
            let id_product = selRow.cells[0].innerHTML;

            let prodData2update = {
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
                selRow.cells[1].innerHTML = result.data.category;
                selRow.cells[2].innerHTML = result.data.name;
                selRow.cells[3].innerHTML = result.data.unitary_price;
                selRow.cells[4].innerHTML = result.data.stock;
                selRow.cells[5].innerHTML = result.data.description;
            })
            .catch((error) => {
                    console.log(error, 'error');
                    alert(JSON.stringify(error.response.data));
            });

        },

        resetForm: function () {
            document.getElementById("categoryField").value = "";
            document.getElementById("nameField").value = "";
            document.getElementById("priceField").value = "";
            document.getElementById("stockField").value = "";
            document.getElementById("descriptionTextArea").value = "";
            this.selectedRow = null;
        },

        onDelete: function (k, product) {
            let id_product = product.id;
            if (confirm('Por favor, confirme si desea eliminar este elemento')) {
                let prod_indx = this.product_list.indexOf(product);
                console.log(k, prod_indx);
                if (prod_indx > -1) {
                    axios.delete(
                        strings.URLs.deleteProduct + id_product + "/",
                        { headers: { "Authorization": `Bearer ${this.tokenStr}` } }
                    ).then((result) => {
                        this.product_list.splice(prod_indx, 1);
                    }).catch((error) => {
                        console.log(error, 'error');
                        alert(JSON.stringify(error.response.data));
                    });
                }
                this.resetForm();
            }
        },

        onEdit: function (td) {
            this.selectedRow = td.target.parentElement.parentElement;
            document.getElementById("categoryField").value = this.selectedRow.cells[1].innerHTML;
            document.getElementById("nameField").value = this.selectedRow.cells[2].innerHTML;
            document.getElementById("priceField").value = this.selectedRow.cells[3].innerHTML;
            document.getElementById("stockField").value = this.selectedRow.cells[4].innerHTML;
            document.getElementById("descriptionTextArea").value = this.selectedRow.cells[5].innerHTML;
        },

        insertNewRecord: function (data) {
            let newProd = {
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
                        category:       result.data.category,
                        nombre:         result.data.name,
                        precio:         result.data.unitary_price,
                        stock:          result.data.stock,
                        description:    result.data.description,
                    });
                })
                .catch((error) => {
                    alert(JSON.stringify(error.response.data));
                })

        },

        readFormData: function () {
            let formData = {};
            formData["category"] = document.getElementById("categoryField").value;
            formData["name"] = document.getElementById("nameField").value;
            formData["price"] = document.getElementById("priceField").value;
            formData["stock"] = document.getElementById("stockField").value;
            formData["description"] = document.getElementById("descriptionTextArea").value;
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

        getAllProducts: function() {
            axios.get(strings.URLs.getAllProducts, 
                {headers: {
                    "Authorization": `Bearer ${this.tokenStr}`}})
                    .then((result) => {
                        for (let i = 0; i < result.data.length; i++) {
                            this.product_list.push(
                                {
                                    id:             result.data[i].id_product,
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
                        if(error.response.status == "401") {
                            this.logOut();
                        }
                        else {
                            console.log(error, 'error in getallproducts()');
                            alert(JSON.stringify(error.response.data));
                        }
                    })
        }

    },

    created: function () {
        document.title = strings.pagetitle.products;
        this.getAllProducts();
    },
};
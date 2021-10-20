import * as strings from "@/strings";
import axios from "axios";

export default {
    name: "products",

    data: function () {
        return {
            selectedRow: null,
            product_list: [
            ]
        };
    },

    methods: {

        onFormSubmit: function () {
            if (this.validate()) {
                let formData = this.readFormData();
                if (this.selectedRow == null) {
                    this.insertNewRecord(formData);
                } else {
                    this.updateRecord(formData);
                }
                this.resetForm();
            }
        },

        updateRecord: function (data) {
            this.selectedRow.cells[0].innerHTML = data.category;
            this.selectedRow.cells[1].innerHTML = data.name;
            this.selectedRow.cells[2].innerHTML = data.price;
            this.selectedRow.cells[3].innerHTML = data.stock;
            this.selectedRow.cells[4].innerHTML = data.description;
        },

        resetForm: function () {
            document.getElementById("categoryField").value = "";
            document.getElementById("nameField").value = "";
            document.getElementById("priceField").value = "";
            document.getElementById("stockField").value = "";
            document.getElementById("descriptionTextArea").value = "";
            this.selectedRow = null;
        },

        onDelete: function (td, k, product) {
            if (confirm('Por favor, confirme si desea eliminar este elemento')) {
                let prod_indx = this.product_list.indexOf(product);
                console.log(k, prod_indx);
                if (prod_indx > -1) {
                    this.product_list.splice(prod_indx, 1);
                }
                this.resetForm();
            }
        },

        onEdit: function (td) {
            console.log(td.target.tagName)
            this.selectedRow = td.target.parentElement.parentElement;
            document.getElementById("categoryField").value = this.selectedRow.cells[0].innerHTML;
            document.getElementById("nameField").value = this.selectedRow.cells[1].innerHTML;
            document.getElementById("priceField").value = this.selectedRow.cells[2].innerHTML;
            document.getElementById("stockField").value = this.selectedRow.cells[3].innerHTML;
            document.getElementById("descriptionTextArea").value = this.selectedRow.cells[4].innerHTML;
        },

        insertNewRecord: function (data) {
            let newProd = {
                category: data.category,
                name: data.name,
                unitary_price: data.price,
                stock: data.stock,
                description: data.description,
            }
            let tokenStr = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjM0NzA3MzYyLCJqdGkiOiJhOTA0ZWI1Y2EyZjk0MTM5OTQ3MzRiZjJkYTA0ZTA2NiIsImlkX3VzZXIiOjF9.Mhpl2UkOiVCQxJPQT5rTQqjXhI5ymLv-jYdhqH5Z3zk";
            axios.post(strings.URLs.insertProduct, newProd, 
                {headers: {"Authorization" : `Bearer ${tokenStr}`}})
            .then((result) => {
                this.product_list.push({
                    category: data.category,
                    nombre: data.name,
                    precio: data.price,
                    stock: data.stock,
                    description: data.description,
                });
            })
            .catch((error) => {
                if (error.response.status == "400")
                    alert(JSON.stringify(error.response.data));
                else
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
        }

    },

    created: function () {
        document.title = strings.pagetitle.products;
    },
};
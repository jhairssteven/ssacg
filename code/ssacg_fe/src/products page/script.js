let selectedRow = null;

function onFormSubmit() {
    if (validate()) {
        let formData = readFormData();
        if (selectedRow == null) {
            insertNewRecord(formData);
        } else {
            updateRecord(formData);
        }
        resetForm();
    }
}

function updateRecord(data) {
    selectedRow.cells[0].innerHTML = data.category;
    selectedRow.cells[1].innerHTML = data.name;
    selectedRow.cells[2].innerHTML = data.price;
    selectedRow.cells[3].innerHTML = data.stock;
    selectedRow.cells[4].innerHTML = data.description;
}

function resetForm() {
    document.getElementById("categoryField").value = "";
    document.getElementById("nameField").value = "";
    document.getElementById("priceField").value = "";
    document.getElementById("stockField").value = "";
    document.getElementById("descriptionTextArea").value = "";
    selectedRow = null;
}

function onDelete(td) {
    if (confirm('Por favor, confirme si desea eliminar este elemento')) {
        row2Delete = td.parentElement.parentElement;
        document.getElementById("productsList").deleteRow(row2Delete.rowIndex);
        resetForm();
    }
}

function onEdit(td) {

    selectedRow = td.parentElement.parentElement;
    document.getElementById("categoryField").value = selectedRow.cells[0].innerHTML;
    document.getElementById("nameField").value = selectedRow.cells[1].innerHTML;
    document.getElementById("priceField").value = selectedRow.cells[2].innerHTML;
    document.getElementById("stockField").value = selectedRow.cells[3].innerHTML;
    document.getElementById("descriptionTextArea").value = selectedRow.cells[4].innerHTML;
}

function insertNewRecord(data) {
    let table = document.getElementById("productsList").getElementsByTagName('tbody')[0];
    let newRow = table.insertRow(table.length);

    categoryCell = newRow.insertCell(0);
    categoryCell.innerHTML = data.category;

    nameCell = newRow.insertCell(1);
    nameCell.innerHTML = data.name;

    priceCell = newRow.insertCell(2);
    priceCell.innerHTML = data.price;

    stockCell = newRow.insertCell(3);
    stockCell.innerHTML = data.stock;

    descriptionCell = newRow.insertCell(4);
    descriptionCell.innerHTML = data.description;

    UpdateDeleteCell = newRow.insertCell(5);
    UpdateDeleteCell.innerHTML = `<a onClick="onEdit(this)">Editar</a>
                                    <a onClick="onDelete(this)">Borrar</a>`;
}

function readFormData() {
    let formData = {};
    formData["category"] = document.getElementById("categoryField").value;
    formData["name"] = document.getElementById("nameField").value;
    formData["price"] = document.getElementById("priceField").value;
    formData["stock"] = document.getElementById("stockField").value;
    formData["description"] = document.getElementById("descriptionTextArea").value;
    return formData;
}

function validate() {
    let nameFV_blank = document.getElementById("nameField").value == "";
    let priceFV_blank = document.getElementById("priceField").value == "";
    let stockFV_blank = document.getElementById("stockField").value == "";

    let nameF_classList = document.getElementById("nameField").classList;
    let priceF_classList = document.getElementById("priceField").classList;
    let stockF_classList = document.getElementById("stockField").classList;
    
    styleField4error(nameFV_blank, nameF_classList);
    styleField4error(priceFV_blank, priceF_classList);
    styleField4error(stockFV_blank, stockF_classList);

    return !(nameFV_blank || priceFV_blank || stockFV_blank);
}

function styleField4error(blankField, field_classList) {
    if (blankField) {
        field_classList.add("required-field")
    } else {
        if (field_classList.contains("required-field"))
            field_classList.remove("required-field")
    }
}


// text area automatic height resizing
const tx = document.getElementsByTagName("textarea");
for (let i = 0; i < tx.length; i++) {
  tx[i].setAttribute("style", "height:" + (tx[i].scrollHeight) + "px;overflow-y:hidden;");
  tx[i].addEventListener("input", OnInput, false);
}

function OnInput() {
  this.style.height = "auto";
  this.style.height = (this.scrollHeight) + "px";
}

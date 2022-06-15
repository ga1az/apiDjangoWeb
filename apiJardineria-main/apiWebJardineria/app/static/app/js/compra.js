const btnfin = document.getElementById("btn-fin");
const calle = document.forms["form-direc"]["calle"];
const numero = document.forms["form-direc"]["numero"];
const region = document.forms["form-direc"]["region"];
const ciudad = document.forms["form-direc"]["ciudad"];
const zip = document.forms["form-direc"]["zip"];

const nombre = document.forms["forma-pago"]["nombre"];
const tarjeta = document.forms["forma-pago"]["tarjeta"];
const mes = document.forms["forma-pago"]["mes"];
const anio = document.forms["forma-pago"]["anio"];
const cvv = document.forms["forma-pago"]["cvv"];

btnfin.addEventListener("click", function () {
    if (
        calle.value == "" ||
        numero.value == "" ||
        region.value == "" ||
        ciudad.value == "" ||
        zip.value == ""
    ) {
        alert("Por favor, rellene todos los campos de la dirección");
    } else if (
        nombre.value == "" ||
        tarjeta.value == "" ||
        mes.value == "" ||
        anio.value == "" ||
        cvv.value == ""
    ) {
        alert("Por favor, rellene todos los campos de la forma de pago");
    } else {
        window.location.href = "./index.html";
    }
});

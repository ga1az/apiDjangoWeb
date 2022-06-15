async function loadApi() {
    const response = await fetch("https://mindicador.cl/api/");
    return await response.json();
}

const api = loadApi();
api.then((data) => {
    let dolar = document.getElementById("dolar");
    dolar.innerText = data.dolar.valor;
});

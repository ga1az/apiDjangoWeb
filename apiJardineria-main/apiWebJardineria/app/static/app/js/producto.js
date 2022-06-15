//Cantidad a llevar actualizable
const cantidad = document.getElementById('cantidad-num');

cantidad.onchange = () =>{
    let cantidad = document.getElementById('cantidad-num').value;
    let precio = document.getElementById('precio-num').innerText;
    let total = document.getElementById('total-num');
    let alert = document.getElementById('alert');
    let disponible = document.getElementById('disp-num').innerText;
    if(cantidad > disponible){
        let template = `
        <div>
            <p class="text-danger">La cantidad a llevar</p>
            <p class="text-danger">no puede ser mayor a la disponible</p>
        </div>
        `
        total.innerHTML = template;
    }else{total.innerText = cantidad * precio;}
}
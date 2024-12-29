

function modal_payment_comanda() {
    document.getElementById('payment-comanda').style.display = 'block';
}

function close_modal_payment_comanda() {
    document.getElementById('payment-comanda').style.display = 'none';
}



function imprimirFichas() {
    const element = document.getElementById("list-products-balcao");
    const style = `<style>
                    td, th {
                                      
                    border-collapse: collapse; 
                    padding-top: 30px;
                    margin: 0px;
                    text-align: center;
                    font-size: 24px;}
                    </style>`;
    const agora = new Date();
    var dateString = agora.getDay() + '/' + agora.getMonth() + '/' + agora.getFullYear() + ' - ' + agora.getHours() + ':' + agora.getMinutes()+' - Raul Rock Bar & Café';

    if (element) {
      var content = element.innerHTML;
      content = content.replace(/<button[^>]*>(?:(?!<\/button>)[\s\S])*<\/button>/gi,'');
      content = content.replace(/<tfoot[^>]*>(?:(?!<\/tfoot>)[\s\S])*<\/tfoot>/gi,'');
      content = content.replace(/<th[^>]*>(?:(?!<\/th>)[\s\S])*<\/th>/gi,'');
      content = content.replace(/<\/tr>/g,'</tr><tr><td colspan="2" style="font-size: 12px">'+dateString+ '<BR>VÁLIDO SOMENTE POR ESSA NOITE'+'</td></tr>');
    
      var printWindow = window.open('', '_blank');
      printWindow.document.write('<table>'+content+'</table>'+style);
      printWindow.document.close();
      printWindow.print();
      printWindow.close();
    } else {
      console.error(`Element with ID not found`);
    }
  }


function reloadPage(){
  setTimeout(function() {
    location.reload();}, 10);
}

function backPage() {
  setTimeout(function() {
    history.back();}, 100);
  setTimeout(function() {
    location.reload();}, 10);
}
  
document.onkeydown = teclado

function teclado(event){
  if (event.keyCode == 13){
    addProductBalcao()
  }else{
    console.log('')
  }

}

function updateTotal(){
  const newTotal = document.getElementById('total').innerText
  document.getElementById('first-total').innerHTML = 'R$ ' + newTotal
}


function addProductBalcao() {
  var productId = document.getElementById('0').innerText;
  var comandaId = document.getElementById('comanda0').innerText;
  var qtd = document.getElementById('qtd-product').value;
  const url = `/balcao/addProductBalcaoTeclado${productId}/${comandaId}/${qtd}/`;
  fetch(url, {
    method: 'GET', 
    headers: {
      'Content-Type': 'application/json'
    },}).then(function(response) {
    return response.text();
    }).then(function(text) {
    var listProductsBalcaoElement = document.getElementById("list-products-balcao");
    listProductsBalcaoElement.innerHTML = text;
  })
  const receber = document.getElementById('pagarComanda')
  const imprimir = document.getElementById('imprimirFichas')
  receber.removeAttribute('disabled');
  imprimir.removeAttribute('disabled');
  setTimeout(function() {
    updateTotal();}, 100);
}


function removeProductBalcao(id) {

  const url = `/balcao/removeProductBalcao${id}/`;
  fetch(url, {
    method: 'GET', 
    headers: {
      'Content-Type': 'application/json'
    },}).then(function(response) {
    return response.text();
    }).then(function(text) {
    var listProductsBalcaoElement = document.getElementById("list-products-balcao");
    listProductsBalcaoElement.innerHTML = text;
  })

  setTimeout(function() {
    updateTotal();}, 100);
  
}


document.getElementById('productForm').addEventListener('submit', function(event) {
    event.preventDefault(); 
});





function searchProduct() {
  setTimeout(() => {
    time();
  }, 100);
  function time(){
  var search_product = document.getElementById('search-product').value.trim()
  var productListElement = document.getElementById("product-list");
  if(search_product.length >= 1 ){
  fetch(`/balcao/listProductBalcao/13/${search_product}`, {
    method: 'GET',}
  ).then(function(response) {
    return response.text();
  }).then(function(text) {
    productListElement.innerHTML = text;
    
  })}}
}

function addProductClick(productId, comandaId) {
  var qtd = document.getElementById('qtd-product').value
  fetch(`/balcao/addProductBalcaoTeclado${productId}/${comandaId}/${qtd}`, {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json'}
    })
    
  .then(function(response) {
    return response.text();
  }).then(function(text) {
    var listProductsBalcaoElement = document.getElementById("list-products-balcao");
    listProductsBalcaoElement.innerHTML = text;
  })
  
  const receber = document.getElementById('pagarComanda')
  const imprimir = document.getElementById('imprimirFichas')
  receber.removeAttribute('disabled');
  imprimir.removeAttribute('disabled');

  setTimeout(function() {
    updateTotal();}, 100);

}

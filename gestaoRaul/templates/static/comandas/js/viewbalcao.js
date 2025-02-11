

function modal_payment_comanda() {
    document.getElementById('payment-comanda').style.display = 'block';
    recebido = document.getElementById('recebido')
    recebido.focus()
}

function troco(){
  recebido = document.getElementById('recebido').value
  total = document.getElementById('first-total').innerHTML
  resultado = document.getElementById('troco')
  total = total.replace('R$ ','')
  total = total.replace(',','.')
  result = recebido - total
  resultado.innerHTML = 'Troco: R$ '+result
}

function close_modal_payment_comanda() {
    document.getElementById('payment-comanda').style.display = 'none';
    document.getElementById('search-product').focus()
}


function imprimirFichas() {
    const element = document.getElementById("list-products-balcao");
    const style = `<style>
                    td, th {
                    max-width: 200px;   
                    border-collapse: collapse; 
                    padding-top: 30px;
                    margin: 0px;
                    text-align: center;
                    font-size: 24px;}
                    </style>`;
    const agora = new Date();
    var dateString = agora.getDate() + '/' +( agora.getMonth() + 1 )+ '/' + agora.getFullYear() + ' - ' + agora.getHours() + ':' + agora.getMinutes()+' - Raul Rock Bar & Café';

    if (element) {
      var content = element.innerHTML;
      content = content.replace(/<button[^>]*>(?:(?!<\/button>)[\s\S])*<\/button>/gi,'');
      content = content.replace(/<tfoot[^>]*>(?:(?!<\/tfoot>)[\s\S])*<\/tfoot>/gi,'');
      content = content.replace(/<th[^>]*>(?:(?!<\/th>)[\s\S])*<\/th>/gi,'');
      content = content.replace(/R\$.{7}/g, '');
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
  if (document.getElementById('payment-comanda').style.display == 'none'){
      if (event.keyCode == 13){
        addProductBalcao()
      }else{
        console.log(event.keyCode)
      }
    }else{
      if (event.keyCode == 13){
        troco()
      }else{
        console.log('')
      }
    }

}

function updateTotal(){
  const newTotal = document.getElementById('total').innerText
  document.getElementById('first-total').innerHTML = 'R$ ' + newTotal
}


function addProductBalcao() {
  var productId = document.getElementById('0').innerText;
  var comandaId = document.getElementById("id-comanda-balcao").value;
  fieldQtd = document.getElementById('qtd-product');

  var qtd = fieldQtd.value;
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
  document.getElementById('search-product').focus()
  fieldQtd.value = 1;
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
  document.getElementById('search-product').focus()
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
  var comanda_id = document.getElementsByName("id-comanda-balcao").value;
  if(search_product.length == 0 ){search_product ='*';}
  fetch(`/balcao/listProductBalcao/1/${search_product}`, {
  // fetch(`/balcao/listProductBalcao/${comanda_id}/${search_product}`, {
    method: 'GET',}
  ).then(function(response) {
    return response.text();
  }).then(function(text) {
    productListElement.innerHTML = text;
    
  })}
}

function addProductClick(productId) {
  fieldQtd = document.getElementById('qtd-product');
  var qtd = fieldQtd.value;
  var comanda_id = document.getElementById("id-comanda-balcao").value;
  fetch(`/balcao/addProductBalcaoTeclado${productId}/${comanda_id}/${qtd}`, {
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
  var search = document.getElementById('search-product')
  receber.removeAttribute('disabled');
  imprimir.removeAttribute('disabled');
  search.focus()
  fieldQtd.value = 1;

  setTimeout(function() {
    updateTotal();}, 100);

}

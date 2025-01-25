

function openModal() {
    document.getElementById('Modal-add-product').style.display = 'block';
}
function openModalAlter() {
    document.getElementById('Modal-alter-comanda').style.display = 'block';
    var name = document.getElementById('name-comanda').innerText.replace('Nome: ','').replace(' | ', '')
    var mesa = document.getElementById('h-mesaId').value
    console.log(name)
    console.log(mesa)

    var fildName =  document.getElementById('nameComanda')
    fildName.value = name
    var fildMesa =  document.getElementById('select-mesa')
    fildMesa.value = mesa
}

function closeModalAlter() {
    document.getElementById('Modal-alter-comanda').style.display = 'none';
}
function openModalObs(id) {
    document.getElementById('modal-obs').style.display = 'block';
    idd = document.getElementById('id-temp').value = id;
    obs = document.getElementById('obs').value;
    console.log(id);
    console.log(obs);
}


function modal_payment_comanda() {
    document.getElementById('payment-comanda').style.display = 'block';
    recebido = document.getElementById('recebido')
    recebido.focus()
}


function modal_conta_client() {
    document.getElementById('conta-cliente').style.display = 'block';
    // recebido = document.getElementById('recebido')
    // recebido.focus()
}

function close_modal_conta_client() {
    document.getElementById('conta-cliente').style.display = 'none';
}


function close_modal_payment_comanda() {
    document.getElementById('payment-comanda').style.display = 'none';
}

function closeModal() {
    document.getElementById('Modal-add-product').style.display = 'none';
}
function closeModalObs() {
    document.getElementById('modal-obs').style.display = 'none';
}



function imprimirFichas() {
    const element = document.getElementById("list-products-comanda");
    const style = `<style>
                    td, th {
                                      
                    border-collapse: collapse; 
                    padding-top: 35px;
                    margin: 20px;
                    text-align: center;
                    font-size: 24px;}
                    </style>`;
    const agora = new Date();
    var dateString = agora.getDate() + '/' + (agora.getMonth()+1) + '/' + agora.getFullYear() + ' - ' + agora.getHours() + ':' + agora.getMinutes()+' - Raul Rock Bar & Café';

    if (element) {
      var content = element.innerHTML;
    //   console.log(content);
      content = content.replace( /<img[^>]*>/gi,'');
      content = content.replace(/<tfoot[^>]*>(?:(?!<\/tfoot>)[\s\S])*<\/tfoot>/gi,'');

      content = content.replace(/<th[^>]*>(?:(?!<\/th>)[\s\S])*<\/th>/gi,'');
      // content = content.replace(/<\/tr>/g,'</tr><tr><td colspan="2" style="font-size: 12px">'+dateString+'</td></tr>');
      content = content.replace(/<\/tr>/g,'</tr><tr><td colspan="2" style="font-size: 12px">'+dateString+ '<BR>VÁLIDO SOMENTE POR ESSA NOITE'+'</td></tr>');

      console.log(content);
    
      var printWindow = window.open('', '_blank');
      printWindow.document.write('<table>'+content+'</table>'+style);
      printWindow.document.close();
      printWindow.print();
      printWindow.close();
    } else {
      console.error(`Element with ID not found`);
    }
  }


function imprimirConta() {
  reloadPage();
    const element = document.getElementById("list-products-comanda");
    const style = `<style>
                    td, th {
                    border-collapse: collapse; 
                    padding-top: 15px;
                    margin: 15px;
                    text-align: justify;
                    font-size: 15px;}
                    </style>`;
    const agora = new Date();
    var dateString = agora.getDate() + '/' + (agora.getMonth()+1) + '/' + agora.getFullYear() + ' - ' + agora.getHours() + ':' + agora.getMinutes();

    if (element) {
      var content = element.innerHTML;
    //   console.log(content);
      content = content.replace(/<img[^>]*>/gi,'');
      content = content.replace(/<th[^>]*>(?:(?!<\/th>)[\s\S])*<\/th>/gi,'');
      // content = content.replace('icons','');
      content = '<img src="/static/midia/logo.png" style="width: 240px; height: 200px;">'
      +'<br>'  
      +document.getElementById('name-comanda').innerText.replace(' | ', '')
      +'<br>'  
      +document.getElementById('mesa-comanda').innerText
      +'<br>'  
      +document.getElementById('open-comanda').innerText
      +'<br> Fechado em: '
      +dateString  
        +content
          +'<br>'
          
         
    
      var printWindow = window.open('', '_blank');
      printWindow.document.write('<table>'+content+'</table><b>Volte Sempre!😁😊</b>'+style);
      printWindow.document.close();
      printWindow.print();
      printWindow.close();
    } else {
      console.error(`Element with ID not found`);
    }
  }

function reloadPage(){
  setTimeout(function() {
    location.reload();}, 100);
}

function backPage() {
  setTimeout(function() {
    history.back();}, 100);
  setTimeout(function() {
    location.reload();}, 100);
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


document.onkeydown = teclado

function teclado(event){
  if (document.getElementById('payment-comanda').style.display == 'block'){
    if (event.keyCode == 13){
      troco()
    }else{
      console.log(event.keyCode)
    }
  }else{
    console.log('')
  }

}
function addOrder(){
  obs = document.getElementById('obs').value
  var id = document.getElementById('id-temp').value
  fetch(`/comandas/editOrders/${id}/${obs}`, {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json'}
    })
    
    .then(function(response) {
      if(response.status == 200){
        closeModalObs()
        alert('Pedido atualizado com sucesso!')
      }else{
        alert('Erro ao atualizar pedido!')
      }
      
  })
}

function addProductComanda(productId,comandaId, cuisine) {
  obs = document.getElementById('obs');
  console.log(obs.value);
  console.log(cuisine);
  if(cuisine == 'ggg'){
    var obs = openModalObs();
    
  }else{

  fetch(`/comandas/addProduct${productId}/${comandaId}`, {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json'}
    })
    
  .then(function(response) {
    return response.text();
  }).then(function(text) {
    console.log(text);
    var listProductsBalcaoElement = document.getElementById("list-products-comanda");
    listProductsBalcaoElement.innerHTML = text;
  })
  
  // const receber = document.getElementById('pagarComanda')
  // const imprimir = document.getElementById('imprimirFichas')
  // var search = document.getElementById('search-product')

  // setTimeout(function() {
  //   updateTotal();}, 100);
    
  alert('Produto adicionado com sucesso!');
  }



}



// document.getElementById('openModal').addEventListener('click', openModal);

// document.getElementById('productForm').addEventListener('submit', function(event) {
//     event.preventDefault(); 
// });


//  hx-get="{% url 'addProduct' product.id comanda.id %} " hx-trigger="click" hx-target="#list-products-comanda"



function openModal() {
  textField = document.getElementById('search-product')
if (textField) {
  setTimeout(() => {
    textField.focus();
  }, 500); // 50ms de delay (ajuste conforme necessário)
}
  textField.value = '';
}


function closeModal() {
   var popover = document.getElementById('addProduct');
   popover.hidePopover()
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
    textField = document.getElementById('obs')
    textField.focus()

}


function modal_payment_comanda() {
    document.getElementById('payment-comanda').style.display = 'block';
    recebido = document.getElementById('recebido')
    recebido.focus()
}
function modal_payment_parcial() {
    document.getElementById('payment-parcial').style.display = 'block';
    value = document.getElementById('value-parcial')
    value.focus()

}


function modal_conta_client() {
    document.getElementById('conta-cliente').style.display = 'block';

}

function close_modal_conta_client() {
    document.getElementById('conta-cliente').style.display = 'none';
}


function close_modal_payment_parcial() {
    document.getElementById('payment-parcial').style.display = 'none';
}
function close_modal_payment_comanda() {
    document.getElementById('payment-comanda').style.display = 'none';
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
function printOrder(id) {
  var item = document.getElementById('id-for-print-'+id).innerText
  var cliente = document.getElementById('name-comanda').innerText
  var local = document.getElementById('mesa-comanda').innerText
  var obs = document.getElementById(id+'-obsOrder').value
  const agora = new Date();
  var dateString = agora.getDate() + '/' + (agora.getMonth()+1) + '/' + agora.getFullYear() + ' - ' + agora.getHours() + ':' + agora.getMinutes();
  console.log(item)
  console.log(cliente)
  console.log(local)
    const body = `<style>
                    td, th {
                                      
                    border-collapse: collapse; 
                    padding-top: 20px;
                    margin: 20px;
                    text-align: center;
                    font-size: 20px;}
                    </style>
                   <tr><td>${item}</td></tr>
                   <tr><td>${obs}</td></tr>
                   <tr><td>${cliente}${local}</td></tr>
                   <tr><td>${dateString}</td></tr>
                    `;

          var printWindow = window.open('', '_blank');
            // printWindow.body.appendChild(body);
              printWindow.document.write('<table>'+body+'</table>');
              printWindow.document.close();
              printWindow.print();
              printWindow.close();

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
      printWindow.document.write('<table>'+content+'</table><br><b>Volte Sempre!😁😊</b><br>'+style);
      printWindow.document.close();
      printWindow.print();
      printWindow.close();
    } else {
      console.error(`Element with ID not found`);
    }
  }


function closeConta(id){

  const resultadoConfirmacao = confirm("Encerrar comanda?");
  const buttonAdd = document.getElementById('openModal')
  const buttonClose = document.getElementById('closeComanda')
  const buttonreOpenComanda = document.getElementById('reOpenComanda')
  const buttonPrintComanda = document.getElementById('printComanda')
  const buttonPayment = document.getElementById('pagarComanda')
  if (resultadoConfirmacao){

  fetch(`/comandas/closeComanda/${id}/`, {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': document.querySelector('[name="csrfmiddlewaretoken"]').value}
    })
    .then(response => response.json())
    .then(data => {
      if(data.status == 'ok'){
        buttonPrintComanda.style.display = 'flex'
        buttonClose.style.display = 'none'
        buttonAdd.style.display = 'none'
        buttonreOpenComanda.style.display = 'flex'
        buttonPayment.style.display = 'flex'
        showToast('✅Comanda encerrada!😁','success')
        imprimirConta()
    }
  })
  .catch(error => {
    showToast('❌Ocorreu um erro!😢','error')
  });
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


function addOrder(){
  obs = document.getElementById('obs')
  
  id = document.getElementById('id-temp').value
  var obsPrint = document.getElementById(id+'-obsOrder')
  tooltipObs = document.getElementById('tooltip-id-'+id)

  fetch(`/comandas/editOrders/${id}/${obs.value}`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': document.querySelector('[name="csrfmiddlewaretoken"]').value}
    })
    .then(response => response.json())
    .then(data => {
      if(data.status == 'ok'){
        showToast('✅Pedido atualizado com sucesso!😁','success')
        tooltipObs.dataset.tooltip = data.obs
        obs.value = ''
        obsPrint.value = data.obs
        document.getElementById('modal-obs').style.display = 'none';
      
    }
  })
  .catch(error => {
    console.log(error)
    showToast('❌Ocorreu um erro!😢','error')
  });

}


function showToastAdd(message, type ,duration = 3000) {
  const toast = document.getElementById('toast-add');

  if (type === 'success') {
    toast.style.backgroundColor = '#28a745';
  } else if (type === 'error') {
    toast.style.backgroundColor = '#dc3545';
  } else if (type === 'info') {
    toast.style.backgroundColor = '#ffc107';
  }
  const toastMessage = document.getElementById('toast-message-add');
  toastMessage.textContent = message;
  toast.classList.add('show');

  setTimeout(() => {
    toast.classList.remove('show');
  }, duration);
}
function addProductComanda(productId,comandaId, cuisine) {
  obs = document.getElementById('obs');
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
    var listProductsBalcaoElement = document.getElementById("list-products-comanda");
    listProductsBalcaoElement.innerHTML = text;
  })
  showToastAdd('Produto adicionado com sucesso!😁','success');
  }

}

function taxa(){
  var taxa = document.getElementById('taxa')
  var total = document.getElementById('first-total')
  var totalComTaxa = document.getElementById('totalComTaxa').innerHTML
  var totalSemTaxa = document.getElementById('totalSemTaxa').innerHTML

  if (taxa.checked){
    total.innerHTML = totalComTaxa
  }else{
    total.innerHTML = totalSemTaxa
  }
}



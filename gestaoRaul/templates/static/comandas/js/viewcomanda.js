

function openModal() {
    document.getElementById('Modal-add-product').style.display = 'block';
}


// function open_remove_product_comanda() {
//     document.getElementById('remove-product-comanda').style.display = 'block';
//     // alert('Produto removido com sucesso!');
// }

function modal_payment_comanda() {
    document.getElementById('payment-comanda').style.display = 'block';
}

function close_modal_payment_comanda() {
    document.getElementById('payment-comanda').style.display = 'none';
}

function closeModal() {
    document.getElementById('Modal-add-product').style.display = 'none';
}


// function removeCloseModal() {
//     document.getElementById('remove-product-comanda').style.display = 'none';
// }

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
    var dateString = agora.getDay() + '/' + agora.getMonth() + '/' + agora.getFullYear() + ' - ' + agora.getHours() + ':' + agora.getMinutes()+' - Raul Rock Bar & Café';

    if (element) {
      var content = element.innerHTML;
    //   console.log(content);
      content = content.replace(/<button[^>]*>(?:(?!<\/button>)[\s\S])*<\/button>/gi,'');
      content = content.replace(/<th[^>]*>(?:(?!<\/th>)[\s\S])*<\/th>/gi,'');
      content = content.replace(/<\/tr>/g,'</tr><tr><td colspan="2" style="font-size: 12px">'+dateString+'</td></tr>');
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
                    text-align: center;
                    font-size: 18px;}
                    </style>`;
    const agora = new Date();
    var dateString = agora.getDay() + '/' + agora.getMonth() + '/' + agora.getFullYear() + ' - ' + agora.getHours() + ':' + agora.getMinutes()+' - Raul Rock Bar & Café';

    if (element) {
      var content = element.innerHTML;
    //   console.log(content);
      content = content.replace(/<button[^>]*>(?:(?!<\/button>)[\s\S])*<\/button>/gi,'');
      content = content.replace(/<th[^>]*>(?:(?!<\/th>)[\s\S])*<\/th>/gi,'');
      // content = content.replace(/<\/tr>/g,'</tr><tr><td colspan="2" style="font-size: 12px">'+dateString+'</td></tr>');
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
  

document.onkeydown = teclado

function teclado(event){
  if (event.keyCode == 65){
    openModal()
  }
  else if (event.keyCode == 73){
    imprimirFichas()
  }
  // else if (event.keyCode == 70){
  //   imprimirConta()
  // }
}


function addProductComanda(productId) {
  alert('Produto adicionado com sucesso!');
    // const productName = document.getElementById('productName').value;
    // const productPrice = document.getElementById('productPrice').value;
    // const productDescription = document.getElementById('productDescription').value;
    // const productqtd = document.getElementById('productqtd').value;
    // const categorie = document.getElementById('select-categorie').value;
    // const url = `/comandas/addProductComanda/${productName}/${productPrice}/${productDescription}/${productqtd}/${categorie}/`;
    // window.location.href = url;
}



document.getElementById('openModal').addEventListener('click', openModal);

document.getElementById('productForm').addEventListener('submit', function(event) {
    event.preventDefault(); 
});


 
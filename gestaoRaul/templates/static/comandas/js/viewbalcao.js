// function openModal() {
//     document.getElementById('Modal-add-product').style.display = 'block';
// }


// function open_remove_product_comanda() {
//     document.getElementById('remove-product-comanda').style.display = 'block';
// }

function modal_payment_comanda() {
    document.getElementById('payment-comanda').style.display = 'block';
}

function close_modal_payment_comanda() {
    document.getElementById('payment-comanda').style.display = 'none';
}

// function closeModal() {
//     document.getElementById('Modal-add-product').style.display = 'none';
// }



function imprimirFichas() {
    const element = document.getElementById("list-products-comanda");
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
    //   console.log(content);
      content = content.replace(/<button[^>]*>(?:(?!<\/button>)[\s\S])*<\/button>/gi,'');
      content = content.replace(/<th[^>]*>(?:(?!<\/th>)[\s\S])*<\/th>/gi,'');
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
    // const productId = document.getElementById('0').value;
    // const comandaId = document.getElementById('comanda0').value;
    addProductBalcao()
    reloadPage()
  }
  // else if (event.keyCode == 73){
  //   imprimirFichas()
  // }
  // else if (event.keyCode == 51){
  //   document.getElementById('qtd-product').innerHTML = '3'


}




function addProductBalcao() {
  var productId = document.getElementById('0').innerText;
  var comandaId = document.getElementById('comanda0').innerText;
  var qtd = document.getElementById('qtd-product').value;
  console.log(productId, comandaId)
  const url = `/balcao/addProductBalcaoTeclado${productId}/${comandaId}/${qtd}/`;
  const listProductsBalcao = document.getElementById('list-products-balcao');
  fetch(url, {
    method: 'GET', 
    headers: {
      'Content-Type': 'application/json'
    },

  })



}

// document.getElementById('openModal').addEventListener('click', openModal);



document.getElementById('productForm').addEventListener('submit', function(event) {
    event.preventDefault(); 
});





function salvarValor() {
  const elemento = document.getElementById('qtd-product');
  const chave = 'qtd';
  const valor = elemento.value;
    localStorage.setItem(chave, valor);
    setCookie(chave, valor);
  console.log(chave, valor);

  }
 
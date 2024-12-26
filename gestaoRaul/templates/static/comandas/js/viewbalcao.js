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
document.cookie = 'qtd=1';


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

  reloadPage()
}

// document.getElementById('openModal').addEventListener('click', openModal);



document.getElementById('productForm').addEventListener('submit', function(event) {
    event.preventDefault(); 
});




const qtd = document.getElementById('qtd-product');
qtd.addEventListener('input', () => {
  const chave = 'qtd';
  const valor = qtd.value;
  document.cookie = chave + '=' + valor;
  console.log(chave, valor);
});

 
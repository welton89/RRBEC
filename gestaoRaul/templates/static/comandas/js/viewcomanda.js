function openModal() {
    document.getElementById('Modal-add-product').style.display = 'block';
}


function open_remove_product_comanda() {
    document.getElementById('remove-product-comanda').style.display = 'block';
}

function closeModal() {
    document.getElementById('Modal-add-product').style.display = 'none';
}


function removeCloseModal() {
    document.getElementById('remove-product-comanda').style.display = 'none';
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



document.getElementById('openModal').addEventListener('click', openModal);

document.getElementById('productForm').addEventListener('submit', function(event) {
    event.preventDefault(); 
});


 
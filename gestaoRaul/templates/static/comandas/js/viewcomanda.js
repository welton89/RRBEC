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
    if (element) {
      var content = element.innerHTML;
      console.log(content);
      content = content.replace(/<button[^>]*>(?:(?!<\/button>)[\s\S])*<\/button>/gi,'');
      const printWindow = window.open('', '_blank');
      printWindow.document.write('<table>'+content+'</table>');
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


 
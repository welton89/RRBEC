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





document.getElementById('openModal').addEventListener('click', openModal);

document.getElementById('productForm').addEventListener('submit', function(event) {
    event.preventDefault(); 


});
 
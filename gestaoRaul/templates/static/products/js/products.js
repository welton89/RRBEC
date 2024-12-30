function openModal() {
    document.getElementById('Modal-create-product').style.display = 'block';
}

function closeModal() {
    document.getElementById('Modal-create-product').style.display = 'none';
}

function editProduct(id) {

    var productId = document.getElementById('productId');
    var productName = document.getElementById('productName');
    var productPrice = document.getElementById('productPrice');
    var productDescription = document.getElementById('productDescription');
    var productqtd = document.getElementById('productqtd');
    var categorie = document.getElementById('select-categorie');
    openModal();
    // productId.innerHTML = id;
    productName.value = document.getElementById('name-'+id).innerHTML;
    var preco = document.getElementById('price-'+id).innerHTML;
    preco = preco.replace('R$ ', '');
    preco = preco.replace(',', '.');
    productPrice.value = preco;
    // productDescription.value = document.getElementById('description-'+id).innerHTML;
    productqtd.value = document.getElementById('quantity-'+id).innerHTML;
    categorie.value = 2;

    // const url = `/products/editProduct/${id}/`;
    // // window.location.href = url;
    // fetch(url, {
    //     method: 'POST', 
    //     headers: {
    //       'Content-Type': 'application/json'
    //     },}).then(function(response) {
    //     return response.text();
    //     })




    //     .then(function(text) {
    //     var listProductsBalcaoElement = document.getElementById("list-products-balcao");
    //     listProductsBalcaoElement.innerHTML = text;
    //   })
}

// document.getElementById('openModal').addEventListener('click', openModal);

// document.getElementById('productForm').addEventListener('submit', function(event) {
//     event.preventDefault(); 

    // const productName = document.getElementById('productName').value;
    // const productPrice = document.getElementById('productPrice').value;
    // const productDescription = document.getElementById('productDescription').value;

    // closeModal();
// }
// );
 
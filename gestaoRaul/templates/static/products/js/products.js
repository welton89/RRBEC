function openModal() {
    document.getElementById('Modal-create-product').style.display = 'block';
    var productId = document.getElementById('productId');
    var productName = document.getElementById('productName');
    var productPrice = document.getElementById('productPrice');
    var productDescription = document.getElementById('productDescription');
    var productqtd = document.getElementById('productqtd');
    var productCuisine = document.getElementById('cuisine');

    var categorie = document.getElementById('select-categorie');
    var buttonEdit = document.getElementById('edit');
    var buttonSave = document.getElementById('save');
    buttonEdit.style.display = 'none';
    buttonSave.style.display = 'block';

    productId.value = '';
    productName.value = '';
    productPrice.value = '';
    productDescription.value ='';
    productqtd.value = '';
    productCuisine.checked = false
    categorie.value = 1;
}

function closeModal() {
    document.getElementById('Modal-create-product').style.display = 'none';
}

function editProduct(id) {

    openModal();
    var buttonSave = document.getElementById('save');
    var buttonEdit = document.getElementById('edit');
    buttonSave.style.display = 'none';
    buttonEdit.style.display = 'block';
    var productId = document.getElementById('productId');
    var productName = document.getElementById('productName');
    var productPrice = document.getElementById('productPrice');
    var productDescription = document.getElementById('productDescription');
    var productqtd = document.getElementById('productqtd');
    var productCuisine = document.getElementById('cuisine');
    var categorie = document.getElementById('select-categorie');

    productId.value = id;
    productName.value = document.getElementById('name-'+id).innerHTML;
    var preco = document.getElementById('price-'+id).innerHTML;
    preco = preco.replace('R$ ', '');
    preco = preco.replace(',', '.');
    productPrice.value = preco;
    productDescription.value = document.getElementById('description-'+id).value;
    productqtd.value = document.getElementById('quantity-'+id).innerHTML;
    productCuisine.checked = document.getElementById('cuisine-'+id).value == 'True' ? true : false;
    categorie.value = document.getElementById('h-category-'+id).value;

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
 
function openModal() {
    document.getElementById('Modal-create-product').style.display = 'block';
}

function closeModal() {
    document.getElementById('Modal-create-product').style.display = 'none';
}

document.getElementById('openModal').addEventListener('click', openModal);

// document.getElementById('productForm').addEventListener('submit', function(event) {
//     event.preventDefault(); 

    // const productName = document.getElementById('productName').value;
    // const productPrice = document.getElementById('productPrice').value;
    // const productDescription = document.getElementById('productDescription').value;

    // closeModal();
// }
// );
 
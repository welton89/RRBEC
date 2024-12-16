function openModal() {
    document.getElementById('Modal-create-comanda').style.display = 'block';
    // HTMLDialogElement.show()
    // HTMLDialogElement.showModal()
}

function closeModal() {
    document.getElementById('Modal-create-comanda').style.display = 'none';
}

document.getElementById('openModal').addEventListener('click', openModal);

// document.getElementById('form-comanda').addEventListener('submit', function(event) {
//     event.preventDefault(); 

    // const productName = document.getElementById('productName').value;
    // const productPrice = document.getElementById('productPrice').value;
    // const productDescription = document.getElementById('productDescription').value;

    // closeModal();
// }
// );
 
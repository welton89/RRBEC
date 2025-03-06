

function openModal() {
    document.getElementById('Modal-create-comanda').style.display = 'block';
    textField = document.getElementById('name-comanda')
    textField.focus()

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
 


function mostrarNotificacao(titulo,corpo,grupo) {
    if (Notification.permission != 'granted') {
        Notification.requestPermission().then(function(permission) {
            if (permission == 'granted') {
                var notification = new Notification(titulo, {
                    body: corpo,
                    icon: 'https://example.com/icon.png'
                });
            }
        });
    } else {
        var notification = new Notification(titulo, {
            body: corpo,
            icon: 'https://imagecolorpicker.com/imagecolorpicker-preview_b.avif',
            image: 'https://imagecolorpicker.com/imagecolorpicker-preview_b.avif',
            
        });
    }
}


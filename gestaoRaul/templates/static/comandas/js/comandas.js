
document.cookie = `pronto=0`; 



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

function notificacao(){
 
  var resposta =   fetch(`/comandas/notificacao/`, {method: 'GET',
    headers: {'Content-Type': 'application/json',
     },})
     .then(response => response.json())
      .then(data => {
          if (data['notificacao'] == 'true'){
            console.log('verdadeiro')
            document.cookie = `pronto=${data['pronto']}`; 
            mostrarNotificacao(data['titulo'], data['corpo'],'Garçom')
            texto = new SpeechSynthesisUtterance(data['corpo']+', para '+data['titulo']+' tá pronto.');
            window.speechSynthesis.speak(texto);
            console.log(data['notificacao'])
            
        }else{
            document.cookie = `pronto=${data['pronto']}`; 
            console.log('falso')
            console.log(data['notificacao'])
          }
      })
   .catch(error => {
     alert('Erro verificar notificação:', error,data['notificacao'])
   });
   
  }


setInterval(()=> {
    notificacao()
}, 10000)



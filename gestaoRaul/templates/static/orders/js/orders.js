
function reloadPage(){
  setTimeout(function() {
    location.reload();}, 3000);
}

function openTab(evt, etapa) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
      tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
      tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    document.getElementById(etapa).style.display = "block";
    evt.currentTarget.className += " active";
  }

  function displayBlock(etapa) {

    document.getElementById('loading').style.display = "none";
    document.getElementById(etapa).style.display = "block";
  }


  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }
  tabcontent[0].style.display = "block";


  function delayTab(tab){
    document.getElementById('Fila').style.display = "none";
    document.getElementById('Preparo').style.display = "none";
    document.getElementById('Finalizado').style.display = "none";
    document.getElementById('Entregue').style.display = "none";
    document.getElementById('loading').style.display = "block";
  
    
        setTimeout(function() {
      displayBlock(tab);}, 1000);
      // reloadPage();
  }


  displayBlock('Fila');


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

// function notificacao(){
 
//   var resposta =   fetch(`/pedidos/notificacao/`, {method: 'GET',
//     headers: {'Content-Type': 'application/json',
//      },})
//      .then(response => response.json())
//       .then(data => {
//           if (data['notificacao'] == 'true'){
//             document.cookie = `fila=${data['fila']}`; 
//             mostrarNotificacao(data['titulo'], data['corpo'],'Cozinha')
//             texto = new SpeechSynthesisUtterance(data['corpo']+', '+data['titulo']+'.');
//             window.speechSynthesis.speak(texto);
//             reloadPage();

//           }else{
//             console.log(data['notificacao'])
//             console.log('notificação foi false')
//           }
//       })
//    .catch(error => {
//      alert('Erro verificar notificação:', error)
//      console.error('Erro verificar notificação:', error);
//    });
   
//   }


// setInterval(()=> {
//   notificacao()
// }, 10000)




// setTimeout(function() {
//   mostrarNotificacao();}, 2000);


  // mostrarNotificacao()
  // notificacao()
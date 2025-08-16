

document.addEventListener('DOMContentLoaded', function() {
  const navToggle = document.querySelector('.nav-toggle');
  const navLinks = document.querySelector('.nav-links');

  if (navToggle) {
    navToggle.addEventListener('click', function() {
      navLinks.classList.toggle('active');
    });
  }
  document.addEventListener('click', function(event) {
    if (navLinks.classList.contains('active') && !navLinks.contains(event.target) && !navToggle.contains(event.target)) {
      navLinks.classList.remove('active');
    }
  });
});







// const websocket = new WebSocket('ws://192.168.0.150:8765');
// const nomeUsuario = document.getElementById('user-info').textContent;

// websocket.addEventListener('open', (event) => {
//   console.log('Conectado ao servidor WebSocket');
// });

// websocket.addEventListener('message', (event) => {
//   const data = JSON.parse(event.data);

//   switch (data.local) {
//     case 'cozinha':

//       if (document.getElementById('Fila') !== null && data.tipo === 'add'){


//         var novoElemento = document.createElement('div');
//         novoElemento.innerHTML = data.message;
//         document.getElementById('Fila').appendChild(novoElemento); 
//         let valorAtual = document.cookie.replace(/(?:(?:^|.*;\s*)notificacao\s*\=\s*([^;]*).*$)|^.*$/, "$1");
//         if (valorAtual === 'true') {
//           texto = new SpeechSynthesisUtterance(data.speak);
//           window.speechSynthesis.speak(texto);
//           // setTimeout(function() {
//           //   location.reload();
//           // }, 6000);
//         }
//       }
//       else if (document.getElementById('obs-'+data.id) !== null && data.tipo === 'edit'){
//         const obs = document.getElementById('obs-'+data.id)
//         const card = obs.parentNode;
//         card.style.backgroundColor = 'rgb(243, 165, 75)';
//         obs.innerHTML = data.message;
//         let valorAtual = document.cookie.replace(/(?:(?:^|.*;\s*)notificacao\s*\=\s*([^;]*).*$)|^.*$/, "$1");

//         if (valorAtual === 'true') {
//         texto = new SpeechSynthesisUtterance(data.speak);
//         window.speechSynthesis.speak(texto);
//         // setTimeout(function() {
//         //   location.reload();
//         // }, 6000);
//         }
//       }
//       else if (document.getElementById('m-card-'+data.id) !== null && data.tipo === 'delete'){
//         // const card = document.getElementById('m-card-'+data.id)
//         // card.style.backgroundColor = 'rgb(253, 69, 69)';
//         let valorAtual = document.cookie.replace(/(?:(?:^|.*;\s*)notificacao\s*\=\s*([^;]*).*$)|^.*$/, "$1");
//         if (valorAtual === 'true') {
//         texto = new SpeechSynthesisUtterance(data.speak);
//         window.speechSynthesis.speak(texto);
//         setTimeout(function() {
//           location.reload();
//         }, 6000);
//         }
//       }
      
//       break;
//     case 'praca':
//       console.log('Mensagem para a praca:', data);
//       break;
//       case 'guarita':
//         console.log('Mensagem para a guarita:', data);
//         break;
//         case 'balcao':
//       console.log('Mensagem para a balcao:', data);
//       break;
//     default:
//       console.log('Local desconhecido:', data);
//   }

// });
// websocket.addEventListener('error', (event) => {
//   console.error('Erro no WebSocket:', event);
// });
// websocket.addEventListener('close', (event) => {
//     console.log("conexão fechada");
// });



function menuShow() {
    let menuMobile = document.querySelector('.mobile-menu');
    if (menuMobile.classList.contains('open')) {
        menuMobile.classList.remove('open');
        document.querySelector('.icon').src = "https://raw.githubusercontent.com/Larissakich/menu_responsivo/6e3b09504434628c1b01f65b7d8ccf6ace3225cb/menu%20responsivo/assets/img/menu_white_36dp.svg";
    } else {
        menuMobile.classList.add('open');
        document.querySelector('.icon').src = "https://raw.githubusercontent.com/Larissakich/menu_responsivo/6e3b09504434628c1b01f65b7d8ccf6ace3225cb/menu%20responsivo/assets/img/close_white_36dp.svg";
    }
}


var elem = document.getElementById("all");
function openFullscreen() {
    if (elem.requestFullscreen) {
      elem.requestFullscreen();
    } else if (elem.webkitRequestFullscreen) { 
      elem.webkitRequestFullscreen();
    } else if (elem.msRequestFullscreen) { 
      elem.msRequestFullscreen();
    }
  }

  function showToast(message, type ,duration = 2500) {
    const toast = document.getElementById('toast');
  
    if (type === 'success') {
      toast.style.backgroundColor = '#28a745';
    } else if (type === 'error') {
      toast.style.backgroundColor = '#dc3545';
    } else if (type === 'info') {
      toast.style.backgroundColor = '#ffc107';
    }
  
  
    const toastMessage = document.getElementById('toast-message');
  
    toastMessage.textContent = message;
    toast.classList.add('show');
  
    setTimeout(() => {
      toast.classList.remove('show');
    }, duration);
  }


  function feedback(message, icon, subMessage) {
    var feedbackMsg = Swal.fire({
        color: 'white',
        title: message,
        text: subMessage || '',
        icon: icon || 'info',
        background: 'rgb(23, 38, 54)',
        confirmButtonColor: 'linear-gradient(145deg, #1E2A3B, #2C3E50)', 
            });


}
function toast(){

    const Toast = Swal.mixin({
      toast: true,
      theme:"dark",
      position: "top",
      showConfirmButton: false,
      background: 'rgb(30, 42, 58)',
      color: 'white',
      showCloseButton: true,
      timer: 2500,
      timerProgressBar: true,
      didOpen: (toast) => {
        toast.onmouseenter = Swal.stopTimer;
        toast.onmouseleave = Swal.resumeTimer;
      }
    });
    return Toast;
    }
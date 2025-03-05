function verificarCookieNotificacao() {
  console.log('cookie notificacao verificado');
  if (document.cookie.indexOf('notificacao=') === -1) {
    document.cookie = 'notificacao=true; expires=Fri, 31 Dec 9999 23:59:59 GMT; path=/';
    var iconNotify = document.getElementById('icon-notify');
    iconNotify.style.backgroundColor = 'green';
    console.log('cookie notificacao criado');
  }else{
    let valorAtual = document.cookie.replace(/(?:(?:^|.*;\s*)notificacao\s*\=\s*([^;]*).*$)|^.*$/, "$1");
    var iconNotify = document.getElementById('icon-notify');
    iconNotify.style.backgroundColor = valorAtual === 'true' ? 'green' : 'red';
  }
}
verificarCookieNotificacao();

function cookieNotificacao() {
  if (document.cookie.indexOf('notificacao=') !== -1) {
    let valorAtual = document.cookie.replace(/(?:(?:^|.*;\s*)notificacao\s*\=\s*([^;]*).*$)|^.*$/, "$1");
    var iconNotify = document.getElementById('icon-notify');
    let novoValor = valorAtual === 'true' ? 'false' : 'true';
    if (novoValor === 'true') {
      iconNotify.style.backgroundColor = 'green';
    }else{
      iconNotify.style.backgroundColor = 'red';
    }
    document.cookie = 'notificacao=' + novoValor + '; expires=Fri, 31 Dec 9999 23:59:59 GMT; path=/';
  } else {
    document.cookie = 'notificacao=true; expires=Fri, 31 Dec 9999 23:59:59 GMT; path=/';
  }
}

const websocket = new WebSocket('ws://192.168.1.150:8765');
const nomeUsuario = document.getElementById('user-info').textContent;

websocket.addEventListener('open', (event) => {
  console.log('Conectado ao servidor WebSocket');
});

websocket.addEventListener('message', (event) => {
  const data = JSON.parse(event.data);

  switch (data.local) {
    case 'cozinha':
      if (document.getElementById('Fila') !== null && data.tipo === 'add'){
        const novoElemento = document.createElement('div');
        novoElemento.innerHTML = data.message;
        var fila = document.getElementById('Fila').appendChild(novoElemento); 
        let valorAtual = document.cookie.replace(/(?:(?:^|.*;\s*)notificacao\s*\=\s*([^;]*).*$)|^.*$/, "$1");
        if (valorAtual === 'true') {
          
          texto = new SpeechSynthesisUtterance(data.speak);
          window.speechSynthesis.speak(texto);
        }
        console.log('Mensagem recebida:', data.local);
      }
      else if (document.getElementById('obs-'+data.id) !== null && data.tipo === 'edit'){
        const obs = document.getElementById('obs-'+data.id)
        const card = obs.parentNode;
        card.style.backgroundColor = 'rgb(243, 165, 75)';
        obs.innerHTML = data.message;
        let valorAtual = document.cookie.replace(/(?:(?:^|.*;\s*)notificacao\s*\=\s*([^;]*).*$)|^.*$/, "$1");

        if (valorAtual === 'true') {
        texto = new SpeechSynthesisUtterance(data.speak);
        window.speechSynthesis.speak(texto);
        }
        console.log('Mensagem recebida:', data.local);
      }
      else if (document.getElementById('m-card-'+data.id) !== null && data.tipo === 'delete'){
        const card = document.getElementById('m-card-'+data.id)
        card.style.backgroundColor = 'rgb(253, 69, 69)';
        // obs.innerHTML = data.message;
        let valorAtual = document.cookie.replace(/(?:(?:^|.*;\s*)notificacao\s*\=\s*([^;]*).*$)|^.*$/, "$1");

        if (valorAtual === 'true') {
        texto = new SpeechSynthesisUtterance(data.speak);
        window.speechSynthesis.speak(texto);
        }
        console.log('Mensagem recebida:', data.local);
      }
      
      break;
    case 'praca':
      console.log('Código a ser executado se expressao === valor2')
      break;
    case 'guarita':
      // Código a ser executado se expressao === valor3
      break;
    case 'balcao':
      // Código a ser executado se expressao === valor3
      break;
    default:
      console.log('Local desconhecido:', data);
  }






});

websocket.addEventListener('error', (event) => {
  console.error('Erro no WebSocket:', event);
});

websocket.addEventListener('close', (event) => {
    console.log("conexão fechada");
});





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

  function showToast(message, type ,duration = 3000) {
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
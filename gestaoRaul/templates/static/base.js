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
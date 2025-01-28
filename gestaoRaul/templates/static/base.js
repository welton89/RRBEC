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

function entrar(){
    alert('Onde tu pensa que vai entrar?🤨');
}
var elem = document.getElementById("all");
function openFullscreen() {
    if (elem.requestFullscreen) {
      elem.requestFullscreen();
    } else if (elem.webkitRequestFullscreen) { /* Safari */
      elem.webkitRequestFullscreen();
    } else if (elem.msRequestFullscreen) { /* IE11 */
      elem.msRequestFullscreen();
    }
  }

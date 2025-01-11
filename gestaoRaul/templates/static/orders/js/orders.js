function openTab(evt, etapa) {
    // Declarar todas as abas e conteúdos
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
      tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
      tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    // Mostrar o conteúdo da aba selecionada e marcar a aba como ativa
    document.getElementById(etapa).style.display = "block";
    evt.currentTarget.className += " active";
    // console.log(evt.currentTarget.className += " active");
  }


  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }
  tabcontent[0].style.display = "block";
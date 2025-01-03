document.addEventListener('dragstart', (e) => {
    e.target.classList.add('dragging');
});

document.addEventListener('dragover', (e) => {
    e.preventDefault();
    const target = e.target;
    if (target.classList.contains('column')) {
        target.style.backgroundColor = ''; 
    }
});

document.addEventListener('dragend', (e) => {
    e.target.classList.remove('dragging');
    document.querySelectorAll('.column').forEach(column => {
        column.style.backgroundColor = '';
    });
});

document.addEventListener('drop', (e) => {
    e.preventDefault();
    const draggable = document.querySelector('.dragging');
    e.target.appendChild(draggable);
});
function manipularCards() {
  const cards = document.querySelectorAll('.m-card');

  cards.forEach(card => {
    const input = card.querySelector('input');
    const inputValue = input.value; 
    const targetElement = document.getElementById(inputValue); 

    if (targetElement) {
      targetElement.appendChild(card);
    } else {
      console.error(`Elemento com ID ${inputValue} não encontrado.`);
    }
  });
}

function saveLocal() {
  const draggedElement = event.dataTransfer.getData('text/plain');

const mesaElement = event.target;
const targetElement = event.target.parentNode;
const mesaId = mesaElement.id
const targetId = targetElement.id;
const parentNodeClass = targetElement.classList.value
console.log(parentNodeClass)


if (parentNodeClass == 'espaco' || targetId == 'drop'){

const url = `/mesas/locationMesa/${mesaId}/${targetId}/`;
var resposta =   fetch(url, {method: 'POST',
   headers: {'Content-Type': 'application/json',
    'X-CSRFToken': document.querySelector('[name="csrfmiddlewaretoken"]').value
    },}).then(response => response.json())
  .then(data => {
    if(data.status != 'ok'){
      alert('Erro ao salvar local:', error)
    }
  })
  .catch(error => {
    alert('Erro ao salvar local:', error)
    console.log(document.cookie)
    console.error('Erro ao salvar local:', error);
  });
}else{
  alert('Aqui não pode!!!')
  location.reload();
}

}

setTimeout(function() {
  manipularCards();}, 1);

  setTimeout()
  
  


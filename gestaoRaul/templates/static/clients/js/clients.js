function openModal() {
    document.getElementById('Modal-create-client').style.display = 'block';
    var clientId = document.getElementById('clientId');
    var clientName = document.getElementById('clientName');
    var clientDebt = document.getElementById('clientDebt');
    var clientContact = document.getElementById('clientContact');
    var clientActive = document.getElementById('active');

    var buttonEdit = document.getElementById('edit');
    var buttonSave = document.getElementById('save');
    buttonEdit.style.display = 'none';
    buttonSave.style.display = 'block';

    clientId.value = '';
    clientName.value = '';
    // clientDebt.value = '';
    clientContact.value ='';
    clientActive.checked = false
}

function reloadPage(){
    setTimeout(function() {
      location.reload();}, 100);
  }

function closeModal() {
    reloadPage()
    // document.getElementById('Modal-create-client').style.display = 'none';
}

function editclient(id) {
    openModal();
    var buttonSave = document.getElementById('save');
    var buttonEdit = document.getElementById('edit');
    var titleWindow = document.getElementById('title-window')
    buttonSave.style.display = 'none';
    buttonEdit.style.display = 'block';
    titleWindow.innerText = 'Editar '
    var clientId = document.getElementById('clientId');
    var clientName = document.getElementById('clientName');
    var clientContact = document.getElementById('clientContact');
    var clientActive = document.getElementById('active');
    
    clientId.value = id;
    clientName.value = document.getElementById('name-'+id).innerHTML;

    console.log(document.getElementById('contact-'+id).innerText)
    clientContact.value = document.getElementById('contact-'+id).innerText;
    clientActive.checked = document.getElementById('active-'+id).innerText == 'True' ? true : false;


}






function calcularTotalSelecionado() {
    let total = 0;
    // Seleciona todos os checkboxes marcados (exceto o "selectAll")
    const checkboxes = document.querySelectorAll('input[type="checkbox"]:checked:not(#selectAll)');
    
    checkboxes.forEach(checkbox => {
        const row = checkbox.closest('tr');
        const valorCell = row.querySelector('td:nth-child(7)'); // 7ª coluna é o valor
        if (valorCell) {
            const valorText = valorCell.textContent.trim();
            // Remove possíveis formatações de moeda e converte para número
            const valor = parseFloat(
                valorText
                    .replace('.',',')
                    .replace(/[^\d,]/g, '')
                    .replace(',', '.')

            );
            if (!isNaN(valor)) {
                total += valor;
            }
        }
    });
    console.log(total)
    
    // Exibe o total na tela (você pode ajustar onde mostrar)
    const totalElement = document.getElementById('total-selecionado');
    if (totalElement) {
        totalElement.textContent = total.toLocaleString('pt-BR', {style: 'currency', currency: 'BRL'});
    } else {
        // Cria um elemento para mostrar o total se não existir
        const display = document.createElement('div');
        display.id = 'total-selecionado';
        display.style.margin = '10px';
        display.style.fontWeight = 'bold';
        display.textContent = `Total selecionado: ${total.toLocaleString()}`;
        document.querySelector('table').insertAdjacentElement('afterend', display);
    }
    
    return total;
}

// Adiciona evento de change a todos os checkboxes
document.addEventListener('DOMContentLoaded', function() {

    const checkboxes = document.querySelectorAll('input[type="checkbox"]');
    checkboxes.forEach(checkbox => {
        checkbox.addEventListener('change', calcularTotalSelecionado);
    });
});





document.addEventListener('DOMContentLoaded', function() {
    const selectAll = document.getElementById('selectAll');
    if (selectAll) {
        selectAll.addEventListener('change', function() {
            const isChecked = this.checked;
            const checkboxes = document.querySelectorAll('input[type="checkbox"]:not(#selectAll)');
            
            checkboxes.forEach(checkbox => {
                checkbox.checked = isChecked;
            });
            
            // Dispara o evento para calcular o total
            calcularTotalSelecionado();
        });
    }
    
    // Adiciona evento para desmarcar "selectAll" se algum checkbox for desmarcado
    const checkboxes = document.querySelectorAll('input[type="checkbox"]:not(#selectAll)');
    checkboxes.forEach(checkbox => {
        checkbox.addEventListener('change', function() {
            if (!this.checked && selectAll.checked) {
                selectAll.checked = false;
            }
        });
    });
});




async function enviarComandasSelecionadas() {
    const btn = document.getElementById('btn-fechar-comandas');
    const feedback = document.getElementById('api-feedback');
    
    btn.disabled = true;
    btn.innerHTML = '<span class="icon">⏳</span> Processando...';
    
    try {
        const checkboxes = document.querySelectorAll('input[type="checkbox"]:checked:not(#selectAll)');
        const ids = [];
        
        checkboxes.forEach(checkbox => {
            const id = checkbox.id;
            if (/^\d+$/.test(id)) {
                ids.push(parseInt(id));
            }
        });
        
        if (ids.length === 0) {
            feedback.textContent = 'Nenhuma comanda válida selecionada.';
            feedback.className = 'feedback-message error';
            return;
        }

        const response = await fetch('http://192.168.1.150:8001/clients/payDebt', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-Requested-With': 'XMLHttpRequest',
                'X-CSRFToken': getCookie('csrftoken'),
            },
            body: JSON.stringify({ ids: ids })
        });
        
        // Verifica se a resposta é JSON válido
        const text = await response.text();
        let data;
        try {
            data = JSON.parse(text);
        } catch (e) {
            throw new Error(`Resposta inválida do servidor: ${text.substring(0, 100)}...`);
        }
        
        if (!response.ok) {
            throw new Error(data.error || `Erro HTTP: ${response.status}`);
        }
        
        feedback.textContent = data.message || `${ids.length} comandas processadas com sucesso!`;
        feedback.className = 'feedback-message success';
        
        setTimeout(() => {
            window.location.reload();
        }, 2000);
        
    } catch (error) {
        console.error('Erro:', error);
        feedback.textContent = error.message || 'Erro ao processar comandas. Verifique o console para mais detalhes.';
        feedback.className = 'feedback-message error';
    } finally {
        btn.disabled = false;
        btn.innerHTML = '<span class="icon">✓</span> Fechar Comandas Selecionadas';
    }
}

// Função auxiliar para pegar o token CSRF
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// Exemplo de como chamar a função (pode ser vinculada a um botão)
// document.getElementById('btn-fechar-comandas').addEventListener('click', enviarComandasSelecionadas);
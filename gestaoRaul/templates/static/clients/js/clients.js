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
    clientDebt.value = '';
    clientContact.value ='';
    clientActive.checked = false
}

function closeModal() {
    document.getElementById('Modal-create-client').style.display = 'none';
}

function editclient(id) {

    openModal();
    var buttonSave = document.getElementById('save');
    var buttonEdit = document.getElementById('edit');
    buttonSave.style.display = 'none';
    buttonEdit.style.display = 'block';
    var clientId = document.getElementById('clientId');
    var clientName = document.getElementById('clientName');
    var clientDebt = document.getElementById('clientDebt');
    var clientContact = document.getElementById('clientContact');
    var clientqtd = document.getElementById('clientqtd');
    var clientActive = document.getElementById('active');
    var categorie = document.getElementById('select-categorie');

    clientId.value = id;
    clientName.value = document.getElementById('name-'+id).innerHTML;
    var preco = document.getElementById('debt-'+id).innerHTML;
    preco = preco.replace('R$ ', '');
    preco = preco.replace(',', '.');
    clientDebt.value = preco;
    clientContact.value = document.getElementById('contact-'+id).value;
    clientqtd.value = document.getElementById('quantity-'+id).innerHTML;
    clientActive.checked = document.getElementById('Active-'+id).value == 'True' ? true : false;
    categorie.value = document.getElementById('h-category-'+id).value;


}


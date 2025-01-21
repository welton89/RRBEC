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


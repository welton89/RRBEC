function openModal() {
    document.getElementById('Modal-create-product').style.display = 'block';
    var productId = document.getElementById('productId');
    var productName = document.getElementById('productName');
    var productPrice = document.getElementById('productPrice');
    var productDescription = document.getElementById('productDescription');
    var productqtd = document.getElementById('productqtd');
    var urlImage = document.getElementById('url-image');
    var imageProduct = document.getElementById('image-product');

    var productCuisine = document.getElementById('cuisine');

    var categorie = document.getElementById('select-categorie');
    var buttonEdit = document.getElementById('edit');
    var buttonSave = document.getElementById('save');
    buttonEdit.style.display = 'none';
    buttonSave.style.display = 'block';

    productId.value = '';
    productName.value = '';
    productPrice.value = '';
    productDescription.value ='';
    productqtd.value = '';
    urlImage.value = '';
    productCuisine.checked = false
    categorie.value = 1;
}

function closeModal() {
    document.getElementById('Modal-create-product').style.display = 'none';
}

function editProduct(id) {

    openModal();
    var buttonSave = document.getElementById('save');
    var buttonEdit = document.getElementById('edit');
    buttonSave.style.display = 'none';
    buttonEdit.style.display = 'block';
    var productId = document.getElementById('productId');
    var productName = document.getElementById('productName');
    var productPrice = document.getElementById('productPrice');
    var productDescription = document.getElementById('productDescription');
    var productqtd = document.getElementById('productqtd');
    var urlImage = document.getElementById('url-image');
    var imageProduct = document.getElementById('modal-product');


    var productCuisine = document.getElementById('cuisine');
    var categorie = document.getElementById('select-categorie');

    productId.value = id;
    productName.value = document.getElementById('name-'+id).innerHTML;
    var preco = document.getElementById('price-'+id).innerHTML;
    preco = preco.replace('R$ ', '');
    preco = preco.replace(',', '.');
    productPrice.value = preco;
    productDescription.value = document.getElementById('description-'+id).value;
    productqtd.value = document.getElementById('quantity-'+id).innerHTML;
    urlImage.value = document.getElementById('image-'+id).innerHTML;
    imageProduct.style.backgroundImage = urlImage.value != '' ?`url('${urlImage.value}'`  : `url('https://placehold.co/600x800/efc7b8/49291c?text=${productName.value}')`;
    productCuisine.checked = document.getElementById('cuisine-'+id).value == 'True' ? true : false;
    categorie.value = document.getElementById('h-category-'+id).value;

    // const url = `/products/editProduct/${id}/`;
    // // window.location.href = url;
    // fetch(url, {
    //     method: 'POST', 
    //     headers: {
    //       'Content-Type': 'application/json'
    //     },}).then(function(response) {
    //     return response.text();
    //     })




    //     .then(function(text) {
    //     var listProductsBalcaoElement = document.getElementById("list-products-balcao");
    //     listProductsBalcaoElement.innerHTML = text;
    //   })
}

// document.getElementById('openModal').addEventListener('click', openModal);

// document.getElementById('productForm').addEventListener('submit', function(event) {
//     event.preventDefault(); 

    // const productName = document.getElementById('productName').value;
    // const productPrice = document.getElementById('productPrice').value;
    // const productDescription = document.getElementById('productDescription').value;

    // closeModal();
// }
// );
 
function listerSortTeable(){
    


// document.addEventListener('DOMContentLoaded', function() {
  const table = document.getElementById('product-list');
  const headers = table.querySelectorAll('th');
  const tbody = table.querySelector('tbody'); // Seleciona o corpo da tabela

  let currentSortColumn = -1; // Armazena o índice da coluna atualmente ordenada
  let sortDirection = 'asc'; // 'asc' para ascendente, 'desc' para descendente

  // Adiciona um ouvinte de evento de clique a cada cabeçalho de coluna
  headers.forEach((header, index) => {
    if (header.textContent.trim() !== 'Ações') {
      header.addEventListener('click', () => {
        // Se a mesma coluna for clicada, inverte a direção da ordenação
        if (currentSortColumn === index) {
          sortDirection = (sortDirection === 'asc') ? 'desc' : 'asc';
        } else {
          // Se uma nova coluna for clicada, define como a coluna atual
          // e inicia a ordenação ascendente
          currentSortColumn = index;
          sortDirection = 'asc';
        }

        // Remove as classes de ordenação de todos os cabeçalhos
        headers.forEach(h => {
          h.classList.remove('sorted-asc', 'sorted-desc');
        });

        // Adiciona a classe de ordenação ao cabeçalho clicado para visualização
        header.classList.add(`sorted-${sortDirection}`);

        // Chama a função de ordenação
        sortColumn(index, sortDirection, header.dataset.colType);
      });
    }
  })

  function sortColumn(columnIndex, direction, columnType) {
    // Converte os NodeList de linhas em um Array para poder usar sort()
    const rows = Array.from(tbody.querySelectorAll('tr'));

    rows.sort((rowA, rowB) => {
      // Obtém o texto da célula na coluna clicada para ambas as linhas
      let valueA = rowA.children[columnIndex].textContent.trim();
      let valueB = rowB.children[columnIndex].textContent.trim();

      // Trata valores específicos para colunas como "Preço" que têm "R$"
      if (columnIndex === 1) { // Índice da coluna "Preço"
        valueA = valueA.replace('R$', '').trim();
        valueB = valueB.replace('R$', '').trim();
      }

      // Converte para número se o tipo da coluna for "number"
      // ou se for a coluna de "Preço" após remover "R$"
      if (columnType === 'number' || columnIndex === 1) {
        valueA = parseFloat(valueA);
        valueB = parseFloat(valueB);
        // Garante que NaN (Not a Number) sejam tratados para evitar problemas de ordenação
        valueA = isNaN(valueA) ? -Infinity : valueA;
        valueB = isNaN(valueB) ? -Infinity : valueB;
      } else {
        // Para texto, use localeCompare para ordenação correta com caracteres acentuados
        // e torna minúsculo para ordenação case-insensitive
        valueA = valueA.toLowerCase();
        valueB = valueB.toLowerCase();
      }

      let comparison = 0;
      if (valueA > valueB) {
        comparison = 1;
      } else if (valueA < valueB) {
        comparison = -1;
      }

      // Aplica a direção da ordenação
      return (direction === 'asc') ? comparison : -comparison;
    });

    // Remove todas as linhas existentes e adiciona as linhas ordenadas de volta ao tbody
    while (tbody.firstChild) {
      tbody.removeChild(tbody.firstChild);
    }
    rows.forEach(row => tbody.appendChild(row));
  }
// });
}

listerSortTeable();

var barColors = ["red", "green","blue","orange","brown"];

var chartVendas = new Chart("vendas", {
  type: "bar",
  data: {
    labels: [],
    datasets: [{
      data: [],
      backgroundColor: barColors,
    }]
  },
  options: {
    legend: {display: false},
    title: {
      display: true,
      text: "Produtos mais vendidos"
    },
    
  }
});

var chartCuisine = new Chart("cuisine", {
  type: "doughnut",
  data: {
    labels: [],
    datasets: [{
      backgroundColor: barColors,
      data: []
    }]
  },
  options: {
    legend: {display: true},
    title: {
      display: true,
      text: "Tempo médio (em minutos) do pedido em cada etapa."
    },
  }
});


function getDataAtualFormatada() {
  const data = new Date();

  const ano = data.getFullYear();
  const mes = String(data.getMonth() + 1).padStart(2, '0'); // Mês começa em 0
  const dia = String(data.getDate()).padStart(2, '0');

  const dataFormatada = `${ano}-${mes}-${dia}`;

  return dataFormatada;
}

function productsPlus(){

var xValues = [document.getElementById('n-0').innerText,
    document.getElementById('n-1').innerText,
    document.getElementById('n-2').innerText, 
    document.getElementById('n-3').innerText, 
    document.getElementById('n-4').innerText
    ];
var yValues = [document.getElementById('q-0').innerText, 
    document.getElementById('q-1').innerText, 
    document.getElementById('q-2').innerText, 
    document.getElementById('q-3').innerText, 
    document.getElementById('q-4').innerText
];
var barColors = ["red", "green","blue","orange","brown"];

// new Chart("vendas", {
//     type: "bar",
//     data: {
//       labels: xValues,
//       datasets: [{
//         backgroundColor: barColors,
//         data: yValues
//       }]
//     },
//     options: {
//       legend: {display: false},
//       title: {
//         display: true,
//         text: "Produtos mais vendidos"
//       },
      
//     }
//   });
}


function mediaCuisine(){
var dateStart = document.getElementById('data-start').value == '' ? '2025-01-01' :document.getElementById('data-start').value;
var dateEnd = document.getElementById('data-end').value == '' ? getDataAtualFormatada() :document.getElementById('data-end').value;;
var yValues = [];
var xValues = ['Fila', 'Preparando', 'Entregar'];
var totalPagamenstos = document.getElementById('total-pagamentos')
var qtdPagamentos = document.getElementById('qtd-pagamentos')
var ticketMedio = document.getElementById('ticket-medio')

var resposta =   fetch(`/chartCuisine/${dateStart}/${dateEnd}`, {method: 'GET',
  headers: {'Content-Type': 'application/json',
   },})
   .then(response => response.json())
    .then(data => {
      yValues = []
      yValues.push(data['mediaFila'])
      yValues.push(data['mediaPreparando'])
      yValues.push(data['mediaFinalizado'])
      var totalP = data['total_pagamentos'] ?? '0,00'
      var qtdP = data['qtd_pagamentos'] ?? '0'
      var tocketP = data['ticket_medio'] ?? '0'
      qtdPagamentos.innerText = qtdP
      totalPagamenstos.innerText = 'R$ ' + totalP
      ticketMedio.innerText = 'R$ ' + tocketP
      var produtos_mais_vendidos = data.produtos_mais_vendidos
      
      var chaves = Object.keys(produtos_mais_vendidos);
      var valores = [];
      
      for (const chave of chaves) {
        valores.push(produtos_mais_vendidos[chave]);
      }

      chartVendas.data.datasets[0].data = valores
      chartVendas.data.labels = chaves
      chartVendas.update();
      
      chartCuisine.data.datasets[0].data = yValues
      chartCuisine.data.labels = xValues
      chartCuisine.update();

    })
 .catch(error => {
   alert('Erro ao trazer dados da cozinha:', error)
   console.error('Erro ao trazer dados da cozinha:', error);
 });
 
}

function deleyGraficos(){
  setTimeout(function() {
    mediaCuisine();}, 20000);
}
mediaCuisine()

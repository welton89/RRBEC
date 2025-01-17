

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

new Chart("vendas", {
    type: "bar",
    data: {
      labels: xValues,
      datasets: [{
        backgroundColor: barColors,
        data: yValues
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
}


function mediaCuisine(){
var dateStart = document.getElementById('data-start').value == '' ? '2025-01-01' :document.getElementById('data-start').value;
var dateEnd = document.getElementById('data-end').value == '' ? '2025-01-15' :document.getElementById('data-end').value;;
var yValues = [];
var xValues = ['Fila', 'Preparando', 'Entregar'];
var barColors = ["red", "green","blue","orange","brown"];

var resposta =   fetch(`/chartCuisine/${dateStart}/${dateEnd}`, {method: 'GET',
  headers: {'Content-Type': 'application/json',
   },})
   .then(response => response.json())
    .then(data => {
      yValues = []
      yValues.push(data['mediaFila'])
      yValues.push(data['mediaPreparando'])
      yValues.push(data['mediaFinalizado'])
      console.log(yValues)
      new Chart("cuisine", {
        type: "doughnut",
        data: {
          labels: xValues,
          datasets: [{
            backgroundColor: barColors,
            data: yValues
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
// productsPlus()
mediaCuisine()

// console.log(document.getElementById('data-start').value)
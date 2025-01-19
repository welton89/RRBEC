
const barColors = ['rgba(252, 52, 95, 0.65)', 
                'rgba(253, 193, 53, 0.65)',
                'rgba(54, 162, 235, 0.65)',
                'rgba(75, 192, 192, 0.65)',
                'rgba(153, 102, 255, 0.65)',];

const barColorsBorder = ['rgba(252, 52, 95)', 
                'rgb(253, 193, 53)',
                'rgb(54, 162, 235)',
                'rgb(75, 192, 192)',
                'rgb(153, 102, 255)',];

var chartVendas = new Chart("vendas", {
  type: "bar",
  data: {
    labels: [],
    datasets: [{
      fill: true,
      // barPercentage: 1.0,
      data: [],
      backgroundColor: barColors,
      borderColor: barColorsBorder,
      borderWidth: 2,
      borderRadius: 8
    }]
  },
  options: {
    
    indexAxis: 'y',
    scales: {
      y: {
        ticks: {
          display: true,

          // color: 'white'
          // padding: 5,
          callback: function(value, index, values) {
            return chartVendas.data.labels[index].substring(0, 6); // Retorna o valor normal do label
          },
        }
      },
      
    },
    legend: {display: false},
    title: {
      display: false,
      text: "Produtos mais vendidos"
    },
    
  },
 
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
      text: "Média (em minutos) do pedido em cada etapa."
    },
  }
});

function faturaMensal() {

  const genericOptions = {
    responsive: true,
    hoverBackgroundColor: 'white',
    hoverRadius: 7,
    hoverBorderWidth: 3,
    onHover: { mode: ['dataset', 'tooltip'] },
    scales: {
      x: { grid: { display: true } },
      y: {
        min: 0,
        max: 200,
        ticks: { stepSize: 50 },
        grid: { borderDash: [5, 5] }
      }
    },
    layout: {
      padding: {
        bottom: 10,
        left: 15,
        right: 25
      }
    },
    interaction: {
      mode: 'index',
      intersect: false
    },
    plugins: {
      legend: { display: true },
      tooltip: {
        padding: 16,
        titleFont: {
          family: "'Poppins', 'sans-serif'",
          size: 18,
          weight: 'normal'
        },
        backgroundColor: 'rgba(8, 26, 81, 1)',
        bodyColor: 'rgba(255, 255, 255, 0.7)',
        bodyFont: {
          family: "'Poppins', 'sans-serif'",
          size: 15
        },
        bodySpacing: 8,
        boxHeight: 6,
        boxPadding: 8,
        usePointStyle: true,
        callbacks: {
          title: ctx => {

            var titulo

            switch (ctx[0].label) {
              case 'Jan':
                titulo = 'Janeiro'
                break;
              case 'Fev':
                titulo = 'Fevereiro'
                break;
              case 'Mar':
                titulo = 'Março'
                break;
              case 'Abr':
                titulo = 'Abril'
                break;
              case 'Mai':
                titulo = 'Maio'
                break;
              case 'Jun':
                titulo = 'Junho'
                break;
              case 'Jul':
                titulo = 'Julho'
                break;
              case 'Ago':
                titulo = 'Agosto'
                break;
              case 'Set':
                titulo = 'Setembro'
                break;
              case 'Out':
                titulo = 'Outubro'
                break;
              case 'Nov':
                titulo = 'Novembro'
                break;
              case 'Dez':
                titulo = 'Dezembro'
                break;
              // ... outros dias
              default:
                console.log("Dia inválido");
            }

            return titulo
          },
          label: ctx => {
            return `${ctx.dataset.label}: R$ ${ctx.raw}`
          }
        }
      }
    }
  }
    
  const lineDash = {
    id: 'lineDash',
    beforeDraw: chart => {
      if (chart.tooltip._active && chart.tooltip._active.length) {
        const ctx = chart.ctx
        ctx.save()
        const activePoint = chart.tooltip._active[0]
  
        ctx.beginPath()
        ctx.setLineDash([5, 5])
        ctx.moveTo(activePoint.element.x, chart.chartArea.top)
        ctx.lineTo(activePoint.element.x, chart.chartArea.bottom)
        ctx.lineWidth = 1
        ctx.strokeStyle = 'rgba(1, 126, 250, 0.8)'
        ctx.stroke()
        ctx.restore()
      }
    }
  }
  
  

var faturamentoMensal = new Chart('mensal', {
  type: "line",
  data: {
    labels: ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'],
    datasets: [
      {
      label: 'Ano Anterior',
      backgroundColor: 'rgba(255, 136, 0, 0.8)',
      borderColor: 'rgba(255, 136, 0, 0.8)',
      borderWidth: 2,
      data: [22, 48, 41, 53, 82, 64, 55, 47, 50, 62, 58, 84],
    },

      {
      label: 'Ano Atual',
      backgroundColor: 'rgba(1, 126, 250, 1)',
      borderColor: 'rgba(1, 126, 250, 1)',
      borderWidth: 2,
      data: [100, 150,80,85,90,70,120,90,100, ]
    },

      {
      label: 'Projeção',
      backgroundColor: 'rgb(1, 250, 13)',
      borderColor: 'rgb(9, 250, 1)',
      borderWidth: 2,
      data: [, ,,,,,,,100, 89, 138, 110 ]
    },

  ]
  },
  options: genericOptions,
  plugins: [ lineDash]

});

}


function getDataAtualFormatada() {
  
  const data = new Date();
  const ano = data.getFullYear();
  const mes = String(data.getMonth() + 1).padStart(2, '0');
  const dia = String(data.getDate()).padStart(2, '0');
  const dataFormatada = `${ano}-${mes}-${dia}`;
  
  const dataAnterior = new Date(data.setDate(data.getDate() - 30));
  const anoAnterior = dataAnterior.getFullYear();
  const mesAnterior = String(dataAnterior.getMonth() + 1).padStart(2, '0');
  const diaAnterior = String(dataAnterior.getDate()).padStart(2, '0');
  const dataFormatadaAnterior = `${anoAnterior}-${mesAnterior}-${diaAnterior}`;

  datas = [dataFormatadaAnterior, dataFormatada]

  return datas;
}



function mediaCuisine(){
var dateStart = document.getElementById('data-start').value == '' ? '2025-01-01' :document.getElementById('data-start').value;
var dateEnd = document.getElementById('data-end').value == '' ? getDataAtualFormatada()[1] :document.getElementById('data-end').value;;
var yValues = [];
var xValues = ['Fila', 'Preparo', 'Entrega'];
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

      document.getElementById('30-days').innerText = ''

    })
 .catch(error => {
   alert('Erro ao trazer dados da cozinha:', error)
   console.error('Erro ao trazer dados da cozinha:', error);
 });
 
}

document.getElementById('data-start').value =  getDataAtualFormatada()[0];
document.getElementById('data-end').value = getDataAtualFormatada()[1];
mediaCuisine()
faturaMensal()
document.getElementById('30-days').innerText = 'Últimos 30 dias'

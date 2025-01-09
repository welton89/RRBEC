

console.log(document.getElementById('n-0'))


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
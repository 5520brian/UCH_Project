const ctx = document.getElementById('myChart')

const myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['LOW', 'MEDIUM', 'HIGH'],
        datasets: [{
            label: '風險數量',
            data: [65, 41, 4],
            backgroundColor: [
                'rgba(75, 192, 192, 0.7)',
                'rgba(255, 159, 64, 0.7)',
                'rgba(255, 205, 86, 0.7)'
            ],
            borderColor: [
                'rgba(75, 192, 192, 1)',
                'rgba(255, 159, 64, 1)',
                'rgba(255, 205, 86, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
        }
    }
});
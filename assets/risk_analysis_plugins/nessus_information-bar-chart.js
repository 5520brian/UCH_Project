const ctx = document.getElementById('myChart')

const myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['LOW', 'MEDIUM', 'HIGH', 'CRITICAL'],
        datasets: [{
            label: '風險數量',
            data: [5, 91, 24, 18],
            backgroundColor: [
                'rgba(75, 192, 192, 0.7)',
                'rgba(255, 159, 64, 0.7)',
                'rgba(255, 205, 86, 0.7)',
                'rgba(255, 99, 132, 0.7)'
            ],
            borderColor: [
                'rgba(75, 192, 192, 1)',
                'rgba(255, 159, 64, 1)',
                'rgba(255, 205, 86, 1)',
                'rgba(255, 99, 132, 1)'
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
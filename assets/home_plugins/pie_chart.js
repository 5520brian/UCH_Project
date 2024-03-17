var ratio = 1;
var labels_padding = 20;

function isWindowSmall() {
    return window.innerWidth < 768;
}

if (isWindowSmall()) {
    var labels_font_size = '15';
}
else {
    var labels_font_size = '20';
}

// social_website_pie_chart
var social_low = 0; var social_medium = 8;
var social_high = 2; var social_critical = 0;
var social_risk_quantity = social_low + social_medium + social_high + social_critical;

var social_website_pieData = {
    labels: ["LOW：" + social_low, "MEDIUM：" + social_medium, "HIGH：" + social_high, "CRITICAL：" + social_critical],
    datasets: [{
        data: [social_low, social_medium, social_high, social_critical],
        backgroundColor: [
            'green',
            'yellow',
            'orange',
            'red'
        ]
    }]
};

var ctx1 = document.getElementById('social_website_pie_chart').getContext('2d');
var SocialWebsitePieChart = new Chart(ctx1, {
    type: 'pie',
    data: social_website_pieData,
    options: {
        plugins: {
            legend: {
                display: true,
                position: 'right',
                labels: {
                    font: {
                        size: labels_font_size
                    },
                    padding: labels_padding
                }
            },

            tooltip: {
                callbacks: {
                    label: function (context) {
                        var label = "  " + Math.round(context.parsed / social_risk_quantity * 100) + '%';
                        return label;
                    }
                }
            }
        },

        maintainAspectRatio: false,
        aspectRatio: ratio
    }
});

// application_website_pie_chart
var application_low = 2; var application_medium = 45;
var application_high = 4; var application_critical = 4;
var application_risk_quantity = application_low + application_medium + application_high + application_critical;

var application_website_pieData = {
    labels: ["LOW：" + application_low, "MEDIUM：" + application_medium, "HIGH：" + application_high, "CRITICAL：" + application_critical],
    datasets: [{
        data: [application_low, application_medium, application_high, application_critical],
        backgroundColor: [
            'green',
            'yellow',
            'orange',
            'red'
        ]
    }]
};

var ctx2 = document.getElementById('application_website_pie_chart').getContext('2d');
var ApplicationWebsitePieChart = new Chart(ctx2, {
    type: 'pie',
    data: application_website_pieData,
    options: {
        plugins: {
            legend: {
                display: true,
                position: 'right',
                labels: {
                    font: {
                        size: labels_font_size
                    },
                    padding: labels_padding
                }
            },

            tooltip: {
                callbacks: {
                    label: function (context) {
                        var label = " " + Math.round(context.parsed / application_risk_quantity * 100) + '%';
                        return label;
                    }
                }
            }
        },

        maintainAspectRatio: false,
        aspectRatio: ratio
    }
});

// transaction_website_pie_chart
var transaction_low = 0; var transaction_medium = 20;
var transaction_high = 5; var transaction_critical = 0;
var transaction_risk_quantity = transaction_low + transaction_medium + transaction_high + transaction_critical;

var transaction_website_pieData = {
    labels: ["LOW：" + transaction_low, "MEDIUM：" + transaction_medium, "HIGH：" + transaction_high, "CRITICAL：" + transaction_critical],
    datasets: [{
        data: [transaction_low, transaction_medium, transaction_high, transaction_critical],
        backgroundColor: [
            'green',
            'yellow',
            'orange',
            'red'
        ]
    }]
};

var ctx3 = document.getElementById('transaction_website_pie_chart').getContext('2d');
var TransactionWebsitePieChart = new Chart(ctx3, {
    type: 'pie',
    data: transaction_website_pieData,
    options: {
        plugins: {
            legend: {
                display: true,
                position: 'right',
                labels: {
                    font: {
                        size: labels_font_size
                    },
                    padding: labels_padding
                }
            },

            tooltip: {
                callbacks: {
                    label: function (context) {
                        var label = " " + Math.round(context.parsed / transaction_risk_quantity * 100) + '%';
                        return label;
                    }
                }
            }
        },

        maintainAspectRatio: false,
        aspectRatio: ratio
    }
});

// information_website_pie_chart
var information_low = 5; var information_medium = 91;
var information_high = 24; var information_critical = 18;
var information_risk_quantity = information_low + information_medium + information_high + information_critical;

var information_website_pieData = {
    labels: ["LOW：" + information_low, "MEDIUM：" + information_medium, "HIGH：" + information_high, "CRITICAL：" + information_critical],
    datasets: [{
        data: [information_low, information_medium, information_high, information_critical],
        backgroundColor: [
            'green',
            'yellow',
            'orange',
            'red'
        ]
    }]
};

var ctx4 = document.getElementById('information_website_pie_chart').getContext('2d');
var InformationWebsitePieChart = new Chart(ctx4, {
    type: 'pie',
    data: information_website_pieData,
    options: {
        plugins: {
            legend: {
                display: true,
                position: 'right',
                labels: {
                    font: {
                        size: labels_font_size
                    },
                    padding: labels_padding
                }
            },

            tooltip: {
                callbacks: {
                    label: function (context) {
                        var label = " " + Math.round(context.parsed / information_risk_quantity * 100) + '%';
                        return label;
                    }
                }
            }
        },

        maintainAspectRatio: false,
        aspectRatio: ratio,
    }
});

// zap_information_website_pie_chart
var zap_information_low = 145; var zap_information_medium = 81; var zap_information_high = 10;
var zap_information_risk_quantity = zap_information_low + zap_information_medium + zap_information_high;

var zap_information_website_pieData = {
    labels: ["LOW：" + zap_information_low, "MEDIUM：" + zap_information_medium, "HIGH：" + zap_information_high],
    datasets: [{
        data: [zap_information_low, information_medium, zap_information_high],
        backgroundColor: [
            'green',
            'yellow',
            'orange',
            'red'
        ]
    }]
};

var ctx5 = document.getElementById('zap_information_website_pie_chart').getContext('2d');
var ZapInformationWebsitePieChart = new Chart(ctx5, {
    type: 'pie',
    data: zap_information_website_pieData,
    options: {
        plugins: {
            legend: {
                display: true,
                position: 'right',
                labels: {
                    font: {
                        size: labels_font_size
                    },
                    padding: labels_padding
                }
            },

            tooltip: {
                callbacks: {
                    label: function (context) {
                        var label = " " + Math.round(context.parsed / zap_information_risk_quantity * 100) + '%';
                        return label;
                    }
                }
            }
        },

        maintainAspectRatio: false,
        aspectRatio: ratio,
    }
});

// zap_transaction_website_pie_chart
var zap_transaction_low = 112; var zap_transaction_medium = 58; var zap_transaction_high = 6;
var zap_transaction_risk_quantity = zap_transaction_low + zap_transaction_medium + zap_transaction_high;

var zap_transaction_website_pieData = {
    labels: ["LOW：" + zap_transaction_low, "MEDIUM：" + zap_transaction_medium, "HIGH：" + zap_transaction_high],
    datasets: [{
        data: [zap_transaction_low, zap_transaction_medium, zap_transaction_high],
        backgroundColor: [
            'green',
            'yellow',
            'orange'
        ]
    }]
};

var ctx6 = document.getElementById('zap_transaction_website_pie_chart').getContext('2d');
var ZapTransactionWebsitePieChart = new Chart(ctx6, {
    type: 'pie',
    data: zap_transaction_website_pieData,
    options: {
        plugins: {
            legend: {
                display: true,
                position: 'right',
                labels: {
                    font: {
                        size: labels_font_size
                    },
                    padding: labels_padding
                }
            },

            tooltip: {
                callbacks: {
                    label: function (context) {
                        var label = " " + Math.round(context.parsed / zap_transaction_risk_quantity * 100) + '%';
                        return label;
                    }
                }
            }
        },

        maintainAspectRatio: false,
        aspectRatio: ratio
    }
});

// zap_application_website_pie_chart
var zap_application_low = 82; var zap_application_medium = 56; var zap_application_high = 11;
var zap_application_risk_quantity = zap_application_low + zap_application_medium + zap_application_high;

var zap_application_website_pieData = {
    labels: ["LOW：" + zap_application_low, "MEDIUM：" + zap_application_medium, "HIGH：" + zap_application_high],
    datasets: [{
        data: [zap_application_low, zap_application_medium, zap_application_high],
        backgroundColor: [
            'green',
            'yellow',
            'orange'
        ]
    }]
};

var ctx7 = document.getElementById('zap_application_website_pie_chart').getContext('2d');
var ZapApplicationWebsitePieChart = new Chart(ctx7, {
    type: 'pie',
    data: zap_application_website_pieData,
    options: {
        plugins: {
            legend: {
                display: true,
                position: 'right',
                labels: {
                    font: {
                        size: labels_font_size
                    },
                    padding: labels_padding
                }
            },

            tooltip: {
                callbacks: {
                    label: function (context) {
                        var label = " " + Math.round(context.parsed / zap_application_risk_quantity * 100) + '%';
                        return label;
                    }
                }
            }
        },

        maintainAspectRatio: false,
        aspectRatio: ratio
    }
});

// zap_social_website_pie_chart
var zap_social_low = 112; var zap_social_medium = 66; var zap_social_high = 7;
var zap_social_risk_quantity = zap_social_low + zap_social_medium + zap_social_high;

var zap_social_website_pieData = {
    labels: ["LOW：" + zap_social_low, "MEDIUM：" + zap_social_medium, "HIGH：" + zap_social_high],
    datasets: [{
        data: [zap_social_low, zap_social_medium, zap_social_high],
        backgroundColor: [
            'green',
            'yellow',
            'orange',
            'red'
        ]
    }]
};

var ctx8 = document.getElementById('zap_social_website_pie_chart').getContext('2d');
var ZapSocialWebsitePieChart = new Chart(ctx8, {
    type: 'pie',
    data: zap_social_website_pieData,
    options: {
        plugins: {
            legend: {
                display: true,
                position: 'right',
                labels: {
                    font: {
                        size: labels_font_size
                    },
                    padding: labels_padding
                }
            },

            tooltip: {
                callbacks: {
                    label: function (context) {
                        var label = "  " + Math.round(context.parsed / zap_social_risk_quantity * 100) + '%';
                        return label;
                    }
                }
            }
        },

        maintainAspectRatio: false,
        aspectRatio: ratio
    }
});

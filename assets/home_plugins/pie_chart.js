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

var nessus_social_low = parseInt(nessus_social[0]); var nessus_social_medium = parseInt(nessus_social[1]);
var nessus_social_high = parseInt(nessus_social[2]); var nessus_social_critical = parseInt(nessus_social[3]);
var social_risk_quantity = nessus_social_low + nessus_social_medium + nessus_social_high + nessus_social_critical;

var social_website_pieData = {
    labels: ["LOW：" + nessus_social_low, "MEDIUM：" + nessus_social_medium, "HIGH：" + nessus_social_high, "CRITICAL：" + nessus_social_critical],
    datasets: [{
        data: nessus_social,
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

var nessus_application_low = parseInt(nessus_application[0]); var nessus_application_medium = parseInt(nessus_application[1]);
var nessus_application_high = parseInt(nessus_application[2]); var nessus_application_critical = parseInt(nessus_application[3]);
var application_risk_quantity = nessus_application_low + nessus_application_medium + nessus_application_high + nessus_application_critical;

var application_website_pieData = {
    labels: ["LOW：" + nessus_application_low, "MEDIUM：" + nessus_application_medium, "HIGH：" + nessus_application_high, "CRITICAL：" + nessus_application_critical],
    datasets: [{
        data: nessus_application,
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

var nessus_transaction_low = parseInt(nessus_transaction[0]); var nessus_transaction_medium = parseInt(nessus_transaction[1]);
var nessus_transaction_high = parseInt(nessus_transaction[2]); var nessus_transaction_critical = parseInt(nessus_transaction[3]);
var transaction_risk_quantity = nessus_transaction_low + nessus_transaction_medium + nessus_transaction_high + nessus_transaction_critical;

var transaction_website_pieData = {
    labels: ["LOW：" + nessus_transaction_low, "MEDIUM：" + nessus_transaction_medium, "HIGH：" + nessus_transaction_high, "CRITICAL：" + nessus_transaction_critical],
    datasets: [{
        data: nessus_transaction,
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

var nessus_information_low = parseInt(nessus_information[0]); var nessus_information_medium = parseInt(nessus_information[1]);
var nessus_information_high = parseInt(nessus_information[2]); var nessus_information_critical = parseInt(nessus_information[3]);
var information_risk_quantity = nessus_information_low + nessus_information_medium + nessus_information_high + nessus_information_critical;

var information_website_pieData = {
    labels: ["LOW：" + nessus_information_low, "MEDIUM：" + nessus_information_medium, "HIGH：" + nessus_information_high, "CRITICAL：" + nessus_information_critical],
    datasets: [{
        data: nessus_information,
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

var zap_social_low = parseInt(zap_social[0]);
var zap_social_medium = parseInt(zap_social[1]);
var zap_social_high = parseInt(zap_social[2]);
var zap_social_risk_quantity = zap_social_low + zap_social_medium + zap_social_high;

var zap_social_website_pieData = {
    labels: ["LOW：" + zap_social_low, "MEDIUM：" + zap_social_medium, "HIGH：" + zap_social_high],
    datasets: [{
        data: zap_social,
        backgroundColor: [
            'green',
            'yellow',
            'orange',
            'red'
        ]
    }]
};

var ctx5 = document.getElementById('zap_social_website_pie_chart').getContext('2d');
var ZapSocialWebsitePieChart = new Chart(ctx5, {
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

var zap_application_low = parseInt(zap_application[0]);
var zap_application_medium = parseInt(zap_application[1]);
var zap_application_high = parseInt(zap_application[2]);
var zap_application_risk_quantity = zap_application_low + zap_application_medium + zap_application_high;

var zap_application_website_pieData = {
    labels: ["LOW：" + zap_application_low, "MEDIUM：" + zap_application_medium, "HIGH：" + zap_application_high],
    datasets: [{
        data: zap_application,
        backgroundColor: [
            'green',
            'yellow',
            'orange'
        ]
    }]
};

var ctx6 = document.getElementById('zap_application_website_pie_chart').getContext('2d');
var ZapApplicationWebsitePieChart = new Chart(ctx6, {
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

var zap_transaction_low = parseInt(zap_transaction[0]);
var zap_transaction_medium = parseInt(zap_transaction[1]);
var zap_transaction_high = parseInt(zap_transaction[2]);
var zap_transaction_risk_quantity = zap_transaction_low + zap_transaction_medium + zap_transaction_high;

var zap_transaction_website_pieData = {
    labels: ["LOW：" + zap_transaction_low, "MEDIUM：" + zap_transaction_medium, "HIGH：" + zap_transaction_high],
    datasets: [{
        data: zap_transaction,
        backgroundColor: [
            'green',
            'yellow',
            'orange'
        ]
    }]
};

var ctx7 = document.getElementById('zap_transaction_website_pie_chart').getContext('2d');
var ZapTransactionWebsitePieChart = new Chart(ctx7, {
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

var zap_information_low = parseInt(zap_information[0]);
var zap_information_medium = parseInt(zap_information[1]);
var zap_information_high = parseInt(zap_information[2]);
var zap_information_risk_quantity = zap_information_low + zap_information_medium + zap_information_high;

var zap_information_website_pieData = {
    labels: ["LOW：" + zap_information_low, "MEDIUM：" + zap_information_medium, "HIGH：" + zap_information_high],
    datasets: [{
        data: zap_information,
        backgroundColor: [
            'green',
            'yellow',
            'orange',
            'red'
        ]
    }]
};

var ctx8 = document.getElementById('zap_information_website_pie_chart').getContext('2d');
var ZapInformationWebsitePieChart = new Chart(ctx8, {
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

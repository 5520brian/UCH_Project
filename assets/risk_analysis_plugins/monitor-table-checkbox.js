var checkboxes = document.querySelectorAll('.risk-severity-checkbox');

document.addEventListener('DOMContentLoaded', function () {
    checkboxes.forEach(function (checkbox) {
        var storedValue = localStorage.getItem(checkbox.getAttribute('name'));
        if (storedValue !== null) {
            checkbox.checked = storedValue === 'true';
        }

        checkbox.dispatchEvent(new Event('change'));

        checkbox.addEventListener('change', function () {
            localStorage.setItem(checkbox.getAttribute('name'), checkbox.checked);

            var selectedRiskLevels = Array.from(checkboxes)
                .filter(function (cb) {
                    return cb.checked;
                })
                .map(function (cb) {
                    return cb.getAttribute('data-risk-level');
                });

            var rows = document.querySelectorAll('.risk-level-row');

            if (selectedRiskLevels.length === 0) {
                rows.forEach(function (row) {
                    row.style.display = 'table-row';
                });
            } else {
                rows.forEach(function (row) {
                    var riskLevel = row.getAttribute('data-risk-level');
                    row.style.display = selectedRiskLevels.includes(riskLevel) ? 'table-row' : 'none';
                });
            }
        });
    });
});

checkboxes.forEach(function (checkbox) {
    checkbox.addEventListener('change', function () {
        var selectedRiskLevels = Array.from(checkboxes)
            .filter(function (checkbox) {
                return checkbox.checked;
            })
            .map(function (checkbox) {
                return checkbox.getAttribute('data-risk-level');
            });

        if (selectedRiskLevels.length === 0) {
            var rows = document.querySelectorAll('.risk-level-row');
            rows.forEach(function (row) {
                row.style.display = 'table-row';
            });
        }
        else {
            var rows = document.querySelectorAll('.risk-level-row');
            rows.forEach(function (row) {
                var riskLevel = row.getAttribute('data-risk-level');
                if (selectedRiskLevels.includes(riskLevel)) {
                    row.style.display = 'table-row';
                } else {
                    row.style.display = 'none';
                }
            });
        }
    });
});

// sort btn
var ascending = true;

function toggleSort() {
    if (ascending) {
        sortCriticalToLow();
        document.getElementById('sort-button').innerHTML = '&#9660;';
    } else {
        sortLowToCritical();
        document.getElementById('sort-button').innerHTML = '&#9650;';
    }
    ascending = !ascending;
}

function sortCriticalToLow() {
    var rows = document.querySelectorAll('.risk-level-row');
    var sortedRows = Array.from(rows).sort(function (a, b) {
        var severityOrder = {
            'LOW': 1,
            'MEDIUM': 2,
            'HIGH': 3,
            'CRITICAL': 4
        };
        var severityA = a.getAttribute('data-risk-level');
        var severityB = b.getAttribute('data-risk-level');
        return severityOrder[severityB] - severityOrder[severityA];
    });
    var tbody = document.querySelector('tbody');
    tbody.innerHTML = '';
    sortedRows.forEach(function (row) {
        tbody.appendChild(row);
    });
}

function sortLowToCritical() {
    var rows = document.querySelectorAll('.risk-level-row');
    var sortedRows = Array.from(rows).sort(function (a, b) {
        var severityOrder = {
            'LOW': 1,
            'MEDIUM': 2,
            'HIGH': 3,
            'CRITICAL': 4
        };
        var severityA = a.getAttribute('data-risk-level');
        var severityB = b.getAttribute('data-risk-level');
        return severityOrder[severityA] - severityOrder[severityB];
    });
    var tbody = document.querySelector('tbody');
    tbody.innerHTML = '';
    sortedRows.forEach(function (row) {
        tbody.appendChild(row);
    });
}

// ------------------------------------------------------------------------------
document.addEventListener('DOMContentLoaded', function () {
    const tableContainer = document.querySelector('.table-responsive');
    const detailInfo = document.querySelector('.detail-info');
    const detailInfoText = document.querySelector('.detail-info-text');
    const backToTableBtn = document.querySelector('.back-to-table-btn');

    tableContainer.addEventListener('click', function (event) {
        const target = event.target;
        if (target.classList.contains('risk-name')) {
            const id = target.dataset.id;

            fetch(`/fetch_detail?id=${id}`)
                .then(response => response.json())
                .then(data => {
                    tableContainer.style.display = 'none';
                    detailInfo.style.display = 'block';
                    backToTableBtn.style.display = 'block';
                    detailInfoText.innerHTML = `<h1 class='my-4'>${data.risk_name}</h1><hr />
                                                <h2>風險描述 - </h2>
                                                <p class='my-3'>${data.risk_description}<p><hr />
                                                <h2>修復建議 - </h2>
                                                <p class='my-3 mb-4'>${data.risk_solution}<p>`;
                })
                .catch(error => console.error('Error:', error));
        }
    });

    backToTableBtn.addEventListener('click', function () {
        detailInfo.style.display = 'none';
        backToTableBtn.style.display = 'none';
        tableContainer.style.display = 'block';
    });
});
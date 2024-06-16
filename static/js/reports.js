const dateFromInput = document.getElementById('date-from');
const dateToInput = document.getElementById('date-to');
const reportNameInput = document.getElementById('report-name');
const generateReportButton = document.getElementById('generate-report');
const reportTableBody = document.getElementById('report-table-body');

generateReportButton.addEventListener('click', (e) => {
    e.preventDefault();
    const dateFrom = dateFromInput.value;
    const dateTo = dateToInput.value;
    const reportName = reportNameInput.value;

    // здесь вы можете добавить логику генерации отчета
    // для примера, я просто добавлю строку в таблицу
    const newRow = document.createElement('tr');
    newRow.innerHTML = `
        <td>${reportName}</td>
        <td>${dateFrom} - ${dateTo}</td>
    `;
    reportTableBody.appendChild(newRow);
});

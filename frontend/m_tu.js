console.log('Fetch from M_TU made!');

// Fetch JSON data from the endpoint
fetch('http://localhost:8000/M_TU/')
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        return response.json(); // Parse JSON data
    })
    .then(data => {
        renderTable(data);
    })
    .catch(error => {
        console.error('Error fetching data:', error);
    });

// Function to render table
function renderTable(data) {
    const table = document.getElementById('data-table');
    const thead = table.querySelector('thead tr');
    const tbody = table.querySelector('tbody');

    // Clear any existing table content
    thead.innerHTML = '';
    tbody.innerHTML = '';

    if (data.length === 0) {
        tbody.innerHTML = '<tr><td colspan="100%">No data available</td></tr>';
        return;
    }

    // Dynamically create table headers based on keys in the first data object
    Object.keys(data[0]).forEach(key => {
        const th = document.createElement('th');
        th.textContent = key;
        thead.appendChild(th);
    });

    // Populate table rows
    data.forEach(row => {
        const tr = document.createElement('tr');
        Object.keys(row).forEach(key => {
            const td = document.createElement('td');
            // Replace null with a placeholder or empty string
            td.textContent = row[key] !== null ? row[key] : 'N/A';
            tr.appendChild(td);
        });
        tbody.appendChild(tr);
    });
}

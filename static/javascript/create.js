function addRow(tableID) {
    let tableRef = document.getElementById(tableID);
    let rows = document.getElementById(tableID).rows.length;
    let newRow = tableRef.insertRow(rows-1);
    let cols = document.getElementById(tableID).rows[0].cells.length
    for (let i = 0; i < cols-1; i++) {
        let newCell = newRow.insertCell(i);
        let cellName = 'cell[' +  Number(rows-1) +'][' + i + ']';
        let cellInput = document.createElement("input");
        cellInput.setAttribute('class', 'form-control');
        cellInput.setAttribute('name', cellName);
        cellInput.setAttribute('placeholder', cellName);
        newCell.appendChild(cellInput);
    }
}

function addCol(tableID) {
    let tableRef = document.getElementById(tableID);
    let rows = document.getElementById(tableID).rows.length;
    let cols = document.getElementById(tableID).rows[0].cells.length;
    for (let i = 0; i < rows; i++) {
        let row = document.getElementById(tableID).rows[i];
        let newCell = row.insertCell(cols-1);
        let cellName = 'cell[' + i +'][' + Number(cols-1) + ']';
        let cellInput = document.createElement("input");
        cellInput.setAttribute('class', 'form-control');
        cellInput.setAttribute('name', cellName);
        if (i==0){
            cellInput.setAttribute('placeholder','Side ' + cols + ' Name')
        } else {
            cellInput.setAttribute('placeholder', cellName);
        }
        newCell.appendChild(cellInput);
    }
}

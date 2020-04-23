function addRow(tableID) {
    let tableRef = document.getElementById(tableID);
    let rows = document.getElementById(tableID).rows.length;
    let newRow = tableRef.insertRow(rows-1);
    let cols = document.getElementById(tableID).rows[0].cells.length;
    let remove = newRow.insertCell(0);
    let button = document.createElement("button");

    // set the remove button
    remove.setAttribute('class', 'onHover');
    button.setAttribute('type', 'button');
    button.innerHTML = '-';
    button.setAttribute('class', 'hidden');
    button.setAttribute('id', 'removeRow[' + Number(rows-1) + ']');
    button.addEventListener("click", function() {removeRow(tableID, rows-1)} );
    remove.appendChild(button);

    // make the form fields
    for (let i = 1; i < cols; i++) {
        let newCell = newRow.insertCell(i);
        let cellName = 'cell[' +  Number(rows-2) +'][' + Number(i-1) + ']';
        let cellInput = document.createElement("input");
        cellInput.setAttribute('class', 'form-control');
        cellInput.setAttribute('name', cellName);
        cellInput.setAttribute('placeholder', cellName);
        cellInput.setAttribute('maxlength', '1000')
        newCell.appendChild(cellInput);
    }
}

function addCol(tableID) {
    let tableRef = document.getElementById(tableID);
    let rows = document.getElementById(tableID).rows.length - 1;
    let cols = document.getElementById(tableID).rows[1].cells.length;
    for (let i = 0; i < rows; i++) {
        let row = document.getElementById(tableID).rows[i];
        let newCell = row.insertCell(cols-1);
        if (i==0) { // set the remove button
            let button = document.createElement("button");
            newCell.setAttribute('class', 'onHover');
            button.setAttribute('type', 'button');
            button.innerHTML = '-';
            button.setAttribute('class', 'hidden');
            button.setAttribute('id', 'removeRow[' + rows-1 + ']');
            button.addEventListener("click", function() {removeCol(tableID, cols-2)});
            newCell.appendChild(button);
        } else { // set form fields
            let cellName = 'cell[' + Number(i-1) + '][' + Number(cols - 2) + ']';
            let cellInput = document.createElement("input");
            cellInput.setAttribute('class', 'form-control');
            cellInput.setAttribute('name', cellName);
            if (i == 1) {
                cellInput.setAttribute('placeholder', 'Side ' + Number(cols - 1) + ' Name')
                cellInput.setAttribute('maxlength', '255')
                cellInput.setAttribute('required', '')
            } else {
                cellInput.setAttribute('placeholder', cellName);
                cellInput.setAttribute('maxlength', '1000')
            }
            newCell.appendChild(cellInput);
        }
    }
}

// renumbers all fields appropriately (in case of row/col removal)
function renumber(rows, numRows, numCols) {
    for (var i=1; i<numRows-1; i++) {
        var currRow = rows[i];
        // console.log("editing a row");
        // console.log(currRow);
        for (var j=1; j<numCols-1; j++) {
            let cellName = 'cell[' + Number(i-1) + '][' + Number(j - 1) + ']';
            currRow.cells[j].children[0].setAttribute('name', cellName);
            if (i == 1) {
                currRow.cells[j].children[0].setAttribute('placeholder', 'Side ' + j + ' Name')
            } else {
                currRow.cells[j].children[0].setAttribute('placeholder', cellName);
            }
        }
    }
}

function removeRow(tableID, row) {
    let rows = document.getElementById(tableID).rows;
    let numRows = document.getElementById(tableID).rows.length-1;
    let numCols = document.getElementById(tableID).rows[1].cells.length;
    if (numRows == 3) {
        alert("You cannot remove all cards from your set!");
        return;
    }
    if (window.confirm("You are removing a row. This will remove all data in the row. " +
        "Are you sure you want to do this?")) {
        document.getElementById(tableID).deleteRow(row);
        renumber(rows, numRows, numCols);
    }
}

function removeCol(tableID, col) {
    let cols = document.getElementById(tableID).rows[1].cells.length;
    console.log(cols);
    if (cols == 3) {
        alert("You cannot remove all sides from your set!");
        return;
    }
    if (window.confirm("You are removing a column. This will remove all data in the column. " +
        "Are you sure you want to do this?")) {
        let rows = document.getElementById(tableID).rows
        let numRows = document.getElementById(tableID).rows.length - 1;
        for (var i = 0; i < numRows; i++) {
            rows[i].deleteCell(col + 1);
        }
        renumber(rows, numRows, cols);
    }
}
// This file contains all dynamic-form related logic for adding and removing rows/cols using jQuery

// Adds a row of form fields to the given table
function addRow(tableID) {
    let tableRef = document.getElementById(tableID);
    let rows = document.getElementById(tableID).rows.length;
    let newRow = tableRef.insertRow(rows-1);
    let cols = document.getElementById(tableID).rows[0].cells.length;
    let remove = newRow.insertCell(0);
    let button = document.createElementNS("http://www.w3.org/2000/svg", "svg");
    let path = document.createElementNS("http://www.w3.org/2000/svg", 'path');

    // set the remove button
    remove.setAttribute('class', 'onHover')
    button.setAttributeNS("http://www.w3.org/2000/xmlns/", "xmlns:xlink", "http://www.w3.org/1999/xlink");
    button.setAttribute('class', 'bi bi-dash-circle-fill hidden');
    button.setAttribute('width', '1.3em');
    button.setAttribute('height', '1.3em');
    button.setAttribute('viewBox', '0 0 16 16');
    button.setAttribute('fill', 'lightsteelblue');
    // button.setAttribute('xmlns', 'http://www.w3.org/2000/svg');
    path.setAttribute("fill-rule", "evenodd");
    path.setAttribute("d",'M16 8A8 8 0 110 8a8 8 0 0116 0zM4 7.5a.5.5 0 000 1h8a.5.5 0 000-1H4z');
    path.setAttribute('clip-rule', 'evenodd')
    button.setAttribute('id', 'removeRow[' + Number(rows-1) + ']');
    button.addEventListener("click", function() {removeRow(tableID, rows-1)} );
    button.appendChild(path);
    remove.appendChild(button);

    // make the form fields
    for (let i = 1; i < cols; i++) {
        let newCell = newRow.insertCell(i);
        let cellName = 'cell[' +  Number(rows-2) +'][' + Number(i-1) + ']';
        let cellInput = document.createElement("input");
        cellInput.setAttribute('class', 'form-control');
        cellInput.setAttribute('name', cellName);
        // cellInput.setAttribute('placeholder', cellName);
        cellInput.setAttribute('maxlength', '1000')
        newCell.appendChild(cellInput);
    }
}

// Adds a column of form fields to the given table
function addCol(tableID) {
    let tableRef = document.getElementById(tableID);
    let rows = document.getElementById(tableID).rows.length - 1;
    let cols = document.getElementById(tableID).rows[1].cells.length;
    for (let i = 0; i < rows; i++) {
        let row = document.getElementById(tableID).rows[i];
        let newCell = row.insertCell(cols-1);
        if (i==0) { // set the remove button
            let button = document.createElementNS("http://www.w3.org/2000/svg", "svg");
            let path = document.createElementNS("http://www.w3.org/2000/svg", 'path');
            newCell.setAttribute('class', 'onHover');
            button.setAttributeNS("http://www.w3.org/2000/xmlns/", "xmlns:xlink", "http://www.w3.org/1999/xlink");
            button.setAttribute('class', 'bi bi-dash-circle-fill hidden');
            button.setAttribute('width', '1.3em');
            button.setAttribute('height', '1.3em');
            button.setAttribute('viewBox', '0 0 16 16');
            button.setAttribute('fill', 'lightsteelblue');
            button.setAttribute('id', 'removeCol[' + rows-1 + ']');
            button.addEventListener("click", function() {removeCol(tableID, cols-2)});
            path.setAttribute("fill-rule", "evenodd");
            path.setAttribute("d",'M16 8A8 8 0 110 8a8 8 0 0116 0zM4 7.5a.5.5 0 000 1h8a.5.5 0 000-1H4z');
            path.setAttribute('clip-rule', 'evenodd')
            button.appendChild(path);
            newCell.appendChild(button);
        } else { // set form fields
            let cellName = 'cell[' + Number(i-1) + '][' + Number(cols - 2) + ']';
            let cellInput = document.createElement("input");
            cellInput.setAttribute('class', 'form-control');
            cellInput.setAttribute('name', cellName);
            if (i == 1) {
                cellInput.setAttribute('placeholder', 'Side ' + Number(cols - 1) + ' Name')
                cellInput.setAttribute('maxlength', '255');
                cellInput.setAttribute('required', '');
            } else {
                // cellInput.setAttribute('placeholder', cellName);
                cellInput.setAttribute('maxlength', '1000');
            }
            newCell.appendChild(cellInput);
        }
    }
}

// Renumbers all fields appropriately (in case of row/col removal that isn't the last row/col)
function renumber(rows, numRows, numCols) {
    // console.log("renumbering", numRows, numCols);
    for (var i=1; i<numRows - 1; i++) {
        // console.log("on row ", i);
        var currRow = rows[i];
        // console.log("editing a row", currRow);
        for (var j=1; j<numCols-2; j++) {
            console.log("on col " + j);
            let cellName = 'cell[' + Number(i-1) + '][' + Number(j - 1) + ']';
            currRow.cells[j].children[0].setAttribute('name', cellName);
            if (i == 1) {
                currRow.cells[j].children[0].setAttribute('placeholder', 'Side ' + j + ' Name')
            // } else { // sets a placeholder name (for debugging)
                // currRow.cells[j].children[0].setAttribute('placeholder', cellName);
            }
        }
    }
}

// Removes a given row of form fields from the table if possible
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

// Removes a given column of form fields from the table if possible
function removeCol(tableID, col) {
    let cols = document.getElementById(tableID).rows[1].cells.length;
    if (cols == 3) {
        alert("You cannot remove all sides from your set!");
        return;
    }
    if (window.confirm("You are removing a column. This will remove all data in the column. " +
        "Are you sure you want to do this?")) {
        let rows = document.getElementById(tableID).rows;
        let numRows = document.getElementById(tableID).rows.length - 1;
        for (var i = 0; i < numRows; i++) {
            console.log('deleting cell', i)
            rows[i].deleteCell(col + 1);
        }
        renumber(rows, numRows, cols);
    }
}

// Exits the editing page
function exit_edit(){
    if (window.confirm("You are exiting editing. This will discard all your changes! " +
        "Are you sure you want to do this?")) {
        let pathArray = window.location.pathname.slice(0, -5);
        window.location.replace(pathArray);
    }
}
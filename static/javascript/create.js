$(document).ready(function(){
    // $('#form').submit(function(e){
    //     var memberArr = [];
    //     $('.member_data').each(function(){
    //         var thisMember = {};
    //         $(this).children().each(function(){
    //             thisMember[$(this).attr('name')] = $(this).val();
    //         });
    //         memberArr.push(thisMember);
    //         // Delete this input
    //         $(this).remove();
    //     });
    //
    //     var input = $("<input>").attr("type", "hidden").attr("name", "members").val(JSON.stringify(memberArr));
    //     $('#dynamic_form').append($(input));
    //     e.preventDefault();
    //
    //     $.post("http://geraintanderson.com/cgi-bin/ajax_array.py",
    //     $('#form').serialize(),
    //     function(data, status){
    //         $('#member_info').html(data);
    //         // Reset the form
    //         $('#dynamic_form').html('<span class="member_data"><input type="text" name="name"><input type="text" name="date"></span><br>');
    //     });
    // });
    // $('#insertRow').click(function(){
    //     document.getElementById("setTable").insertRow(-1).innerHTML ='<td class="tg-0lax">card1</td>\n' +
    //         '            <td class="tg-0lax">abc</td>\n' +
    //         '            <td class="tg-0lax">def</td>\n' +
    //         '            <td class="tg-0lax">ghi</td>';
    // });
    // $('button').click(function(){
    //     // Add new form fields
    //     $('#dynamic_form').append('<span class="member_data"><input type="text" name="name"><input type="text" name="date"></span><br>');
    // });


});


function addRow(tableID) {
    let tableRef = document.getElementById(tableID);
    let rows = document.getElementById(tableID).rows.length;
    // Insert a row at the end of the table
    let newRow = tableRef.insertRow(rows-1);
    console.log(rows);
    let cols = document.getElementById(tableID).rows[0].cells.length
    for (let i = 0; i < cols-1; i++) {
        let newCell = newRow.insertCell(i);
        // let newText = document.createTextNode('(' + rows + ', ' + i + ')');
        // newCell.appendChild(newText);
        let cellName = 'cell[' + rows +'][' + Number(i+1) + ']';
        let cellInput = document.createElement("input");
        cellInput.setAttribute('class', 'form-control');
        cellInput.setAttribute('name', cellName);
        cellInput.setAttribute('placeholder', cellName);
        newCell.appendChild(cellInput);
    }
};

function addCol(tableID) {
    let tableRef = document.getElementById(tableID);
    let rows = document.getElementById(tableID).rows.length;
    console.log(rows);
    let cols = document.getElementById(tableID).rows[0].cells.length;
    for (let i = 0; i < rows; i++) {
        let row = document.getElementById(tableID).rows[i];
        let newCell = row.insertCell(cols-1);
        let cellName = 'cell[' + Number(i+1) +'][' + cols + ']';
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
};

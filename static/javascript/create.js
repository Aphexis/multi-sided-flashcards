

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
    $('button').click(function(){
        // Add new form fields
        $('#dynamic_form').append('<span class="member_data"><input type="text" name="name"><input type="text" name="date"></span><br>');
    });
});

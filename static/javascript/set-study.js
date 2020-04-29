$(document).ready(function(){
    console.log("jQuery connected!")
    $("#nextCard").click(function() {
        console.log("clicking")
        $(".middle-col").load("../../api/1", function( response, status, xhr ) {
      if ( status == "error" ) {
          console.log("we tried")
        var msg = "Sorry but there was an error: ";
        $( ".middle-col" ).html( msg + xhr.status + " " + xhr.statusText );
      }
    })});
});



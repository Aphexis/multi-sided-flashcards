function loadCard(set_id, side_num, card_num, total_cards) {
    $(".middle-col").load("../../api/card?set=" + set_id + "&side=" + side_num + "&card=" + card_num,
        function( response, status, xhr ) {
            if ( status == "error" ) {
                console.log("Error occured");
                var msg = "Sorry but there was an error: ";
                $( ".middle-col" ).html( msg + xhr.status + " " + xhr.statusText );
            }
        });
    $(".progress-bar")
        .css("width", (card_num+1)/total_cards*100 + "%")
        .attr("aria-valuenow", (card_num+1)/total_cards*100)
        .text(card_num+1 + "/" + total_cards + " cards studied");
}

function loadDone(set_id, total_cards) {
    $("#body").load("../../api/study_done?set=" + set_id,
        function( response, status, xhr ) {
            if ( status == "error" ) {
                console.log("Error occured");
                var msg = "Sorry but there was an error: ";
                $( ".middle-col" ).html( msg + xhr.status + " " + xhr.statusText );
            }
        })
    $(".progress-bar")
        .css("width", "100%")
        .attr("aria-valuenow", 100)
        .text("All cards studied!");
}

$(document).ready(function(){
    console.log("jQuery connected!");
    let pathArray = window.location.pathname.split('/');
    let set_id = pathArray[2];
    let total_sides, total_cards;
    $.get("../../api/set_info?set=" + set_id, function(data, status){
        if ( status == "error" ) {
            console.log("Error occured: " + xhr.status + " " + xhr.statusText);
        } else {
            total_sides = data.num_sides;
            total_cards = data.num_cards;
        }
    });
    let side_num = 1;
    let card_num = 0;

    function nextCard() {
        console.log("clicking nextCard");
        card_num++;
        console.log({card_num: card_num, total_cards: total_cards});
        if (card_num >= total_cards) {
            console.log("past total cards");
            loadDone(set_id, total_cards);
            card_num = total_cards;
            return;
        }
        loadCard(set_id, side_num, card_num, total_cards);
    };
    function prevCard() {
        console.log("clicking prevCard");
        card_num--;
        if (card_num < 0) {
            card_num = 0;
            return;
        }
        loadCard(set_id, side_num, card_num, total_cards);
    }
    function nextSide() {
        console.log("clicking nextSide");
        // console.log({side_num: side_num, total_sides: total_sides});
        if (card_num == total_cards) return;
        side_num++;
        if (side_num > total_sides) {
            side_num = 1; // loops around
        }
        loadCard(set_id, side_num, card_num, total_cards);
    }
    function prevSide() {
        if (card_num == total_cards) return;
        side_num--;
        if (side_num < 1) {
            side_num = total_sides; // loops around
        }
        loadCard(set_id, side_num, card_num, total_cards);
    }
    function restart() {
        console.log("clicking restart");
        side_num = 1;
        card_num = 0;
        loadCard(set_id, side_num, card_num, total_cards);
    }


    $("#nextCard").click(function() {
        nextCard()
    });
    $("#prevCard").click(function() {
        prevCard()
    });
    $(".middle-col").on("click", "#nextSide", function() {
        nextSide()
    });
    $(".middle-col").on("click", "#prevSide", function() {
        prevSide()
    });
    $("#body").on("click", "#restart", function() {
        restart()
    });

    $(document).keydown(function (e) {
        var arrow = { left: 37, up: 38, right: 39, down: 40 };

        switch (e.which) {
            case arrow.left:
                prevCard();
                break;
            case arrow.up:
                prevSide();
                break;
            case arrow.right:
                nextCard();
                break;
            case arrow.down:
                nextSide();
                break;
            case 82: // restart
                restart();
                break;
        }
    });

});




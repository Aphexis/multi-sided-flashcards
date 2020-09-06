// Displays a specific card and side
function loadCard(set_id, side_num, card_num, total_cards, sides, cards, side_order) {
    let nextSide = side_num+1 < sides.length ? sides[side_order[side_num+1]] : sides[side_order[1]];
    if ($('.card').length) {
        $("#nextSideText").text("Next: " + nextSide);
        $("#sideProgress").text("Side " + side_num + "/" + String(sides.length-1));
        $(".card-title").text(sides[side_order[side_num]]);
        $(".card-text").text(cards[card_num][side_order[side_num]]);
    } else {
        $("#body").load(" #bodyRow",
            function (response, status, xhr) {
                if (status == "error") {
                    console.log("Error occured");
                    var msg = "Sorry but there was an error: ";
                    $("#body").html(msg + xhr.status + " " + xhr.statusText);
                } else {
                    $("#nextSideText").text("Next: " + nextSide);
                    $("#sideProgress").text("Side " + side_num + "/" + String(sides.length-1));
                    $(".card-title").text(sides[side_order[side_num]]);
                    $(".card-text").text(cards[card_num][side_order[side_num]]);
                }
            });
    }
    $(".progress-bar")
        .css("width", (card_num+1)/total_cards*100 + "%")
        .attr("aria-valuenow", (card_num+1)/total_cards*100)
        .text(card_num+1 + "/" + total_cards + " cards studied");
}

// Displays "studying complete" UI
function loadDone(set_id, total_cards) {
    $("#body").load("../../api/study_done?set=" + set_id,
        function( response, status, xhr ) {
            if ( status == "error" ) {
                console.log("Error occured");
                var msg = "Oops, there was an error: ";
                $( "#body" ).html( msg + xhr.status + " " + xhr.statusText );
            }
        });
    $(".progress-bar")
        .css("width", "100%")
        .attr("aria-valuenow", 100)
        .text("All cards studied!");
}

function shuffleArray(array) {
    for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
    }
}

$(document).ready(function(){
    let pathArray = window.location.pathname.split('/');
    let set_id = pathArray[2];
    let total_sides, total_cards, sides, cards, cards_shuffled;
    let side_order = {};
    $.get("../../api/set_info?set=" + set_id, function(data, status){
        if ( status == "error" ) {
            console.error("Error occured: " + xhr.status + " " + xhr.statusText);
        } else {
            total_sides = data.num_sides;
            total_cards = data.num_cards;
            sides = data.sides;
            cards = data.cards;
            cards_shuffled = cards;
            for (i=1; i<=total_sides; i++) {
                side_order[i] = i;
            }

        }
    });
    let side_num = 1;
    let card_num = 0;


    let el = document.getElementById('sideList');
    let sortable = Sortable.create(el, {animation: 150});

    // Modal (side re-ordering)
    $("#settingsModal").on("click", "#saveChanges", function() {
        sortable.save()
        let arr = sortable.toArray();
        arr.map((currElement, index) => {
            side_order[index+1] = currElement;
        });
        restart();
        $('#settingsModal').modal('hide');
    });

    // Card/Side navigation
    function nextCard() {
        // console.log("clicking nextCard");
        card_num++;
        // console.log({card_num: card_num, total_cards: total_cards});
        if (card_num >= total_cards) {
            loadDone(set_id, total_cards);
            card_num = total_cards;
            return;
        }
        loadCard(set_id, side_num, card_num, total_cards, sides, cards_shuffled, side_order);
    }
    function prevCard() {
        // console.log("clicking prevCard");
        card_num--;
        if (card_num < 0) {
            card_num = 0;
            return;
        }
        loadCard(set_id, side_num, card_num, total_cards, sides, cards_shuffled, side_order);
    }
    function nextSide() {
        // console.log("clicking nextSide");
        // console.log({side_num: side_num, total_sides: total_sides});
        if (card_num == total_cards) return;
        side_num++;
        if (side_num > total_sides) {
            side_num = 1; // loops around
        }
        loadCard(set_id, side_num, card_num, total_cards, sides, cards_shuffled, side_order);
    }
    function prevSide() {
        if (card_num == total_cards) return;
        side_num--;
        if (side_num < 1) {
            side_num = total_sides; // loops around
        }
        loadCard(set_id, side_num, card_num, total_cards, sides, cards_shuffled, side_order);
    }
    function restart() {
        // console.log("clicking restart");
        side_num = 1;
        card_num = 0;
        loadCard(set_id, side_num, card_num, total_cards, sides, cards_shuffled, side_order);
    }

    function shuffle() {
        // console.log("shuffling cards");
        shuffleArray(cards_shuffled);
        restart();
    }

    // set click handlers
    $("#body").on("click", "#nextCard", function() {
        nextCard()
    });
    $("body").on("click", "#prevCard", function() {
        prevCard()
    });
    $("#body").on("click", "#nextSide", function() {
        nextSide()
    });
    $("#body").on("click", "#prevSide", function() {
        prevSide()
    });
    $("#body").on("click", "#restart", function() {
        restart()
    });
    $("#options").on("click", "#shuffle", function() {
        shuffle();
    });

    // set key handlers
    $(document).keydown(function (e) {
        var key = { left: 37, up: 38, right: 39, down: 40, R: 82, S: 83 };

        switch (e.which) {
            case key.left:
                prevCard();
                break;
            case key.up:
                prevSide();
                break;
            case key.right:
                nextCard();
                break;
            case key.down:
                nextSide();
                break;
            case key.R:
                restart();
                break;
            case key.S:
                shuffle();
                break;
        }
    });
});

$(document).ready(function(){

    var update = function(data) {
        var players = Object.keys(data);
        for (var i = 0; i < players.length; i++) {
            console.log(players[i]);
        }
    };

    $.ajax({
        url: '/score',
        type: 'GET',
        dataType: 'json',
        success: update
    });

});

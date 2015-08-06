$(document).ready(function(){

    var update = function(data) {
        var players = data['sb'];
        for (var i = 0; i < players.length; i++) {
            var player = players[i];
            console.log("id", player.pid);
            console.log("name", player.player_name);
            console.log("results", player.results);
        }
    };

    $.ajax({
        url: '/score',
        type: 'GET',
        dataType: 'json',
        success: update
    });

});

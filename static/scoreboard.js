$(document).ready(function(){

    var update = function(data) {
        var players = data['sb'];
        var $scores = $('#scores');
        for (var i = 0; i < players.length; i++) {
            var player = players[i];
            var name = player.player_name;
            $scores.append('<div class="row" id=' + player.pid + '></div>');
            $row = $('#' + player.pid);
            $row.append('<div class="box name">' + name + '</div>');
            var results = player.results;
            for (var j = 0; j < results.length; j++) {
                var resultClass = results[j] === 1 ? "box result correct" : "box result";
                $row.append('<div class="' + resultClass + '"></div>');
            }
        }
    };

    $.ajax({
        url: '/score',
        type: 'GET',
        dataType: 'json',
        success: update
    });

});

$(document).ready(function(){

    $.ajax({
        url: '/score',
        type: 'GET',
        dataType: 'json',
        success: function() {
            alert("success!")
        },
        error: function() {
            alert("error");
        }
    });

});

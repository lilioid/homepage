document.onkeypress = function (ev) {
    $.ajax("./handler.php", {
        data: {key:ev.key},
        method: 'GET'
    }).done(function (data) {
        data = $.trim(data);
        if (data !== 'nope') {
            $('#navbar').append('<section class=\'navbar-section\'><a href=\'' + data + '\' class=\'btn btn-link\'>Challenge 3</a></section>')
        }
    });
}
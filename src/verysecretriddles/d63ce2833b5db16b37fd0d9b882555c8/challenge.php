<!doctype html>
<html lang="en">
<head>
    <title>Finns Challenge 2</title>
    <?php
    include "../challenge_framework.head.php";
    ?>
    <script>
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
    </script>
</head>


<body>
<?php
$currentRiddle = 2;
include "../challenge_framework.body.php";
?>

<h3>Ooh, you got that one <i>right</i>. But where to go from here?</h3>

</body>

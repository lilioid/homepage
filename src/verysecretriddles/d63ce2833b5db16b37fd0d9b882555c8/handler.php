<?php
    require "../challenge_generator.php";

    $key = $_GET['key'];
    if ($key == 'ArrowRight' | $key == 'l') {
        echo calc_link(3);
    } else {
        echo "nope";
    }
?>


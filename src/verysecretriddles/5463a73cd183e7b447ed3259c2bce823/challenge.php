<!doctype html>
<html lang="en">
<head>
    <title>Finns Challenge 3</title>
    <?php
    require "../challenge_framework.head.php";
    ?>
</head>

<body>
<?php
$currentRiddle = 3;
require "../challenge_framework.body.php";
?>

<video class="mx-2" width="720" height="360" autoplay loop>
    <?php
    do {
        $videos = scandir("videos");
        $video = $videos[array_rand($videos, 1)];
    } while ($video == '..' || $video == '.');

    echo "<source src='videos/$video'>"
    ?>
</video>

</body>

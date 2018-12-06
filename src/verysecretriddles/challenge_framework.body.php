<?php

require "challenge_generator.php";

if ($currentRiddle == null) {
    echo "<h1>\$currentRiddle is null</h1>";
    return;
}

echo "<header id='navbar' class='navbar'>
    <section class='navbar-section'>
        <span class='navbar-brand mr-2'>Finns Cryptochallenges / Riddles</span>
    </section>";

echo "<section class='navbar-section'><a href='/verysecretriddles/windowsupdate.php' class='btn btn-link'>Challenge 1</a></section>";
for ($i = 2; $i <= $currentRiddle; $i++) {
    $link = calc_link($i);
    echo "<section class='navbar-section'><a href='$link' class='btn btn-link'>Challenge $i</a></section>";
}

echo "</header>";

echo "<div class='divider my-2 py-2'></div>";

$nextRiddle = $currentRiddle + 1;
$nextFolder = calc_folder($nextRiddle);
$nextLink = calc_link($nextRiddle);

?>


<?php

function calc_folder($number)
{
    $secret = "495bba4c591f4526cdae78a2ec2ae3f3ee0ad56da2e326391d52117aa2a267f7";
    return md5("$secret/$number");
}

function calc_link($number)
{
    $baseUrl = "/verysecretriddles";
    $folder = calc_folder($number);
    return "$baseUrl/$folder/challenge.php";
}

?>
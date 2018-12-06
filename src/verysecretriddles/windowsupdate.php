<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Windows Update</title>
</head>
<body>
<?php

    $userAgent = $_SERVER['HTTP_USER_AGENT'];
    if (strpos(strtolower($userAgent), 'linux') == false) {
        echo "
        
        <h1>Windows Update has crashed.</h1>
        <br><br><br><br>
        <p>Of course it has. It is Windows after all.. Please use something decent</p>
    
    ";
    } else {
        echo "
        
        <p>Ahhh, that's a better Operating System.</p>
        <p>Here, take this as a token of appreciation:</p>
        <blockquote>F53GK4TZONSWG4TFORZGSZDENRSXGL3EGYZWGZJSHAZTGYRVMRRDCNTCGM3WMZBQMQ4WEOBYGI2TKNLDHAXWG2DBNRWGK3THMUXHA2DQBI======
</blockquote>
        
        ";
    }

    ?>
</body>
</html>
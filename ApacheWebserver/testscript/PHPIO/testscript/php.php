<?php
    $uid=$_REQUEST['userid'];
    //[IP ADDRESS]/testscript/php.php?userid=2 will set $uid = 2
    $item= $uid.'Everything is awesome!!';
    $tmp = exec("python py.py $item");
    echo $tmp;
?>
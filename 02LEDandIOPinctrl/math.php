<?php
    
    $args1 = $_REQUEST['arg1'];
    $args2 = $_REQUEST['arg2'];
    $sum = exec("python pythonadd.py $args1 $args2");
    echo $sum;

?>
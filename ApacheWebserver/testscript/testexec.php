<?php
$a = 'Hello';
echo "$a";
$b = shell_exec("/var/www/html/testscript/test.sh");
header('Location: http://192.168.50.141/index.html?success='.$b);
//echo "$b";

?>
<?php
shell_exec("/var/www/html/testscript/test.sh");
header('Location: http://192.168.50.100/testscript/index.html?success=true');
?>
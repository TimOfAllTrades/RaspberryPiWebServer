# Raspberry Pi Server

Hello

This repository contains an example on how to run server side python scripts via php using html and javascript.  The end goal is to control GPIO pins on the raspberry pi through a simple web interface and return necessary status return codes as needed.  The Raspberry pi uses apache web server with php 7.1 installed to create the webpage and server side scripts.  Index.html contains javascript to call php functions periodically as a way to constantly check the status of the GPIO pins in real time, and there are button activated javascript functions too for when control is needed.

Instructions to set up the Raspberry Pi server after the default OS has been loaded

Step          | Command to run in terminal
-----------------------|--------------------------------
1.&nbsp;Install&nbsp;Apache           |  sudo apt install apache2 -y 
2.&nbsp;Add&nbsp;Pi&nbsp;to&nbsp;Apache's&nbsp;usergroup&nbsp;for&nbsp;easier&nbsp;editing. | sudo usermod -a -G www-data pi
3.&nbsp;Set&nbsp;user&nbsp;permissions&nbsp;(Although&nbsp;by&nbsp;default&nbsp;this&nbsp;should&nbsp;already&nbsp;be&nbsp;set) | sudo chown -R -f www-data:www-data /var/www/html data type.
4.&nbsp;Give&nbsp;execution&nbsp;permissions | sudo chmod -R 777 /var/www/
5.&nbsp;Install&nbsp;php | sudo apt install php7.3 libapache2-mod-php7.3 php7.3-mbstring php7.3-mysql php7.3-curl php7.3-gd php7.3-zip -y
6.&nbsp;Restart&nbsp;Apache&nbsp;if&nbsp;needed | service apache2 restart
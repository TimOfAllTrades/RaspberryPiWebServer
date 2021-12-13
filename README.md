# Raspberry Pi Server

Hello

This repository contains an example on how to run server side python scripts via php using html and javascript.  The end goal is to control GPIO pins on the raspberry pi through a simple web interface and return necessary status return codes as needed.  The Raspberry pi uses apache web server with php 7.1 installed to create the webpage and server side scripts.  Index.html contains javascript to call php functions periodically as a way to constantly check the status of the GPIO pins in real time, and there are button activated javascript functions too for when control is needed.

Instructions to set up the Raspberry Pi server after the default OS has been loaded

Step          | Command to run in terminal
-----------------------|--------------------------------
1.&nbsp;Install&nbsp;Apache           |  sudo apt install apache2 -y 
2.&nbsp;Add&nbsp;Pi&nbsp;to&nbsp;Apache's&nbsp;usergroup&nbsp;for&nbsp;easier&nbsp;editing. | sudo usermod -a -G www-data pi
3.&nbsp;Set&nbsp;user&nbsp;permissions&nbsp;(If&nbsp;needed) | sudo chown -R -f www-data:www-data /var/www/html data type.
4.&nbsp;Give&nbsp;execution&nbsp;permissions | sudo chmod -R 777 /var/www/
5.&nbsp;Install&nbsp;php | sudo apt install php7.3 libapache2-mod-php7.3 php7.3-mbstring php7.3-mysql php7.3-curl php7.3-gd php7.3-zip -y
6.&nbsp;Restart&nbsp;Apache&nbsp;if&nbsp;needed | service apache2 restart
7.&nbsp;Set&nbsp;GPIOmem&nbsp;owner&nbsp;to&nbsp;www-data | sudo chown www-data /dev/gpiomem
8.&nbsp;Get&nbsp;video&nbsp;streaming&nbsp;software&nbsp;| sudo apt-get install motion It may be necessary to do 'sudo apt-get update' first
9.&nbsp;Set&nbsp;ttys0&nbsp;owner&nbsp;to&nbsp;www-data | sudo chown www-data /dev/ttyS0



Project          | Purpose
-----------------------|--------------------------------
1.&nbsp;01SimpleAjaxPhpPy&nbsp;           |  Contains the most basic functions of html, javascript, php and python.  In this webpage, a javascript is used to routinely call a php, which then runs a simply python addition script and then returns the python's console out.  There is also a button which can manually start call a php and python, although its output is synchronized with the 1 second refresh of the javascript.
2.&nbsp;02LEDandIOPinctrl&nbsp;           |  Contains a script to communicate with the GPIO pins on the raspberry pi by controlling the LED on off state and reading the button pressed state.
3.&nbsp;03MotionWebserver | Contains a snippet to turn a USB camera into a webcam
4.&nbsp;04SerialIN | Contains code to begin the serial stream from an arduino UNO and read it on raspberry pi. 
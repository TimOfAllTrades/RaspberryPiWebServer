# Raspberry Pi Server

Hello

This repository contains an example on how to run server side python scripts via php using html and javascript.  The end goal is to control GPIO pins on the raspberry pi through a simple web interface and return necessary status return codes as needed.  The Raspberry pi uses apache web server with php 7.1 installed to create the webpage and server side scripts.  Index.html contains javascript to call php functions periodically as a way to constantly check the status of the GPIO pins in real time, and there are button activated javascript functions too for when control is needed.

Instructions to set up the Raspberry Pi server after the default OS has been loaded

Step          | Command to run in terminal
-----------------------|--------------------------------
1.&nbsp;Install&nbsp;Apache           |  sudo apt install apache2 -y 
1.&nbsp;Add&nbsp;Pi&nbsp;to&nbsp;www-data&nbsp;Usergroups&nbsp;for&nbsp;easier&nbsp;editing. | sudo usermod -a -G www-data pi
03 | An example on how to dynamically link compiled C++/GPU code to python via ctypes.  Explains how to do pass numpy array pointers, numbers to the C/GPU functions with the proper data type.
04 | An example on how to flatten, pass and then reshape numpy arrays into a compiled DLL for processing and also shows an example of using the 3D grid in CUDA.  The example assumes the numpy array created in python is Fortran ordering, i.e. matrix indicies are such matrix[x][y][z] not matrix[z][y][x] (C ordering).
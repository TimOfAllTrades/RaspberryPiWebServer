#!/usr/bin/env python3
import serial
if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyS0', 9600, timeout=1)
    ser.flush()

    # if ser.in_waiting > 0:
    line = ser.readline().decode('utf-8').rstrip()
    print(line)

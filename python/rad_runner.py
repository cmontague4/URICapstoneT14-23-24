# Capstone 2023-2024
# Team 14 - Radiation Detection Drone
# Radiation, Time, and Position Reading


import serial
import time

reader = serial.Serial(port = '/dev/ttyUSB0', baudrate = 9600, timeout = 0.05)

while True:
    data = reader.readline().decode().strip()
    print(data)

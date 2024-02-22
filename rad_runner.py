# Capstone 2023-2024
# Team 14 - Radiation Detection Drone
# Radiation, Time, and Position Reading

import serial
import time
import math
import statistics
import tkinter as tk
import datetime

window = tk.Tk()
window.title("Radiation Detection Control")
window.geometry('500x200')

reader = serial.Serial(port = '/dev/ttyUSB0', baudrate = 9600, timeout = 0.05)
rad_data = []
time_data = []
location_data = []

def read_rad():
    data = reader.readline().decode().strip()
    try:
        int(data)
    except:
        return 0
    return int(data)

def write_data(rads, times, locations):
    
    out_file = open("rad-data.csv", "w")
    out_file.write("Counts Per Second,Time,Location\n")
    
    for i in range(len(rads)):
        str_to_write = str(rads[i]) + "," + times[i] + ',' + str(locations[i]) + "\n"
        out_file.write(str_to_write)

    out_file.close()
    return


def Start():
    rad_interval = 1000
    rad_time = time.time()*1000
    rad_count = 0
    while True:
        window.update()
        rad_count += read_rad()
        if time.time() * 1000 - rad_time >= rad_interval:
            rad_time = time.time()*1000
            rad_data.append(rad_count)
            current_time = datetime.datetime.now()
            time_data.append(current_time.strftime("%m:%d:%Y-%H:%M:%S"))
            location_data.append(1) #placeholder number until we get the GPS working
            rad_count = 0
            
def Stop():
    write_data(rad_data, time_data, location_data)
    quit()

start_button = tk.Button(text = "Start", command = Start, width = 10)
start_button.place(x = 170, y = 100)

stop_button = tk.Button(text = "Stop", command = Stop, width = 10)
stop_button.place(x = 40, y = 100)

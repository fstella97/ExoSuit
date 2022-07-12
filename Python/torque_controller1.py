# Simple PID controller

import sys
import time
import socket
import json
import math
sys.path.append('libraries/')
sys.path.append('config/')

from libraries.comms_wrapper import *
from config.config_controller1 import *

# Connect loadcell arduino
IMU_shoulder = Arduino( descriptiveDeviceName=IMU_shoulder["name"], 
                    portName=IMU_shoulder["port"], 
                    baudrate=IMU_shoulder["baudrate"])

IMU_shoulder.connect_and_handshake()


# Main loop
timer = time.time()
while 1: 

    #print(time.time() - timer, loadcell._rawReceivedMessage)
    IMU_shoulder.receive_message()

       
    t = time.time() - timer
    raw_x = float(IMU_shoulder.receivedMessages["x"])
    raw_y = float(IMU_shoulder.receivedMessages["y"])
    raw_z = float(IMU_shoulder.receivedMessages["z"])
    
        
    print(time.time() - timer,raw_x,raw_y,raw_z)
    

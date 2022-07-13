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
IMU_trunk = Arduino( descriptiveDeviceName=IMU_trunk["name"], 
                    portName=IMU_trunk["port"], 
                    baudrate=IMU_trunk["baudrate"])
IMU_shoulder = Arduino( descriptiveDeviceName=IMU_shoulder["name"], 
                    portName=IMU_shoulder["port"], 
                    baudrate=IMU_shoulder["baudrate"])

IMU_shoulder.connect_and_handshake()
IMU_trunk.connect_and_handshake()

# Main loop
timer = time.time()
trunk=[0,0,0]; 
shoulder=[0,0,0];
while 1: 

    #print(time.time() - timer, loadcell._rawReceivedMessage)
    IMU_shoulder.receive_message()
    IMU_trunk.receive_message()

    t = time.time() - timer
    
    shoulder[0] = float(IMU_shoulder.receivedMessages["x"])
    shoulder[1]=  float(IMU_shoulder.receivedMessages["y"])
    shoulder[2] = float(IMU_shoulder.receivedMessages["z"])
    
    trunk[0] = float(IMU_trunk.receivedMessages["x"])
    trunk[1] = float(IMU_trunk.receivedMessages["y"])
    trunk[2] = float(IMU_trunk.receivedMessages["z"])

        
    print(time.time() - timer,trunk[0],trunk[1],trunk[2])
    

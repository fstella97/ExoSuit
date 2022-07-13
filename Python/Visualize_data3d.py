# Simple PID controller

import sys
import time
import socket
import json
import math
import numpy as np 
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot as plt

sys.path.append('libraries/')
sys.path.append('config/')

from libraries.comms_wrapper import *
from config.config_controller1 import *
from utility import *

def update_line(hl, new_data):
	xdata, ydata, zdata = hl._verts3d
	hl.set_xdata(list(np.append(xdata, new_data[0])))
	hl.set_ydata(list(np.append(ydata, new_data[1])))
	hl.set_3d_properties(list(np.append(zdata, new_data[2])))
	plt.draw()

def plot_segment(hl,p1,p2):
    hl.set_xdata(list(np.append(p1[0],p2[0])))
    hl.set_ydata(list(np.append(p1[1],p2[1])))
    hl.set_3d_properties(list(np.append(p1[2],p2[2])))
    plt.draw()


def plot_human(hl,p):
 print(p)
 x=[];y=[];z=[];
 #for i in range(2):
 #   for j in range(len(p)):
 #       if j==0:
 #           x.append(p[i,j])
 #       if j==1:
 #           y.append(p[i,j])
 #       if j==2:
 #           z.append(p[i,j])
 x=p[:, 0]
 y=p[:, 1]
 z=p[:,2]
 hl.set_xdata(list(x))
 hl.set_ydata(list(y))
 hl.set_3d_properties(list(z)) 
 plt.draw()
  


# Connect loadcell arduino
IMU_trunk = Arduino(descriptiveDeviceName=IMU_trunk["name"], 
                    portName=IMU_trunk["port"], 
                    baudrate=IMU_trunk["baudrate"])
IMU_shoulder = Arduino(descriptiveDeviceName=IMU_shoulder["name"], 
                    portName=IMU_shoulder["port"], 
                    baudrate=IMU_shoulder["baudrate"])

IMU_shoulder.connect_and_handshake()
IMU_trunk.connect_and_handshake()

# Main loop
timer = time.time()
trunk=[0,0,0]; 
shoulder=[0,0,0];

map = plt.figure()
map_ax = Axes3D(map)
map_ax.autoscale(enable=True, axis='both', tight=True)

# # # Setting the axes properties
map_ax.set_xlim3d([-1.0, 1.0])
map_ax.set_ylim3d([-1.0,1.0 ])
map_ax.set_zlim3d([-1.0, 1.0])

hl, = map_ax.plot3D([0], [0], [0])


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
    R_trunk=rotation_matrix(trunk[0], trunk[1], trunk[2], order='zyx')
    R_shoulder=rotation_matrix(shoulder[0], shoulder[1], shoulder[2], order='zyx')
    R_trunk2shoulder=np.dot(R_shoulder,R_trunk.transpose())
    neck= np.array([0, 0, 1])
    neck2elbow= np.array([1, 0, 0])
    p1=R_trunk.dot(neck)
    p2= p1+R_trunk2shoulder.dot(neck2elbow)
    human=np.array([[0,0,0],p1,p2])
    print(p1)
    #print(time.time() - timer,neck[0],neck[1],neck[2])
    #update_line(hl, (trunk[0],trunk[1], trunk[2]))
    plot_human(hl,human)
  
    plt.show(block=False)     
    plt.pause(0.001)
    #print(time.time() - timer,trunk[0],trunk[1],trunk[2])
    

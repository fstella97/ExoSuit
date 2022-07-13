
import numpy as np 

R_trunk=np.array([[0,0,1],[0,1,0],[0,0,1]])

neck= np.array([0, 0, 1])
result=R_trunk.dot(neck)
print(R_trunk)
print(result)
#print(time.time() - timer,trunk[0],trunk[1],trunk[2])

print(R_trunk[0])
print(len(R_trunk))
x=[];y=[];z=[];
for i in range(len(R_trunk)):
    for j in range(len(R_trunk)):
        if j==0:
            x.append(R_trunk[i,j])
        if j==1:
            y.append(R_trunk[i,j])
        if j==2:
            z.append(R_trunk[i,j])
print(z)
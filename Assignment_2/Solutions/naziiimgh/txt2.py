# find the position

import numpy as np
  
data = np.loadtxt("2.txt", dtype='str')

up=0
down=0
forward=0

for i in range(0,len(data)):

    if str(data[i][0]) == 'up':
        up=up+int(data[i][1])

    if str(data[i][0]) == 'down':
        down=down+int(data[i][1])


    if str(data[i][0]) == 'forward':
        forward=forward+int(data[i][1])

if down>up:
    down=down-up
    place=down*forward
elif up>down:
    up=up-down
    place=up*forward

print(place)




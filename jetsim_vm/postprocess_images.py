xMain = 0.0
yMain = 0.0
counter = 0

def onClick(event):
    global xMain, yMain, counter
    x, y = event.xdata, event.ydata
    xMain = int(x)
    yMain = int(y)
    
    now = str(datetime.now())
    now = now.replace(" ", "")
    now = now.replace(".", "")
    now = now.replace(":", "-")

    newName = str(xMain) + "_" + str(yMain) + "_" + str(now) + ".jpg"
    
    print(newName)
    
    os.rename(imageName,('./keyboard_images/' + newName)) #images, lane_change, lane_cone_avoid. I made difernet folders for each training scenario. 
    
    counter = counter + 1
    print(str(counter) + " image(s) renamed")
    plt.close()

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os
import glob
from datetime import datetime

list = glob.glob("./keyboard_images/*.jpg") #images, lane_change, lane_cone_avoid
list.sort()
print(str(len(list)) + " images total")

for imageName in list:
    name = imageName
    img = mpimg.imread(imageName)
    plt.connect('button_press_event', onClick)
    imgplot = plt.imshow(img)
    plt.show()








# single_test_subject_data_analysis.py

import numpy as np
import matplotlib.pyplot as plt

def readFile(file):
    data=[]
    time=[]
    file = open(file)
    # get rid of column titles
    file.readline()
    #read data
    data = file.readlines()
    # put data in lists
    for i in range(len(data)):
        pair = data[i].split()
        #print(pair[0])
        data.append(pair[0])
        time.append(int(pair[1]))
    # first 5 elements of data, they go like this - '10\t12875\n'. not sure why...
    return (data[5:],time)


# Create a figure
fig = plt.figure(figsize=(12, 7))
fig.canvas.set_window_title('Single test subject data') 
fig.subplots_adjust(wspace=0.3)
suptitle = plt.suptitle('Analysis of a single test subject data', fontsize=18)


# Plot Blurriness

## read file saved_data_blur.txt
blurr, time = readFile("saved_data_blur.txt")

## plot data
ax1 = fig.add_subplot(221)
ax1.plot(blurr,time)
ax1.set_xlabel('Blurriness')
ax1.set_ylabel('Time (ms)')

# Color

color, time = readFile("saved_data_color.txt")

ax2 = fig.add_subplot(222)

width=0.8
bars = ax2.bar([0,1,2,3,4], time, width, align='center', edgecolor='black')
plt.xticks(np.array([0, 1, 2, 3, 4]),color)
ax2.set_ylabel('Time (ms)')

for i in range(len(color)):
    bars[i].set_facecolor(color[i])

# Size

size, time = readFile("saved_data_size.txt")
size.append(0)
time.append(0)

ax3 = fig.add_subplot(223)
ax3.plot(size,time)
ax3.set_xlabel('Size')
ax3.set_ylabel('Time (ms)')


# Distance

dist, time = readFile("saved_data_dist.txt")

ax4 = fig.add_subplot(224)
ax4.plot(dist,time)
ax4.set_xlabel('Distance')
ax4.set_ylabel('Time (ms)')

plt.show()

# 'Model.py' | Anastasia Bolotnikova | 23.05.14

from matplotlib import pyplot as plt
import numpy as np


d = 9000

s = d + 3000

end = s + 100


def node_1(ax,d,s,end,effect=0):

    ax.set_title("Node 1: Sensory adaptation")
    
    # 0 < x < d

    x = np.arange(0,d,10)
    y = -x*(10/d)+10

    # d < x < s

    z = np.arange(d,s,10)

    w = [0]*len(z)

    # s < x < end

    l = np.arange(s,end,1)

    m = l/10-s/10


    X = np.concatenate((x,z,l))

    Y = np.concatenate((y,w,m))

    noise = np.random.normal(0,0.3,len(Y))
    Y = Y + noise

    node_4(ax,d,s,X,Y,end)

    ax.plot(X,Y)
    

def node_2(ax,d,s,end,effect):

    ax.set_title("Node 2: Neural adaptation")
    
    # 0 < x < d

    x = np.arange(0,d,10)
    y = -x*(10/(d-effect))+10

    # d < x < s

    z = np.arange(d,s,10)

    w = [0]*len(z)

    # s < x < end

    l = np.arange(s,end,1)

    m = l/10-s/10


    X = np.concatenate((x,z,l))

    Y = np.concatenate((y,w,m))

    noise = np.random.normal(0,0.3,len(Y))
    Y = Y + noise

    ax.plot(X,Y)

    node_4(ax,d,s,X,Y,end)


def node_3(ax,d,s,end,effect):

    ax.set_title("Node 3: Filling-in the missing informtion")
    
    # 0 < x < d

    x = np.arange(0,d,10)
    y = -x*(10/(d-effect))+10

    # d < x < s

    z = np.arange(d,s,10)

    w = [0]*len(z)

    # s < x < end

    l = np.arange(s,end,1)

    m = l/10-s/10


    X = np.concatenate((x,z,l))

    Y = np.concatenate((y,w,m))

    noise1 = np.random.normal(0,0.3,len(Y))
    Y = Y + noise1

    # Node 3 background

    b = x*(2/d)+10

    b2 = [12]*len(z)

    b3 = np.arange(12,10,-0.02)

    Y4 = np.concatenate((b,b2,b3))

    Y4 = Y4 + noise1

    ax.plot(X,Y4,'g', label="Background stimulus")
    
    node_4(ax,d,s,X,Y,end)
    
    ax.plot(X,Y)


def node_4(ax,d,s,X,Y,end):
    
    X_length = len(X)
    
    noise = np.random.normal(0,0.3,X_length)

    ax.plot(X,[10]*X_length+noise,'k',label="Node 4")

    ax.plot([d]*X_length,Y*2,'m--',label="D time point")
    ax.plot([s]*X_length,Y*2,'r--',label="S time point")
    
    ax.set_xlabel('Time (ms)')
    ax.set_ylabel('Response level')

    ax.legend(loc=3,fontsize='10')
    ax.set_ylim(0,13)
    ax.set_xlim(0,end+100)

    
def model(d,s,end):
    fig = plt.figure(figsize=(8, 12))
    fig.canvas.set_window_title('Troxler Effect Model')
    fig.subplots_adjust(hspace=.5)
    suptitle = plt.suptitle('Model nodes behavior during the experiment', fontsize=18)

    ax1 = fig.add_subplot(311)
    node_1(ax1,d,s,end)

    ax2 = fig.add_subplot(312)
    node_2(ax2,d,s,end,200)

    ax3 = fig.add_subplot(313)
    node_3(ax3,d,s,end,400)

    plt.show()


model(d,s,end)
    







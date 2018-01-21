import numpy as np
import matplotlib
from matplotlib import pylab, mlab, pyplot

from IPython.core.pylabtools import figsize, getfigs 

style.use('ggplot')
rcParams['figure.figsize'] = (10,10) 

from IPython.core.display import display, HTML
display(HTML("<style>.container { width:90% !important; }</style>"))

N = 5 #number of iterations

#make a competition matrix
m = 3 #pairs of prey/predators 
e = zeros((m,m))
j = 1
for i in range (m):
    while (j < m): 
        e[i][j] = uniform(0,10)
        j += 1
    j = i + 2

e += e.transpose()

prey = zeros((m,N))
pred = zeros((m,N))

#initialize with some populations
prey[0][0] = 150
prey[1][0] = 150
prey[2][0] = 150

pred[0][0] = 50
pred[1][0] = 40
pred[2][0] = 30

b_rate = zeros(m) #birth rate
p_rate = zeros(m) #predation rate
d_rate = zeros(m) #decay rate
B_size = zeros(m) #burst size

for i in range (m):
    b_rate[i] = uniform(0,10)
    p_rate[i] = uniform(0,10)
    d_rate[i] = uniform(0,10)
    B_size[i] = uniform(0,10)

for i in range (m):
    for j in range(N -1): 
        prey[i][j+1] = b_rate[i]*prey[i][j] - p_rate[i]*pred[i][j]*prey[i][j] - dot(e[i],prey.transpose()[i]) #Fix the sum
        if(prey[i][j+1]<=0): prey[i][j+1] = 0
        pred[i][j+1] = B_size[i]*p_rate[i]*prey[i][j]*pred[i][j] - d_rate[i]*pred[i][j]
        if (pred[i][j+1] <= 0): pred[i][j+1] = 0
        
        
for i in range(m):
    plot(prey[i])
    plot(pred[i])

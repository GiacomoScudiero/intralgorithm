import numpy as np

def getC(x):
    vl = []
    try:
        data[2].index(x)
    except ValueError:
        return 0.0
    for i in range (1,int(data[2][data[2].index(x)+1])+1):
        s=0
        for j in range (1,int(data[3][data[3].index(data[2][data[2].index(x)+1+i])+1])+1):
            try:
                s+=float(data[1][data[1].index(data[3][data[3].index(data[2][data[2].index(x)+1+i])+1+j])+1])
            except:
                s+=0
        vl.append(s)
    if (int(data[2][data[2].index(x)+1])>1):
        return 1/(1+np.e**(-1*float(sum(vl)/len(vl))))-1/2
    else:
        return 1/(1+np.e**(-1*float(vl[0])))-1/2

def getS(x):
    if(x>=0.0): return 1.0
    else: return -1.0
    
def getV(x,y):
    if((x>=0) and (y<0)) or ((y>=0) and (x<0)):
        if float(abs(x)-abs(y))==0:
            return 1/((abs(x)+abs(y))*5)
        else:
            return float(abs(x)-abs(y))
    else:
        if abs(x-y)==0:
            return 0.01
        else:
            return float(abs(x-y))

with open('data.txt') as f:
    read_data = f.readline()

data = []
for i in range(0,4):
    data.append('')
    
for i in range(0,4):
    data[i] = read_data.split('#')[i].split(',')
    
intr = []
for i in range(0,int(data[0][2])):
    if (i==0):
        found = True
        try: 
            data[1].index(data[0][3]) 
        except ValueError: 
            found = False
        if found: 
            intr.append(np.tanh(float(data[0][4])*float(data[1][data[1].index(data[0][3])+1])+(1.0/(6.0*getV(float(data[0][4]),float(data[1][data[1].index(data[0][3])+1])))))*getS(float(data[0][4])*float(data[1][data[1].index(data[0][3])+1])))
        else:
            intr.append(np.tanh(float(data[0][4])*getC(data[0][3])+(1.0/(6.0*getV(float(data[0][4]),getC(data[0][3])))))*getS(float(data[0][4])*getC(data[0][3])))
    else:
        found = True
        try: 
            data[1].index(data[0][3+i*2]) 
        except ValueError: 
            found = False
        if found: 
            intr.append(np.tanh(float(data[0][4+i*2])*float(data[1][data[1].index(data[0][3+i*2])+1])+(1.0/(6.0*getV(float(data[0][4+i*2]),float(data[1][data[1].index(data[0][3+i*2])+1])))))*getS(float(data[0][4+i*2])*float(data[1][data[1].index(data[0][3+i*2])+1])))
        else:
            intr.append(np.tanh(float(data[0][4+i*2])*getC(data[0][3+i*2])+(1.0/(6.0*getV(float(data[0][4+i*2]),getC(data[0][3+i*2])))))*getS(float(data[0][4+i*2])*getC(data[0][3+i*2])))

print(intr)

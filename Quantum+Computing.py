
# coding: utf-8

# In[3]:


import numpy as np

inWire = 1
numWires = 3

myState = [
    (numpy.sqrt(0.1),'00'),
    (numpy.sqrt(0.4),'01'),
    (-numpy.sqrt(0.5),'11')
    
]


# In[4]:


myState[0]


# In[5]:


import numpy


# In[6]:


collect = [(myState[0][1]),(myState[1][1]),(myState[2][1])]
collect


# In[7]:


def Hadamard(inWire,numWires,inputState):
    newState = []
    for element in inputState:
        
        #print (list(element[1]))
        if element[1][inWire-1] == '0':
            #print(numpy.sqrt(0.5)*float(1))
            a = ((numpy.sqrt(0.5)*(float(1))))
            newState.append((element[0]*a,element[1]))
            newString = list(element[1])
            newString[inWire-1] = '1'
            ''.join(newString)
            newState.append(((element[0]*a),''.join(newString)))
                            
        if element[1][inWire-1] == '1':
            b = ((numpy.sqrt(0.5)*float(-1)))
            newState.append((element[0]*b,element[1]))
            newString = list(element[1])
            newString[inWire-1] = '0'
            ''.join(newString)
            newState.append(((element[0]*b*(-1),''.join(newString))))
        #print(newState)
        #newState=RemoveDuplicates(newState)
    return newState 
Hadamard(2,2,myState)               


# In[8]:


mylist = (list ('00'))


# In[9]:


mylist[0] = '1'


# In[10]:


mylist


# In[11]:


''.join(mylist)


# In[12]:


def Cnot(inWire,numWires,inputState):
    newState=[]
    for element in inputState:
        #print(element[1][inWire-2])
        if element[1][inWire-2] == '1':
            if element[1][inWire-1]=='1':
                newString = list(element[1])
                newString[inWire-1] = '0'
         #       print(newString)
                ''.join(newString)
                newState.append((element[0],''.join(newString)))
                
            
            if element[1][inWire-2] == '1':
                if element[1][inWire-1]=='0':
                    newString = list(element[1])
                    newString[inWire-1] = '1'
         #          print(newString)
                    ''.join(newString)
                    newState.append((element[0],''.join(newString)))
                    
        if element[1][inWire-2] =='0':
            newState.append((element[0],element[1]))
    return newState
#print(myState)
Cnot(2,2,myState)


# In[13]:


def Phase(inWire,numWires,inputState,theta):
    newState=[]
    for element in inputState:
        if element[1][inWire-1]=='1':
                #newString = np.exp()
                #print(newString)
                #''.join(newString)
                newState.append((element[0]*np.exp((1.j*theta)),element[1]))
        if element[1][inWire-1]=='0':
            newState.append((element[0],element[1]))
    return newState
            
                
                
Phase(2,2,myState,0.2)


# In[14]:


def ReadInput(myInput_a):
        #myInput_lines=open(fileName).readlines()
        myInput_lines=myInput_a.split('\n')
        myInput=[]
        numberOfWires=int(myInput_lines[0])
        for line in myInput_lines[1:]:
            myInput.append(line.split())
            
        return (numberOfWires,myInput)


# In[15]:


myInput=ReadInput(
'''3
H 1 
CNOT 2 3 
P 1 0.45''')
#print(myInput[1][0][0])

numWire=myInput[0]
gate1 = myInput[1][0][0]
wire1 = myInput[1][0][1]
gate2 = myInput[1][1][0]
myState = [(1.0,'111')]

for line in range(0,3):
    gate = myInput[1][line][0]
    if gate == 'H':
        wire = int(myInput[1][line][1])
        myState=Hadamard(wire,numWire,myState)
    if gate == 'CNOT':
        wire1 = int(myInput[1][line][1])
        wire2 = int(myInput[1][line][2])
        myState = Cnot(wire2,numWire,myState)
    if gate =='P':
        wire = int(myInput[1][line][1])
        angle = float(myInput[1][line][2])
        myState = Phase(wire,numWire,myState,angle)
print(myState)


# In[16]:


def Rphase (inWire, inWire2, numWires, inputState, angle):
    newState=[]

    for element in inputState:
           # print(element[1][inWire-1])
            if (element[1][inWire-1]=='1'):
                if (element[1][inWire2-1]=='1'):
                     newState.append((element[0]*np.exp((1.j*angle)),element[1]))
                if (element[1][inWire2-1]=='0'):
                    newState.append((element[0],element[1]))
                
            if element[1][inWire-1]=='0':
                newState.append((element[0],element[1]))
    return newState
            
            
Rphase(2,1, 2,myState, 0.45)


# In[17]:


myInput = ReadInput(

'''3
H 3 
Rphase 2 3 1.57 
H 2
Rphase 1 3 0.78
Rphase 1 2 1.57
H 1 ''')
#print(myInput[1][0][0])

numWire=myInput[0]
gate1 = myInput[1][0][0]
wire1 = myInput[1][0][1]
gate2 = myInput[1][1][0]
myState = [(1.0,'111')]

print(myInput)
print(len((myInput[1])))
for line in range(0,len(myInput[1])):
    gate = myInput[1][line][0]
    if gate == 'H':
        wire = int(myInput[1][line][1])
        myState=Hadamard(wire,numWire,myState)
    if gate == 'CNOT':
        wire1 = int(myInput[1][line][1])
        wire2 = int(myInput[1][line][2])
        myState = Cnot(wire2,numWire,myState)
    if gate =='P':
        wire = int(myInput[1][line][1])
        angle = float(myInput[1][line][2])
        myState = Phase(wire,numWire,myState,angle)
    if gate == 'Rphase':
        wire1 = int(myInput[1][line][1])
        wire2 = int(myInput[1][line][2])
        angle = float(myInput[1][line][3])
        myState = Rphase(wire1, wire2,numWire,myState,angle)
print(myState)


# In[32]:


def fourier (inWire, numWires, inputState):
    lista = []
    listb = []
    for element in range(0,len(inputState)):
        for k in range(0,numWires):
            #print (inputState[element][1])
            lista = int(inputState[element][1])
            #print(lista)
            listb.append(((1/np.sqrt(numWires))*(np.exp(((1.j*6.28*inputState[element][0]*k)/numWires))),str(lista)))
          #  lista.append((1/np.sqrt(numWires))*(np.exp(((1.j*6.28*lista[1]*k)/numWires))))
           # listb = listb.append(np.sum(lista[0][1]))
                                    
            
            
    return listb
                                             
fourier(2,1,myState)  


# In[ ]:





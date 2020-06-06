import json
import random
from operator import itemgetter
llaves = [0,0,0,0]
PosIni = [[1,0,2],[0,0,0],[3,0,4]]
mov = [0,0,0,0]
posCab = [[0,1],[2,1],[6,-1],[8,-1]]
Tabl = [[0,0,0],[0,0,0],[0,0,0]]
Edo = 0
with open('4caballos.json') as file:
	data = json.load(file)

def MovCab(data,posCab,llaves,mov,Edo):
    Edo = Edo +1
    for t in range(len(posCab)):
        for d in data:
            if d[0] == posCab[t][0]:
                if (t == 0)and(llaves[0] == 0) and (mov[0] == 0):
                    posCab[t][0] = d[1]
                    mov[0] = 1
                    Tabl = Tabl(posCab[t][0],1)
                    if (posCab[t][0]) == 8:
                        llaves[t] = 1
            
                if (t == 1)and(llaves[1] == 0)and (mov[1] == 0):
                    posCab[t][0] = d[1]
                    mov[1] = 1
                    Tabl = Tabl(posCab[t][0],2)
                    if (posCab[t][0]) == 6:
                        llaves[t] = 1
                    
                if (t == 2)and(llaves[2] == 0)and (mov[2] == 0):
                    posCab[t][0] = d[1]
                    mov[2] = 1
                    Tabl = Tabl(posCab[t][0],3)
                    if (posCab[t][0]) == 2:
                        llaves[t] = 1
                    
                if (t == 3)and(llaves[3] == 0)and (mov[3] == 0):
                    posCab[t][0] = d[1]
                    mov[3] = 1
                    Tabl = Tabl(posCab[t][0],4)
                    if (posCab[t][0]) == 0:
                        llaves[t] = 1
    print("-------------------------------")
    print("Estado : "+ str(Edo))                
    for t in Tabl:
        print(t)
    print("--------------------------------")
   
    if 0 in llaves:
        mov = [0,0,0,0]
        Tabl = BorrTab(Tabl)
        return MovCab(data,posCab,llaves,mov,Edo)
    else:
        return

def Tabl(Posc,caballo):    
    if Posc==0:
        Tabl[0][0] = caballo
    if Posc==1:
        Tabl[0][1] = caballo
    if Posc==2:
        Tabl[0][2] = caballo
    if Posc==3:
        Tabl[1][0] = caballo
    if Posc==5:
        Tabl[1][2] = caballo
    if Posc==6:
        Tabl[2][0] = caballo
    if Posc==7:
        Tabl[2][1] = caballo
    if Posc==8:
        Tabl[2][2] = caballo
    return Tabl

def BorrTab(Tabl):
    for t in range(len(Tabl)):
        for r in range(len(Tabl[t])):
            Tabl[t][r] = 0
    return Tabl




print("Posces iniciales")
for t in PosIni:
    print(t)

MovCab(data,posCab,llaves,mov, Edo)
import math
import numpy as np
from metnum import *
from getInput import *
from matrixProcess import *


data = getInput()

# for datai in data:
#     print(datai)
#     print(data[datai])
#
#     print()

processed = matrixProcess(data)



ff = processed[0]
matrix_calcula = processed[1]
flat_temp2 = processed[2]
matriz_global = processed[3]
angs = processed[4]
lados = processed[5]
E_list = processed[6]
glcort = processed[7]

# print(np.matrix(matrix_calcula))
# print(np.matrix(matriz_global))

desloc = gauss(ff,matrix_calcula,1000,10**-4)

desloc_global = []
c = 0
for i in flat_temp2:
    if i == 1:
        desloc_global.append(desloc[c])
        c +=1
    else:
        desloc_global.append(0)

print("*DISPLACEMENTS")
for i in range(0,len(desloc_global),2):
    print("    {0} {1} {2}".format(int(i/2),desloc_global[i],desloc_global[i+1]))
print()

forcas = np.matrix(matriz_global) * np.transpose(np.matrix(desloc_global))


strain_list = calcStrain(data,angs,desloc_global,lados)

print("*ELEMENT_STRAINS")
for i in range(len(strain_list)):
    print("    {0} {1}".format(i,np.array(strain_list[i])[0]))

print()
stress_list = calcStress(strain_list,E_list)

print("*ELEMENT_STRESSES")
for i in range(len(stress_list)):
    print("    {0} {1}".format(i,np.array(stress_list[i])[0]))
print()

print("*REACTION_FORCES")
for i in range(len(forcas)):
    if(flat_temp2[i] == 0):
        if(i%2 == 0):
            print("    {0} FX = {1}".format(int(i/2)+1,np.array(forcas)[i][0]))
        else:
            print("    {0} FY = {1}".format(int(i/2)+1,np.array(forcas)[i][0]))

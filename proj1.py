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

# print(np.matrix(matrix_calcula))
# print(np.matrix(matriz_global))

desloc = gauss(ff,matrix_calcula,100,10**-4)

desloc_global = []
c = 0
for i in flat_temp2:
    if i == 1:
        desloc_global.append(desloc[c])
        c +=1
    else:
        desloc_global.append(0)

print()
print(np.array(desloc_global))




forcas = np.matrix(matriz_global) * np.transpose(np.matrix(desloc_global))


strain_list = calcStrain(data,angs,desloc_global,lados)
stress_list = calcStress(strain_list,E_list)

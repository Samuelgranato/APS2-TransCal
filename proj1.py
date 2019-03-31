import math
import numpy as np
from metnum import *
from getInput import *
from matrixProcess import *


data = getInput()
processed = matrixProcess(data)

ff = processed[0]
matrix_calcula = processed[1]
flat_temp2 = processed[2]
matriz_global = processed[3]

desloc = gauss(ff,matrix_calcula,100,10**-4)

desloc_global = []
c = 0
for i in flat_temp2:
    if i == 1:
        desloc_global.append(desloc[c])
        c +=1
    else:
        desloc_global.append(0)

print(desloc_global)




forcas = np.matrix(matriz_global) * np.transpose(np.matrix(desloc_global))

print(forcas)
# vetor_stress = []

# for i in angs:
#     vetor_stress.append([-i[0],-i[1],i[0],i[1]])

        
 

# # print(vetor_stress)
# # print(desloc_global)

# desloc_stress = []
# for i in range(0,len(desloc_global), 2):
#     desloc_stress.append([desloc_global[i], desloc_global[i+1]])

    

# desform_espec = []
# for i in range(len(lados)):
#     const = 1/lados[i]
#     vetor = vetor_stress[i]
#     vetor_desloc_total = []
#     for j in range(len(desloc_stress))
#         vetor_desloc = desloc_stress[]
#         if i+1 < len(lados):
#             vetor_desloc2 = desloc_stress[i+1]
#         else: 
#             vetor_desloc2 = desloc_stress[-1]
#     print(vetor,vetor_desloc)
    # desform_espec.append()
import math
import numpy as np

data = {}
temp_iteration = 0
for i in range(7):
    tipo = input()
    # print(tipo)
    if tipo == "*INCIDENCES":
        temp_sum=[]
        for nos in ((data['*ELEMENT_GROUPS'])):
            temp_sum.append(int(nos[1]))
        iterations = sum(temp_sum)
    else:
        iterations = int(input())

    nodes = []
    for i in range(iterations):
        pontos = input().split(" ")
        if (tipo == "*COORDINATES"):
            pontos.pop(0)
        nodes.append(pontos)


    data[tipo] = nodes
# print(data)

# for i in range(len(data["*ELEMENT_GROUPS"])):

lados = []
angs = []

for incidence in data["*INCIDENCES"]:
    x0 = float(data["*COORDINATES"][int(incidence[1]) - 1][0])
    x1 = float(data["*COORDINATES"][int(incidence[2]) - 1][0])

    y0 = float(data["*COORDINATES"][int(incidence[1]) - 1][1])
    y1 = float(data["*COORDINATES"][int(incidence[2]) - 1][1])

    L = math.sqrt((x1 - x0)**2 + (y1 - y0)**2)
    lados.append(L)
    cos = (x1 - x0) / L
    sin = (y1 - y0) / L
    angs.append([cos,sin])

matrizes = []


for incidence in range(len(data["*INCIDENCES"])):
    ke = []
    cos = angs[incidence][0]
    sin = angs[incidence][1]

    ke.append([cos**2, cos*sin,-1*cos**2,-1*cos*sin])
    ke.append([cos*sin, sin**2,-1*cos*sin,-1*sin**2])
    ke.append([-1*cos**2,-1*cos*sin,cos**2, cos*sin])
    ke.append([-1*cos*sin,-1*sin**2,cos*sin, sin**2])
    matrizes.append(ke)


gl = []
count = 0
for i in range(len(data["*COORDINATES"])):

    gl.append([count, count + 1])
    count += 2


matriz_global = []

for i in range(len(data["*ELEMENT_GROUPS"]) * 2):
    linha=[]
    for j in range(len(data["*ELEMENT_GROUPS"])* 2):

        linha.append(0)
    matriz_global.append(linha)


counter = 0
for i in range(len(data["*ELEMENT_GROUPS"])):
    m = matrizes[i]

    E = 210 *( 10**9)
    A = 2 * (10**-4)
    l = lados[i]



    gl1 = gl[int(data["*INCIDENCES"][i][1]) - 1]
    gl2 = gl[int(data["*INCIDENCES"][i][2]) - 1]

    glT = [gl1[0],gl1[1], gl2[0], gl2[1]]


    for i in range(4):
        for j in range(4):
            v = float((E*A)/l) * m[i][j]
            if (matriz_global[glT[i]][glT[j]] == 0):
                matriz_global[glT[i]][glT[j]] = v
            else:
                matriz_global[glT[i]][glT[j]] = matriz_global[glT[i]][glT[j]] + v

# print(np.matrix(matriz_global))
# print(data)
cc = []
temp = []
temp2 = []


for i in range(len(data["*COORDINATES"]) *2):
    temp.append(1)

for i in range(len(data["*COORDINATES"])):
    temp2.append([1,1])

# count = 0
# for i in range(len(data["*COORDINATES"])):
#     for j in range(2):
#         if (int (data["*BCNODES"][i][0]) == i+1):
#             print("rodou")
#             if (int (data["*BCNODES"][i][1]) == 1):
#                 temp[i] =  0
#             elif (int (data["*BCNODES"][i][1]) == 2):
#                 temp[i+j] = 0


# count = 1
# count_aux = 0
# for i in range(len(data["*BCNODES"])):
#     if(count == int( data["*BCNODES"][i][0])):
#         a = int( data["*BCNODES"][i][1])
#
#         print("entrou {0}".format(count))
#         if(a == 1 ):
#             temp[count-1] = 0
#         else:
#             temp[count + count_aux] = 0

for grau_list in data["*BCNODES"]:
    temp2[int(grau_list[0])-1][int(grau_list[1])-1] =0

index_count = 0
glcort = []




#     count_aux +1
#     if count_aux == 2:
#         count_aux = 0
#         count +=1






#     no = int(node[0])
#     value = int(node[1])

#     temp[count] = 0


print(np.squeeze(np.asarray(temp2)))
# print(data["*BCNODES"])







# print(temp)
# print(cc)

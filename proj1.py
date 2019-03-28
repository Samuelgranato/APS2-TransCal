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
    sin = math.sqrt(1 - (cos**2))   
    angs.append([cos,sin])    

matrizes = []


for incidence in range(len(data["*INCIDENCES"])):
    ke = []
    # print(angs[inscidence])
    cos = angs[incidence][0]
    sin = angs[incidence][1]
    ke.append([cos**2, cos*sin,-1*cos**2,-1*cos*sin])
    ke.append([cos*sin, sin**2,-1*cos*sin,-1*sin**2])
    ke.append([-1*cos**2,-1*cos*sin,cos**2, cos*sin])
    ke.append([-1*cos*sin,-1*sin**2,cos*sin, sin**2])
    matrizes.append(ke)

# print(matrizes[0])

gl = []
count = 0
for i in range(len(data["*COORDINATES"])):
    
    gl.append([count, count + 1])
    count += 2


matrizes_elemento = []

for incidence in data["*INCIDENCES"]:
    for i in range(len(data["*ELEMENT_GROUPS"]) * 2):
        linha=[]
        for j in range(len(data["*ELEMENT_GROUPS"])* 2):
            linha.append(0)
    matrizes_elemento.append(linha)

counter = 0
for i in range(len(data["*ELEMENT_GROUPS"])):
    m = np.matrix(matrizes[i])
    
    E = 210 *( 10**9)
    A = 2 * (10**-4)
    l = lados[i]

    m = (E*A)/l * m
    linha = [0,0,0,0,0,0]
    
    gl1 = gl[int(data["*INCIDENCES"][i][1]) - 1]
    gl2 = gl[int(data["*INCIDENCES"][i][2]) - 1]
    print(gl1,gl2)
    # linha.insert(gl1/, m)
    # linha.insert(gl2/,m)
    # matrizes_elemento.insert()

print(np.matrix(matrizes[0]))
# print(gl)
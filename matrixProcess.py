import math
import numpy as np

def matrixProcess(data):
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
        angs.append([cos, sin])

    matrizes = []


    for incidence in range(len(data["*INCIDENCES"])):
        ke = []
        cos = angs[incidence][0]
        sin = angs[incidence][1]

        ke.append([cos**2, cos*sin, -1*cos**2, -1*cos*sin])
        ke.append([cos*sin, sin**2, -1*cos*sin, -1*sin**2])
        ke.append([-1*cos**2, -1*cos*sin, cos**2, cos*sin])
        ke.append([-1*cos*sin, -1*sin**2, cos*sin, sin**2])
        matrizes.append(ke)

    gl = []
    count = 0
    for i in range(len(data["*COORDINATES"])):

        gl.append([count, count + 1])
        count += 2

    temp = []
    temp2 = []


    for i in range(len(data["*COORDINATES"]) * 2):
        temp.append(1)

    for i in range(len(data["*COORDINATES"])):
        temp2.append([1, 1])


    for grau_list in data["*BCNODES"]:
        temp2[int(grau_list[0])-1][int(grau_list[1])-1] = 0


    index_count = 0
    glcort = {}

    for i in range(len(temp2)):
        for j in range(2):
            index_count += 1
            if temp2[i][j] == 1:
                glcort[str(index_count - 1)] = temp2[i].count(1)

    c = 0
    for i in glcort.values():
        c += i

    matriz_global = []

    for i in range(c):
        linha = []
        for j in range(c):

            linha.append(0)
        matriz_global.append(linha)

    # print(np.matrix(matrizes[-1]))
    # print(np.matrix(matriz_global))

    counter = 0
    for i in range(len(data["*ELEMENT_GROUPS"])):
        m = matrizes[i]

        # E = float(data["*MATERIALS"][0][0])
        # A = float(data["*GEOMETRIC_PROPERTIES"][0][0])
        l = lados[i]
        E = 21 * 10**5
        A = 10

        gl1 = gl[int(data["*INCIDENCES"][i][1]) - 1]
        gl2 = gl[int(data["*INCIDENCES"][i][2]) - 1]

        glT = [gl1[0], gl1[1], gl2[0], gl2[1]]
        for i in range(4):
            for j in range(4):
                # print(glT[i], glT[j])
                v = float((E*A)/l) * m[i][j]
                if (matriz_global[glT[i]][glT[j]] == 0):
                    matriz_global[glT[i]][glT[j]] = v
                else:
                    matriz_global[glT[i]][glT[j]] = matriz_global[glT[i]][glT[j]] + v

    # print(np.matrix(matriz_global))
    # print(data)
    # print(glcort)
    # print(lados)
    # print(temp2)

    matrix_calcula = []
    for i in glcort.keys():
        linha = []
        for j in glcort.keys():
            linha.append(matriz_global[int(i)][int(j)])

        matrix_calcula.append(linha)


    flat_temp2 = []
    for sublist in temp2:
        for item in sublist:
            flat_temp2.append(item)

    F = []
    for i in range(len(flat_temp2)):
        F.append(0)

    # for i in matrizes:
    #     print(np.matrix(i))

    for list in data["*LOADS"]:
        F[int(list[0]) + int(list[1])] = int(list[2])


    #
    # print(np.matrix(matriz_global))
    # print(np.matrix(matrix_calcula))
    # print(F)
    # print(glcort)

    ff = []
    for i in glcort.keys():
        ff.append(F[int(i)])

    return ff, matrix_calcula, flat_temp2,matriz_global

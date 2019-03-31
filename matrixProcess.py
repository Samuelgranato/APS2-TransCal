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


    matriz_global = []

    for i in range(len(data["*ELEMENT_GROUPS"]) * 2):
        linha = []
        for j in range(len(data["*ELEMENT_GROUPS"]) * 2):

            linha.append(0)
        matriz_global.append(linha)

    # print(np.matrix(matrizes[-1]))

    counter = 0
    E_list = []
    for i in range(len(data["*ELEMENT_GROUPS"])):
        m = matrizes[i]

        E = float(data["*MATERIALS"][0][0])
        E_list.append(E)

        A = float(data["*GEOMETRIC_PROPERTIES"][0][0])
        l = lados[i]

        gl1 = gl[int(data["*INCIDENCES"][i][1]) - 1]
        gl2 = gl[int(data["*INCIDENCES"][i][2]) - 1]

        glT = [gl1[0], gl1[1], gl2[0], gl2[1]]

        for i in range(4):
            for j in range(4):
                v = float((E*A)/l) * m[i][j]
                if (matriz_global[glT[i]][glT[j]] == 0):
                    matriz_global[glT[i]][glT[j]] = v
                else:
                    matriz_global[glT[i]][glT[j]
                                        ] = matriz_global[glT[i]][glT[j]] + v

    # print(np.matrix(matriz_global))
    # print(data)
    cc = []
    temp = []
    temp2 = []


    for i in range(len(data["*COORDINATES"]) * 2):
        temp.append(1)

    for i in range(len(data["*COORDINATES"])):
        temp2.append([1, 1])


    for grau_list in data["*BCNODES"]:
        temp2[int(grau_list[0])-1][int(grau_list[1])-1] = 0

    index_count = 0
    glcort = []

    for i in range(len(temp2)):
        for j in range(2):
            index_count += 1
            if temp2[i][j] == 1:
                glcort.append(index_count - 1)

    # print(glcort)
    # print(lados)
    # print(temp2)

    matrix_calcula = []
    for i in range(len(glcort)):
        linha = []
        for j in range(len(glcort)):
            linha.append(matriz_global[glcort[i]][glcort[j]])

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
    for i in range(len(glcort)):
        ff.append(F[glcort[i]])

    return ff, matrix_calcula, flat_temp2,matriz_global,angs,lados,E_list


# calcula a deformação dos elementos
def calcStrain(data,angs,desloc_global,lados):
    sincos_list =[]
    sincos_list_aux =[]

    for incidence in range(len(data["*INCIDENCES"])):
        sincos_list_aux = []
        cos = angs[incidence][0]
        sin = angs[incidence][1]

        sincos_list_aux.append(-cos)
        sincos_list_aux.append(-sin)
        sincos_list_aux.append(cos)
        sincos_list_aux.append(sin)

        sincos_list.append(sincos_list_aux)
    # print(np.array(desloc_global))
    print(sincos_list)
    print()
    print()
    strain_list = []
    element_desloc_list = []
    for incidence in data["*INCIDENCES"]:
        desloc_aux = []
        # print((int(incidence[1])-1)*2)
        # print((int(incidence[1])-1)*2 +1)
        # print()
        # print((int(incidence[2])-1)*2)
        # print((int(incidence[2])-1)*2 +1)
        # print()
        desloc_aux.append(desloc_global[(int(incidence[1])-1)*2])
        desloc_aux.append(desloc_global[(int(incidence[1])-1)*2 +1])
        desloc_aux.append(desloc_global[(int(incidence[2])-1)*2])
        desloc_aux.append(desloc_global[(int(incidence[2])-1)*2 +1])
        # strain_list.append(np.array(desloc_aux))
        # print(np.array(strain_list))
        desloc_aux = np.array(desloc_aux)
        desloc_aux.shape = (len(desloc_aux) , 1)
        element_desloc_list.append(desloc_aux)
        # print(desloc_aux)
        # print(np.array(sincos_list) *  desloc_aux )
        # print(np.transpose(desloc_aux))
        # break

    # print(element_desloc_list)

    for i in range(len(data["*INCIDENCES"])):
        strain_list.append((np.array(sincos_list)[i].dot( element_desloc_list[i]))/lados[i])

    return strain_list

def calcStress(strain_list,E_list):
    stress_list = []
    for i in range(len(strain_list)):
        stress_list.append(strain_list[i] * E_list[i])

    print(np.array(strain_list))
    print(np.array(stress_list))

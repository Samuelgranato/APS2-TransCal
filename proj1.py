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


print(data)
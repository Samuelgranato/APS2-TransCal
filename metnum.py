# maxIT = int(input("Insira o número máximo de iterações: "))
# tol = int(input("Insira a tolerância para o erro: "))

maxIT = 45
tol = 10

K = []
F = []
with open('inputmetnumk.txt', 'r') as f:
    for line in f:
        K.append(list(map(float,line.split())))

with open('inputmetnumf.txt', 'r') as f:
    for line in f:
        F.append(float(line))

nmaxIT = 0
ntol = tol +1

U = []
for f in F:
    U.append(0)

U_old = []
for f in F:
    U_old.append(0)

U_error = []
for f in F:
    U_error.append(0)

print(K)
print(U)
print(F)
print()

while(nmaxIT < maxIT and ntol > tol):
    for i in range(len(U)):
        U[i] = F[i] / K[i][i]
        print("U[{0}] = F[{0}]/ K[{0}][{0}] -> {1}/{2} ".format(i,F[i],K[i][i]))

        for j in range(0,len(U)):
            if(j != i):
                U[i] -= K[i][j] * U_old[j] / K[i][i]
                print("U[{0}] = U[{0}] - K[{0}][{1}] * U_old[{1}] / K[[{0}]][{0}] - >  {2} - {3} * {4} / {5} ".format(i,j,U[i],K[i][j],U_old[j],K[i][i]))

        print("U[{0}] = {1}".format(i,U[i]))

        if(U[i] != 0):
            U_error[i] = abs( (U[i] - U_old[i]) / U[i] )

    tol = max(U_error)
    nmaxIT +=1
    U_old = U.copy()
    print()


print(U)














# print(K)
# print()
# print(F)

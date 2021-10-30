#Problem: given positive integers n≤40 and k≤5, return The total number of rabbit pairs that will be present after n months, 
#if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair)
n = int(input("Insira o valor de meses: "))
k = int(input("Insira o valor de pares por geracao: "))

Fn = [1, 1]
Fn.append(1+k) #F3 sempre é 1 + o numero K de pares

for i in range(3, n):
    A = Fn[i-2] * k + Fn[i-1] 
    Fn.append(A)

print(Fn[n-1])

def factorial(n: int):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
    
def binomial_coeficient(n: int,k: int):
    return factorial(n)/(factorial(k)*factorial(n-k))
    

numRows = int(input())
ans = []
i = 0
while (i <= numRows):
    aux = []
    j = 0
    while (j <= i):
        aux.append(binomial_coeficient(i,j))
        print(i,j)
        j += 1
    i += 1
    print(aux)
    ans.append(aux)

print(ans)
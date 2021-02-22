def somadiag(x):
    soma=0
    for i in range(0,3):
        soma=soma+x[i][i]-x[3-i-1][i]
    return soma
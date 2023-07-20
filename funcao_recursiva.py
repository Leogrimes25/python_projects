def funcao_recursiva(n):
    if n==0:
        return 0
    else:
        return  n + funcao_recursiva(n-1)
resultado = funcao_recursiva(6)
print(resultado)

def fibonacci2(n):
    lista = [0]
    pwyrazy = (0, 1)
    a, b = pwyrazy
    while len(lista) < n:
        a, b = b, a+b
        lista.append(a)
    return lista


n = int(input())

print(fibonacci2(n))

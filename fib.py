def fibonacci2(n):
    lista = [0]
    pwyrazy = (0, 1)
    a, b = pwyrazy
    while len(lista) < n:
        a, b = b, a+b
        lista.append(a)
    print(lista)


n = int(input())

fibonacci2(n)

def fast(a, g ,N):
    g = bin(g)[2:]
    g = g[::-1]
    x = a
    d = 1
    for gi in g:
        if gi == '1':
            d = (d*x) % N
        x = (x ** 2) % N
    return d

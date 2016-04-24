import math
import fast

def gcd(x, y):
    (a,b,u,v,g,w) = (1,0,0,1,x,y)
    while w > 0:
        q = math.floor(g/w)
        t = w
        w = g % t
        g = t
        if w == 0:
            break
        U = a - q*u
        V = b - q*v
        a = u
        b = v
        u = U
        v = V
    return (g, U, V)

def powerMod(a,g,N):
    b = a % g
    for i in range(g-1):
        b = (a * b) % N

    return b


print("=== (i) ===")
(g, u ,v) = gcd(126048, 5050)
print("GCD(126048, 5050) = " + str(g))
print(str(int(u)) + " " + str(int(v)))
print("")

print("=== (ii) ===")
for i in range(1002):
    if (i*809)%1001 == 1:
        print(i)
        break
print("")

print("=== (iii) ===")
print("2^(100)mod101 = " + str(powerMod(2,100,101)))
print("")

print("=== (iv) ===")
print("2^(1234567)mod12345 = " + str(fast.fast(2,1234567,12345)))
print("130^(7654321)mod567 = " + str(fast.fast(130,7654321,567)))
print("")

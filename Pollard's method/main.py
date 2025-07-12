from Crypto.Util.number import getPrime
import math

# create N = pq, using two large primes.

def generate_n():
    p = getPrime(32)
    q = getPrime(32)
    print(p)
    print(q)
    return p * q

# pollard's p - 1 algorithm
def pollard(a, N, bound, k):
    for i in range(1, bound + 1):
        if (i % 500 == 0):
            print(f"pollard's p - 1 algorithm, iteration: {i}")
        a = a ** i # a = 2^(i!)
        a %= N
        if (i % k == 1): #calculate the gcd every kth iteration. 
            d = math.gcd(a - 1, N)
            if (d > 1 and d < N):
                return d
    return "failed"


def g(x):
    return x * x + 5

#pollard rho algorithm
def pollard_rho(N):
    x, y, d = 2, 2, 1
    i = 1
    while d == 1:
        if (i % 1000000 == 0):
            print(f"pollard rho algorithm, iteration: {i}")
        x = g(x) % N
        y = g(g(y)) % N
        d = math.gcd(x - y, N)
        i += 1
    if d < N:
        return d

N = generate_n()
k1 = pollard(2, N, 3000, 10)
k2 = pollard_rho(N)
print(f"pollard's p - 1 method: {k1}")
print(f"pollard rho method: {k2}")

# k = pollard(13927189, 14)
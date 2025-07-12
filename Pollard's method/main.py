from Crypto.Util.number import getPrime
import math

# create N = pq, using two large primes.

def generate_n(n):
    p = getPrime(n)
    q = getPrime(n)
    print(p)
    print(q)
    return p * q

# pollard's p - 1 algorithm
def pollard(a, N, bound, k):
    for i in range(1, bound + 1):
        a = a ** i # a = 2^(i!)
        a %= N
        if (i % k == 1): #calculate the gcd every kth iteration. 
            d = math.gcd(a - 1, N)
            if (d > 1 and d < N):
                return d
    return "failed"


def g(x):
    return x * x + 5

#pollard's rho algorithm
def pollard_rho(N):
    x, y, d = 2, 2, 1
    while d == 1:
        x = g(x) % N
        y = g(g(y)) % N
        d = math.gcd(x - y, N)
    if d < N:
        return d
    return "failed"



# testing and comparing Pollard's rho and Pollard's p - 1 algorithm on 32-bit primes 
def test1():
    score = [0, 0]
    iters = 50
    for i in range(iters):
        print(f"-------iteration{i}--------")
        N = generate_n(32)
        print(N)
        k1 = pollard(2, N, 3000, 10)
        k2 = pollard_rho(N)
        print(f"Pollard's p - 1 method: {k1}")
        print(f"Pollard's rho method: {k2}")
        if k1 != "failed":
            score[0] += 1
        if k2 != "failed":
            score[1] += 1

    print(f"Pollard's p - 1 algorithm: {score[0]} out of {iters}")
    print(f"Pollard's rho algorithm: {score[1]} out of {iters}")

#testing the Pollard's rho method for 64-bit primes
def test2():
    score = 0
    iters = 10
    for i in range(iters):
        print(f"-------iteration{i}--------")
        N = generate_n(50)
        print(N)
        k = pollard_rho(N)
        print(f"Pollard's rho method: {k}")
        if k != "failed":
            score += 1
    print(f"Pollard's rho algorithm: {score} out of {iters}")

test1()
# test2()
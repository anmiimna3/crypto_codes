# Pollard's methods

Here I implemented two different methods: Pollard's p-1 algorithm, and Pollard rho algorithm.
In both of them we are trying to break an RSA key $N = pq$, by finding either $p$ or $q$. 

1. Pollard's $p - 1$ algorithm

    this method uses the fact that if $N = pq$ where $p$ and $q$ are prime numbers, if for example
    $p - 1$ (or $q - 1$) is product of some small primes, then with a high probability we have that 
    $p - 1 \mid n!$ for some relatively small $n$ and we have $n! = (p - 1)k$ for some k. Assuming 
    this happens we have that for some $a$ (we use $a = 2$ in implementation for simplicity)
    $a^{n!} = (a^{p - 1})^{k} = 1 \pmod p$. Therefore since $p \mid a^{n!} - 1$ and $p \mid N$, then 
    finding $\gcd(a^{n!} - 1, N)$ could lead us to find $p$, although this might not always work, 
    because maybe $n$ is too large to find and compute and also that maybe $q$ also divide $a^{n!}$.
    Note that we can do all the calculations modulus $N$, since we are looking for these answers modulus $p$,
    but since we are already looking for $p$, we can use $N = pq$.
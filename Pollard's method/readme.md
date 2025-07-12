# Pollard's methods

Here I implemented two different methods: Pollard's p-1 algorithm, and Pollard rho algorithm.<br>
In both of them we are trying to break a **RSA** key $N = pq$, by finding either $p$ or $q$. 

## 1. Pollard's $p - 1$ algorithm
This method uses the fact that if $N = pq$ where $p$ and $q$ are prime numbers, if for example <br>
$p - 1$ (or $q - 1$) is product of some small primes, then with a high probability we have that <br>
$p - 1 \mid n!$ for some relatively small $n$ and we have $n! = (p - 1)k$ for some k. Assuming this  <br>
happens we have that for some $a$ (we use $a = 2$ in implementation for simplicity) <br>
$a^{n!} = (a^{p - 1})^{k} = 1 \pmod p$. Therefore since $p \mid a^{n!} - 1$ and $p \mid N$, then finding $\gcd(a^{n!} - 1, N)$ <br>
could lead us to find $p$, although this might not always work because maybe $n$ is too large <br>
to find and compute and also that maybe $q$ also divide $a^{n!}$. Note that we can do all the <br>
calculations modulo $N$, since we are looking for these answers modulo $p$ but since we are <br>
already looking for $p$, we can use $N = pq$.

## 2. Pollard's rho algorithm
In this method, first we use a simple polynomial $g(x) = x^2 + 5$ (could use any other). <br>
Now starting with some $x$ (we used $x = 2$), we can generate the sequence $x, g(x), g(g(x)), \dots$. <br>
If we consider this sequnce modulo $N$, then it is obvious that that this sequence forms a <br>
loop at some point. This is also true if look at the sequence modulo $p$. Indeed when we find <br>
two elements in the sequence that are the same modulo $p$ ($x_i, x_j$), then their difference <br>
divides $p$, this also means that $d = (x_i - x_j, n) \ne 1$. Now $d$ is either equal to $p$ or $q$, <br>
or $d = N$, which shows that the test is failed. (Although this is highly unlikely and we can <br> 
run the test again, with different initial parameters). <br>
To find the loop, we use the tortoise and hare algorithm, using two pointers, one going one <br>
step at a time and the other two step at a time, if there is loop (which we know there is), <br>
at some point these two pointers will again meet each other.



## the code
In our code we first generate two 32 bit prime numbers, and then use the two methods above,<br>
to try to find the factorization. The second method is much more faster and reliable.


## analysis
Using only 32-bit prime numbers, Pollard's $p - 1$ method dones't respond really well and can't<br>
find the factorization, where Pollard's rho method can easily solve then in less than a second. <br>
The final score for 32-bit primes was:
- Pollard's p - 1 algorithm: 12 out of 50
- Pollard's rho algorithm: 50 out of 50

We also ran the Pollard's rho algorithm for 50-bit primes: <br>
the result still was:
- Pollard's rho algorithm: 10 out of 10

But slower than the previous one, (~30 second on each test)

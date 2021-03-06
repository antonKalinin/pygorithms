def get_primes(n):
    """ Returns a list of primes < n """
    sieve = [True] * (n//2)
    for i in range(3, int(n**0.5)+1, 2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [2*i+1 for i in range(1, n//2) if sieve[i]]


# k is quantity of prime numbers
# n is size of matrix
k, n = [int(j) for j in input('>').split()]
primes = get_primes(10**7)

if k > n**2 or k > len(primes):
    print(-1)
else:
    if k > n:
        pass
    else:
        pass
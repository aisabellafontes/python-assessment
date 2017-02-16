import math
import sys

def primes_sieves_atkin(nmin, nmax):
    """
    Returns a list of prime numbers between nmin and nmax
    """
    is_prime = dict([(i, False) for i in range(5, nmax+1)])

    for x in range(1, int(math.sqrt(nmax))+1):
        for y in range(1, int(math.sqrt(nmax))+1):
            n = 4*x**2 + y**2
            if (n <= nmax) and ((n % 12 == 1) or (n % 12 == 5)):
                is_prime[n] = not is_prime[n]
            n = 3*x**2 + y**2
            if (n <= nmax) and (n % 12 == 7):
                is_prime[n] = not is_prime[n]
            n = 3*x**2 - y**2
            if (x > y) and (n <= nmax) and (n % 12 == 11):
                is_prime[n] = not is_prime[n]

    for n in range(5, int(math.sqrt(nmax))+1):
        if is_prime[n]:
            ik = 1
            while (ik * n**2 <= nmax):
                is_prime[ik * n**2] = False
                ik += 1
    primes = []
    for i in range(nmin, nmax + 1):
        if i in [0, 1, 4]: pass
        elif i in [2,3] or is_prime[i]: primes.append(i)
        else: pass
    return primes

def main():
    count_intervals = int(sys.stdin.readline())
    #print type(count_intervals)
    while count_intervals > 0:
        numbers = sys.stdin.readline()
        n, m = numbers.split()
        interval = primes_sieves_atkin(int(n), int(m))
        for i in interval:
            print i
        print '\n'
        count_intervals -= 1

if __name__ == '__main__':
    main()
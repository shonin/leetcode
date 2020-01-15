class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        primes = [True] * n
        count = 0
        primes[0], primes[1] = False, False

        for i in range(n):
            # if number already marked false, skip
            if not primes[i]:
                continue

            # hasn't been marked false, so it is prime
            count += 1

            # mark all of its multiples false, starting at i**2, incrementing by i
            for j in range(i**2, n, i):
                primes[j] = False

        return count

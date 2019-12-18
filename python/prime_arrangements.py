"""
Problem:
Return the number of permutations of 1 to n so that prime numbers are at prime
indices (1-indexed.)

(Recall that an integer is prime if and only if it is greater than 1, and cannot
be written as a product of two positive integers both smaller than it.)

Since the answer may be large, return the answer modulo 10^9 + 7.

Solution:
Implements the Sieve of Eratosthenes to count how many primes are below and
including the given number `n`. Then does some basic math to determine the
number of possible permutations without actually having to implement said
permutations. 
"""

class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        num_primes = self.count_primes_to(n)
        non_primes = n - num_primes

        return (math.factorial(num_primes) * math.factorial(non_primes)) % (10**9+7)


    def count_primes_to(self, n):
        n += 1 # add 1 to account for 0 indexed array
        primes = [True] * n
        primes[0] = primes[1] = False
        count = 0

        for i in range(n):
            if not primes[i]:
                continue

            count += 1

            for j in range(i**2, n, i):
                primes[j] = False

        return count

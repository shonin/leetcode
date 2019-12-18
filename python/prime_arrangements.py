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
import math

class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        num_primes = self.count_primes_to(n)
        non_primes = n - num_primes

        # counting possible permutations utilizes factorials, typically written
        # like 4!, meaning 4*3*2*1.
        # e.g. the number of possible permutations for 25 primes and
        # 75 non-primes would be 25! * 75!

        return (math.factorial(num_primes) * math.factorial(non_primes)) % (10**9+7)


    def count_primes_to(self, n):
        n += 1 # add 1 to account for 0 indexed array
        primes = [True] * n # creates an array of n length with all True values
        primes[0] = primes[1] = False # 0 and 1 are not prime
        count = 0

        for i in range(n):
            # if encountering a number already marked as not prime, skip
            if not primes[i]:
                continue

            # if this code runs, i is prime
            count += 1

            # mark all multiples of i as not prime, starting at i^2
            # any non-prime between i and i^2 has already been marked
            # as non-prime according to math
            for j in range(i**2, n, i):
                primes[j] = False

        return count

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        primes = [True] * (right + 1)
        primes[0] = primes[1] = False

        for i in range(2, int(right ** 0.5) + 1):
            if primes[i]:
                for j in range(i * i, right + 1, i):
                    primes[j] = False
        
        primes_in_range = [i for i in range(left, right + 1) if primes[i]]

        if len(primes_in_range) < 2:
            return [-1, -1]
        
        min_diff = 9999999
        for i in range(1, len(primes_in_range)):
            diff = primes_in_range[i] - primes_in_range[i - 1]
            if diff < min_diff:
                min_diff = diff
                closest_pair = [primes_in_range[i - 1], primes_in_range[i]]
        
        return closest_pair
        
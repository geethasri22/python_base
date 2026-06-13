class Solution:
    def computeValue(self, n):
        MOD = 10**9 + 7
        
        # Precompute factorials up to 2n
        fact = [1] * (2*n + 1)
        for i in range(1, 2*n + 1):
            fact[i] = (fact[i-1] * i) % MOD
        
        # Modular inverse using Fermat's Little Theorem
        def modinv(x):
            return pow(x, MOD-2, MOD)
        
        # nCr function
        def nCr(n, r):
            if r < 0 or r > n:
                return 0
            return (fact[n] * modinv(fact[r]) % MOD * modinv(fact[n-r])) % MOD
        
        # Answer is C(2n, n)
        return nCr(2*n, n)

class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        return sum(bin(i).count('1') in [2, 3, 5, 7, 11, 13, 17, 19] for i in range(L, R+1))
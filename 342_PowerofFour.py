class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return math.log(n, 1/4) % 1 == 0 if n > 0 else False
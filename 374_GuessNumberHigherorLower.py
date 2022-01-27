class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n

        while True:
            middle_num = int((left + right) / 2)
            if guess(middle_num) == 1:
                left = middle_num + 1
            elif guess(middle_num) == -1:
                right = middle_num - 1
            else:
                return middle_num


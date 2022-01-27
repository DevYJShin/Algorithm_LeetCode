class Solution(object):
    def triangleNumber(self, nums):

        nums, count, n = sorted(nums, reverse=1), 0, len(nums)
        for i in range(n):
            j, k = i + 1, n - 1
            while j < k:
                if nums[j] + nums[k] > nums[i]:
                    count += k - j
                    j += 1
                else:
                    k -= 1
        return count
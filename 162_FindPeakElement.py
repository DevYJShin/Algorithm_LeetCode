class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
				# left가 커지고 right가 작아지는 경우 left와 right가 같아질 수 있다.
        # 그 때 원한느 값을 찾은 경우이므로 left와 right가 같아지면 반복문 종료
        while left < right:
            mid = (left + right) // 2      # 가운데 지점
            if nums[mid] < nums[mid+1]:    # 현재 값이 오른쪽 값보다 작다면
                left = mid+1
            else:                          # 현재 값이 오른쪽 값보다 크다면
                right = mid
        return left                        # 반복문이 종료되면 left가 정답
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        res = nums[0]
        temp_sum = 0

        for n in nums:
            # 이전 값이 음수인 경우 0 으로 초기화
            if temp_sum < 0:
                temp_sum = 0
            temp_sum += n
            
            #전체가 음수인 경우 더 큰 값 res 저장
            res = max(res, temp_sum)

        return res
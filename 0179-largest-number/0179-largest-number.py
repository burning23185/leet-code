class Solution:
    
    def largestNumber(self, nums: List[int]) -> str:

        for i in range(0, len(nums)):
            for j in range(i, len(nums)):
                str_i = str(nums[i])
                str_j = str(nums[j])

                if str_i + str_j < str_j + str_i:
                    nums[i], nums[j] = nums[j], nums[i]
                    continue
                
        return str(int(''.join(map(str,nums))))
    
s = Solution()
print(s.largestNumber([10,2,9,39,17]))
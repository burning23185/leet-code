class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left_idx = 0
        right_idx = len(numbers) - 1
        
        while left_idx < right_idx:
            res = numbers[left_idx] + numbers[right_idx]

            if res == target:
                return [left_idx+1, right_idx+1]
            
            if res < target:
                left_idx += 1
                continue
            
            right_idx -= 1
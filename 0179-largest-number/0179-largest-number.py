class Solution:
    import sys

class Solution:
    def _merge(self, arr1, arr2):
        result = []
        i = j = 0

        while i < len(arr1) and j < len(arr2):
            str_i = str(arr1[i])
            str_j = str(arr2[j])

            if str_i + str_j > str_j + str_i:
                result.append(arr1[i])
                i += 1
            else:
                result.append(arr2[j])
                j += 1

        while i < len(arr1):
            result.append(arr1[i])
            i += 1

        while j < len(arr2):
            result.append(arr2[j])
            j += 1

        return result
    
    def mergeSort(self, arr):
        if len(arr) <= 1:
            return arr
        
        pivot = len(arr)//2

        L = arr[:pivot]
        R = arr[pivot:]

        return self._merge(self.mergeSort(L), self.mergeSort(R))


    def largestNumber(self, nums: List[int]) -> str:
        sorted = self.mergeSort(nums)
        return '0' if sum(nums) == 0 else ''.join(str(n) for n in sorted)
'''

class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:    
        def binary_search(nums, target, is_searching_left):
            left = 0
            right = len(nums) - 1
            idx = -1
            
            while left <= right:
                mid = (left + right) // 2
                
                if nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    idx = mid
                    if is_searching_left:
                        right = mid - 1
                    else:
                        left = mid + 1
            
            return idx
        
        left = binary_search(nums, target, True)
        right = binary_search(nums, target, False)
        
        return [left, right]
'''
class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        left = 0
        right = len(nums) - 1
        while left < len(nums):
            if nums[left] == target:
                break
            left += 1
            
        while right >= 0:
            if nums[right] == target:
                break
            right -= 1
        if left == len(nums) or right < 0:
            return [-1,-1]
        else:
            return [left,right]
        
x = Solution()
print(x.searchRange([5,7,7,8,8,10],8))
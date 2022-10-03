#Time_Complexity: O(log n)
#Space_Complexity: O(1)
 
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        left, right = 0, n - 1
        if n == 0: return -1
        
        while left <= right:
            mid = left + (right - left) // 2 #find the mid
            if nums[mid] == target: return mid 
            #either one side of the array is increasing
            # Pivot point left side is strictly increasing
            if nums[mid] >= nums[left]: 
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
                    
            # Pivot point right side is strictly increasing
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1 
                    
            
#TC: log(log mn)  
#SC: O(1)

class Solution:
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        M = len(matrix)         # m will be Row size
        N = len(matrix[0])      # N will be column size
        
        left = 0                 #make the low pointer 
        right = (M * N) - 1      # the right pointer points to the last element of the matrix which is (M*N)-1
        
        while left <= right:
            mid = left + (right - left) // 2    #find the mid pointer index
            mid_element = matrix[mid // N][mid % N]   #now find the mid value
            
            if mid_element < target:  #if mid element is lesser than the target, left will be mid index + 1
                left = mid + 1
            elif mid_element > target: #if mid element is greater than the target, right  will be mid index - 1
                right = mid - 1
            else:
                return True #else return true
        
        return False #if nothing turns true, then the element is not present and return False
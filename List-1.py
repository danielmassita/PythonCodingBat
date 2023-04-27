"""
List-1 chance
Basic python list problems -- no loops.. Use a[0], a[1], ... to access elements in a list, len(a) is the length.

 first_last6 H    	 same_first_last H      	 make_pi
 common_end	         sum3                   	 rotate_left3
 reverse3	           max_end3                	 sum2
 middle_way	         make_ends              	 has23
 """

"""
List-1 > first_last6
prev  |  next  |  chance
Given an array of ints, return True if 6 appears as either the first or last element in the array. The array will be length 1 or more.


first_last6([1, 2, 6]) → True
first_last6([6, 1, 2, 3]) → True
first_last6([13, 6, 1, 2, 3]) → False

Hint:
The first element is nums[0] and the last element is nums[len(nums) - 1]. Check if either of those is == 6.
"""
def first_last6(nums):
  if nums[0] == 6 or nums[-1] == 6:
    return True
  else:
    return False

def first_last6(nums):
  return (nums[0] == 6) or (nums[-1] == 6)
  
"""
Expected	Run		
first_last6([1, 2, 6]) → True	True	OK	
first_last6([6, 1, 2, 3]) → True	True	OK	
first_last6([13, 6, 1, 2, 3]) → False	False	OK	
first_last6([13, 6, 1, 2, 6]) → True	True	OK	
first_last6([3, 2, 1]) → False	False	OK	
first_last6([3, 6, 1]) → False	False	OK	
first_last6([3, 6]) → True	True	OK	
first_last6([6]) → True	True	OK	
first_last6([3]) → False	False	OK	
first_last6([5, 6]) → True	True	OK	
first_last6([5, 5]) → False	False	OK	
first_last6([1, 2, 3, 4, 6]) → True	True	OK	
first_last6([1, 2, 3, 4]) → False	False	OK	
other tests
OK	

All Correct
"""

"""
List-1 > same_first_last
prev  |  next  |  chance
Given an array of ints, return True if the array is length 1 or more, and the first element and the last element are equal.


same_first_last([1, 2, 3]) → False
same_first_last([1, 2, 3, 1]) → True
same_first_last([1, 2, 1]) → True

Hint:
The length is nums.length, the first element is nums[0] and the last element is nums[nums.length - 1]
"""

def same_first_last(nums):
 if (len(nums) >= 1) and (nums[0] == nums[-1]):
  return True
 else:
  return False

def same_first_last(nums):
  tamanho = len(nums)
  return tamanho >= 1 and (nums[0] == nums[-1])

def same_first_last(nums):
  return (len(nums) >= 1 and nums[0] == nums[-1])
 
"""
Expected	Run		
same_first_last([1, 2, 3]) → False	False	OK	
same_first_last([1, 2, 3, 1]) → True	True	OK	
same_first_last([1, 2, 1]) → True	True	OK	
same_first_last([7]) → True	True	OK	
same_first_last([]) → False	False	OK	
same_first_last([1, 2, 3, 4, 5, 1]) → True	True	OK	
same_first_last([1, 2, 3, 4, 5, 13]) → False	False	OK	
same_first_last([13, 2, 3, 4, 5, 13]) → True	True	OK	
same_first_last([7, 7]) → True	True	OK	
other tests
OK	

All Correct
"""
  
  
  
  
  
  
  
  
  
  

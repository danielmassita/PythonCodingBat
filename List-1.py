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
  

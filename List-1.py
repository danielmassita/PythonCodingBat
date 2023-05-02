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
  
"""
List-1 > make_pi
prev  |  next  |  chance
Return an int array length 3 containing the first 3 digits of pi, {3, 1, 4}.


make_pi() → [3, 1, 4]
"""

def make_pi():
 pi = [3, 1, 4]
 return pi

"""
Expected	Run		
make_pi() → [3, 1, 4]	[3, 1, 4]	OK	

All Correct
"""
  
"""
List-1 > common_end
prev  |  next  |  chance
Given 2 arrays of ints, a and b, return True if they have the same first element or they have the same last element. Both arrays will be length 1 or more.


common_end([1, 2, 3], [7, 3]) → True
common_end([1, 2, 3], [7, 3, 2]) → False
common_end([1, 2, 3], [1, 3]) → True
"""

def common_end(a, b):
 return (a[0] == b[0]) or (a[-1] == b[-1])
  
def common_end(a, b):
  if a[0] == b[0] or a[-1] == b[-1]:
    return True
  else:
    return False

"""
  Expected	Run		
common_end([1, 2, 3], [7, 3]) → True	True	OK	
common_end([1, 2, 3], [7, 3, 2]) → False	False	OK	
common_end([1, 2, 3], [1, 3]) → True	True	OK	
common_end([1, 2, 3], [1]) → True	True	OK	
common_end([1, 2, 3], [2]) → False	False	OK	
other tests
OK	

All Correct
"""  

"""
List-1 > sum3
prev  |  next  |  chance
Given an array of ints length 3, return the sum of all the elements.


sum3([1, 2, 3]) → 6
sum3([5, 11, 2]) → 18
sum3([7, 0, 0]) → 7
"""

def sum3(nums):
 return nums[0] + nums[1] + nums[2]

"""
Expected	Run		
sum3([1, 2, 3]) → 6	6	OK	
sum3([5, 11, 2]) → 18	18	OK	
sum3([7, 0, 0]) → 7	7	OK	
sum3([1, 2, 1]) → 4	4	OK	
sum3([1, 1, 1]) → 3	3	OK	
sum3([2, 7, 2]) → 11	11	OK	

All Correct
"""

"""
List-1 > rotate_left3
prev  |  next  |  chance
Given an array of ints length 3, return an array with the elements "rotated left" so {1, 2, 3} yields {2, 3, 1}.


rotate_left3([1, 2, 3]) → [2, 3, 1]
rotate_left3([5, 11, 9]) → [11, 9, 5]
rotate_left3([7, 0, 0]) → [0, 0, 7]
"""

def rotate_left3(nums):
 nums.append(nums[0])
 return nums[1:4]

"""
Expected	Run		
rotate_left3([1, 2, 3]) → [2, 3, 1]	[2, 3, 1]	OK	
rotate_left3([5, 11, 9]) → [11, 9, 5]	[11, 9, 5]	OK	
rotate_left3([7, 0, 0]) → [0, 0, 7]	[0, 0, 7]	OK	
rotate_left3([1, 2, 1]) → [2, 1, 1]	[2, 1, 1]	OK	
rotate_left3([0, 0, 1]) → [0, 1, 0]	[0, 1, 0]	OK	
other tests
OK	

All Correct
"""

# ACHO QUE VOU VOMITAR!

"""
List-1 > reverse3
prev  |  next  |  chance
Given an array of ints length 3, return a new array with the elements in reverse order, so {1, 2, 3} becomes {3, 2, 1}.


reverse3([1, 2, 3]) → [3, 2, 1]
reverse3([5, 11, 9]) → [9, 11, 5]
reverse3([7, 0, 0]) → [0, 0, 7]
"""

def reverse3(nums):
 nums.append(nums[2])
 nums.append(nums[1])
 nums.append(nums[0])
 return nums[3:6]

def reverse3(nums):
#  nums[0:3]
  nums.append(nums[2])
  nums.append(nums[1])
  nums.append(nums[0])
  return nums[3:6]


"""
Expected	Run		
reverse3([1, 2, 3]) → [3, 2, 1]	[3, 2, 1]	OK	
reverse3([5, 11, 9]) → [9, 11, 5]	[9, 11, 5]	OK	
reverse3([7, 0, 0]) → [0, 0, 7]	[0, 0, 7]	OK	
reverse3([2, 1, 2]) → [2, 1, 2]	[2, 1, 2]	OK	
reverse3([1, 2, 1]) → [1, 2, 1]	[1, 2, 1]	OK	
reverse3([2, 11, 3]) → [3, 11, 2]	[3, 11, 2]	OK	
reverse3([0, 6, 5]) → [5, 6, 0]	[5, 6, 0]	OK	
reverse3([7, 2, 3]) → [3, 2, 7]	[3, 2, 7]	OK	
other tests
OK	

All Correct
"""

"""
List-1 > max_end3
prev  |  next  |  chance
Given an array of ints length 3, figure out which is larger, the first or last element in the array, and set all the other elements to be that value. Return the changed array.


max_end3([1, 2, 3]) → [3, 3, 3]
max_end3([11, 5, 9]) → [11, 11, 11]
max_end3([2, 11, 3]) → [3, 3, 3]
"""  
  
def max_end3(nums):
  if nums[0] == nums[2]:
    nums.append(nums[0])
    nums.append(nums[0])
    nums.append(nums[0])
    return nums[3:6]    
  elif nums[0] > nums[2]:
    nums.append(nums[0])
    nums.append(nums[0])
    nums.append(nums[0])
    return nums[3:6]
  elif nums[2] > nums[0]:
    nums.append(nums[2])
    nums.append(nums[2])
    nums.append(nums[2])
    return nums[3:6]

# Our Solution: 

def max_end3(nums):
  big = max(nums[0], nums[2])
  nums[0] = big
  nums[1] = big
  nums[2] = big
  return nums

"""
Expected	Run		
max_end3([1, 2, 3]) → [3, 3, 3]	[3, 3, 3]	OK	
max_end3([11, 5, 9]) → [11, 11, 11]	[11, 11, 11]	OK	
max_end3([2, 11, 3]) → [3, 3, 3]	[3, 3, 3]	OK	
max_end3([11, 3, 3]) → [11, 11, 11]	[11, 11, 11]	OK	
max_end3([3, 11, 11]) → [11, 11, 11]	[11, 11, 11]	OK	
max_end3([2, 2, 2]) → [2, 2, 2]	[2, 2, 2]	OK	
max_end3([2, 11, 2]) → [2, 2, 2]	[2, 2, 2]	OK	
max_end3([0, 0, 1]) → [1, 1, 1]	[1, 1, 1]	OK	
other tests
OK	

All Correct
"""

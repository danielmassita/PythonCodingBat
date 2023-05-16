"""
List-2 chance
Medium python list problems -- 1 loop.. Use a[0], a[1], ... to access elements in a list, len(a) is the length.

  count_evens H     big_diff    centered_average
  sum13             sum67       has22
"""
"""
List-2 > count_evens
prev  |  next  |  chance
Return the number of even ints in the given array. Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.


count_evens([2, 1, 2, 3, 4]) → 3
count_evens([2, 2, 0]) → 3
count_evens([1, 3, 5]) → 0
Hint:
In Python, "for num in nums:" will loop through all the values in the list. Loop through all the values, and count how many times the value is even.
"""
# Da amiga Gio...
def count_evens(nums):
  count = 0
  for i in range(len(nums)):
    if nums[i] % 2 == 0:
      count += 1
  return count

# Our Solution:
def count_evens(nums):
  count = 0
  for num in nums:
    if num % 2 == 0:
      count = count + 1
  return count
"""
Expected	Run		
count_evens([2, 1, 2, 3, 4]) → 3	3	OK	
count_evens([2, 2, 0]) → 3	3	OK	
count_evens([1, 3, 5]) → 0	0	OK	
count_evens([]) → 0	0	OK	
count_evens([11, 9, 0, 1]) → 1	1	OK	
count_evens([2, 11, 9, 0]) → 2	2	OK	
count_evens([2]) → 1	1	OK	
count_evens([2, 5, 12]) → 2	2	OK	
other tests
OK	

All Correct
"""



"""

"""

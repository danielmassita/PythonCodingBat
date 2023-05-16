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
List-2 > big_diff
prev  |  next  |  chance
Given an array length 1 or more of ints, return the difference between the largest and smallest values in the array. Note: the built-in min(v1, v2) and max(v1, v2) functions return the smaller or larger of two values.


big_diff([10, 3, 5, 6]) → 7
big_diff([7, 2, 10, 9]) → 8
big_diff([2, 10, 7, 2]) → 8
"""
# Da amiga Gio...
def big_diff(nums):
  return max(nums) - min(nums)
"""
Expected	Run		
big_diff([10, 3, 5, 6]) → 7	7	OK	
big_diff([7, 2, 10, 9]) → 8	8	OK	
big_diff([2, 10, 7, 2]) → 8	8	OK	
big_diff([2, 10]) → 8	8	OK	
big_diff([10, 2]) → 8	8	OK	
big_diff([10, 0]) → 10	10	OK	
big_diff([2, 3]) → 1	1	OK	
big_diff([2, 2]) → 0	0	OK	
big_diff([2]) → 0	0	OK	
big_diff([5, 1, 6, 1, 9, 9]) → 8	8	OK	
big_diff([7, 6, 8, 5]) → 3	3	OK	
big_diff([7, 7, 6, 8, 5, 5, 6]) → 3	3	OK	
other tests
OK	

All Correct
"""



"""
List-2 > centered_average
prev  |  next  |  chance
Return the "centered" average of an array of ints, which we'll say is the mean average of the values, except ignoring the largest and smallest values in the array. If there are multiple copies of the smallest value, ignore just one copy, and likewise for the largest value. Use int division to produce the final average. You may assume that the array is length 3 or more.


centered_average([1, 2, 3, 4, 100]) → 3
centered_average([1, 1, 5, 5, 10, 8, 7]) → 5
centered_average([-10, -4, -2, -4, -2, 0]) → -3
"""
# Da amiga Vesper...
def centered_average(nums):
  # Encontre o menor e o maior valor na lista
  menor = min(nums)
  maior = max(nums)
  # Remova uma ocorrência do menor valor e do maior valor
  nums.remove(menor)
  nums.remove(maior)
  # Calcule a média dos valores restantes
  media = sum(nums) // len(nums)
  # Retorne o valor arredondado
  return media

# Da amiga Gio...
def centered_average(nums):
  nums.sort()
  count = 0
  total = 0
  for i in range(1, len(nums)-1 ):
    count += 1
    total += nums[i]
  return total / count
"""
Expected	Run		
centered_average([1, 2, 3, 4, 100]) → 3	3	OK	
centered_average([1, 1, 5, 5, 10, 8, 7]) → 5	5	OK	
centered_average([-10, -4, -2, -4, -2, 0]) → -3	-3	OK	
centered_average([5, 3, 4, 6, 2]) → 4	4	OK	
centered_average([5, 3, 4, 0, 100]) → 4	4	OK	
centered_average([100, 0, 5, 3, 4]) → 4	4	OK	
centered_average([4, 0, 100]) → 4	4	OK	
centered_average([0, 2, 3, 4, 100]) → 3	3	OK	
centered_average([1, 1, 100]) → 1	1	OK	
centered_average([7, 7, 7]) → 7	7	OK	
centered_average([1, 7, 8]) → 7	7	OK	
centered_average([1, 1, 99, 99]) → 50	50	OK	
centered_average([1000, 0, 1, 99]) → 50	50	OK	
centered_average([4, 4, 4, 4, 5]) → 4	4	OK	
centered_average([4, 4, 4, 1, 5]) → 4	4	OK	
centered_average([6, 4, 8, 12, 3]) → 6	6	OK	
other tests
OK	

All Correct
"""



"""
List-2 > sum13
prev  |  next  |  chance
Return the sum of the numbers in the array, returning 0 for an empty array. Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.


sum13([1, 2, 2, 1]) → 6
sum13([1, 1]) → 2
sum13([1, 2, 2, 1, 13]) → 6
"""
# Da amiga Vesper...
def sum13(nums):
    soma = 0
    i = 0
    while i < len(nums):
        if nums[i] == 13:
            i += 2  # Pula o número 13 e o próximo número
            continue
        soma += nums[i]
        i += 1
    return soma
  
# Da amiga Gio...def sum13(nums):
  total = 0
  skip = False
  if len(nums) == 0:
    return 0
  else:
    for i in range(len(nums)):
      if nums[i] == 13:
        skip = True
      elif skip:
        skip = False
      else:
        total += nums[i]
  return total
"""
Expected	Run		
sum13([1, 2, 2, 1]) → 6	6	OK	
sum13([1, 1]) → 2	2	OK	
sum13([1, 2, 2, 1, 13]) → 6	6	OK	
sum13([1, 2, 13, 2, 1, 13]) → 4	4	OK	
sum13([13, 1, 2, 13, 2, 1, 13]) → 3	3	OK	
sum13([]) → 0	0	OK	
sum13([13]) → 0	0	OK	
sum13([13, 13]) → 0	0	OK	
sum13([13, 0, 13]) → 0	0	OK	
sum13([13, 1, 13]) → 0	0	OK	
sum13([5, 7, 2]) → 14	14	OK	
sum13([5, 13, 2]) → 5	5	OK	
sum13([0]) → 0	0	OK	
sum13([13, 0]) → 0	0	OK	
other tests
OK	

All Correct
"""

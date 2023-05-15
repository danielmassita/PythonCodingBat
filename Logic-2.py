"""
Logic-2 chance
Medium boolean logic puzzles -- if else and or not

 make_bricks	 lone_sum	 lucky_sum
 no_teen_sum	 round_sum	 close_far
 make_chocolate
"""

"""
Logic-2 > make_bricks
prev  |  next  |  chance
We want to make a row of bricks that is goal inches long. We have a number of small bricks (1 inch each) and big bricks (5 inches each). Return True if it is possible to make the goal by choosing from the given bricks. This is a little harder than it looks and can be done without any loops. See also: Introduction to MakeBricks


make_bricks(3, 1, 8) → True
make_bricks(3, 1, 9) → False
make_bricks(3, 2, 10) → True
"""

# TÁ MUITO DIFÍCIL... :( 

# Da amiga Giovanna
def make_bricks(small, big, goal):
 big_needed = min(big, goal // 5)
 return goal - (big_needed * 5) <= small

# Da amiga Vesper
def make_bricks(small, big, goal):
    # Calculate the maximum number of inches we can cover with the given big bricks
    max_big_inches = big * 5

    # If the goal is greater than the maximum inches we can cover with big bricks,
    # we need to subtract that maximum from the goal
    if goal > max_big_inches:
        goal -= max_big_inches
    else:
        # Otherwise, we don't need to use any big bricks, so set the goal to itself
        goal %= 5

    # Check if the remaining goal can be covered by the available small bricks
    return goal <= small

"""
Expected	Run		
make_bricks(3, 1, 8) → True	True	OK	
make_bricks(3, 1, 9) → False	False	OK	
make_bricks(3, 2, 10) → True	True	OK	
make_bricks(3, 2, 8) → True	True	OK	
make_bricks(3, 2, 9) → False	False	OK	
make_bricks(6, 1, 11) → True	True	OK	
make_bricks(6, 0, 11) → False	False	OK	
make_bricks(1, 4, 11) → True	True	OK	
make_bricks(0, 3, 10) → True	True	OK	
make_bricks(1, 4, 12) → False	False	OK	
make_bricks(3, 1, 7) → True	True	OK	
make_bricks(1, 1, 7) → False	False	OK	
make_bricks(2, 1, 7) → True	True	OK	
make_bricks(7, 1, 11) → True	True	OK	
make_bricks(7, 1, 8) → True	True	OK	
make_bricks(7, 1, 13) → False	False	OK	
make_bricks(43, 1, 46) → True	True	OK	
make_bricks(40, 1, 46) → False	False	OK	
make_bricks(40, 2, 47) → True	True	OK	
make_bricks(40, 2, 50) → True	True	OK	
make_bricks(40, 2, 52) → False	False	OK	
make_bricks(22, 2, 33) → False	False	OK	
make_bricks(0, 2, 10) → True	True	OK	
make_bricks(1000000, 1000, 1000100) → True	True	OK	
make_bricks(2, 1000000, 100003) → False	False	OK	
make_bricks(20, 0, 19) → True	True	OK	
make_bricks(20, 0, 21) → False	False	OK	
make_bricks(20, 4, 51) → False	False	OK	
make_bricks(20, 4, 39) → True	True	OK	
other tests
OK	

All Correct
"""



"""
Logic-2 > lone_sum
prev  |  next  |  chance
Given 3 int values, a b c, return their sum. However, if one of the values is the same as another of the values, it does not count towards the sum.


lone_sum(1, 2, 3) → 6
lone_sum(3, 2, 3) → 2
lone_sum(3, 3, 3) → 0
"""
# Da amiga Gio...
def lone_sum(a, b, c):
 sum = 0
 if a not in [b, c]:
  sum += a
 if b not in [a, c]:
  sum += b
 if c not in [a, b]:
  sum += c
 return sum

# Our Solution:

def lone_sum(a, b, c):
  sum = 0
  if a != b and a != c: sum += a
  if b != a and b != c: sum += b
  if c != a and c != b: sum += c 
  return sum
 
"""
Expected	Run		
lone_sum(1, 2, 3) → 6	6	OK	
lone_sum(3, 2, 3) → 2	2	OK	
lone_sum(3, 3, 3) → 0	0	OK	
lone_sum(9, 2, 2) → 9	9	OK	
lone_sum(2, 2, 9) → 9	9	OK	
lone_sum(2, 9, 2) → 9	9	OK	
lone_sum(2, 9, 3) → 14	14	OK	
lone_sum(4, 2, 3) → 9	9	OK	
lone_sum(1, 3, 1) → 3	3	OK	
other tests
OK	

All Correct
"""



"""
Logic-2 > lucky_sum
prev  |  next  |  chance
Given 3 int values, a b c, return their sum. However, if one of the values is 13 then it does not count towards the sum and values to its right do not count. So for example, if b is 13, then both b and c do not count.


lucky_sum(1, 2, 3) → 6
lucky_sum(1, 2, 13) → 3
lucky_sum(1, 13, 3) → 1
"""
# Da amiga Vesper...
def lucky_sum(a, b, c):
 if a == 13:
  return 0
 if b == 13:
  return a
 if c == 13:
  return a + b
 else:
  return a + b + c
 
# Da amiga Gio...def lucky_sum(a, b, c):
  sum = 0
  for n in (a, b, c):
    if n != 13:
      sum += n
    else:
      break
  return sum
"""
Expected	Run		
lucky_sum(1, 2, 3) → 6	6	OK	
lucky_sum(1, 2, 13) → 3	3	OK	
lucky_sum(1, 13, 3) → 1	1	OK	
lucky_sum(1, 13, 13) → 1	1	OK	
lucky_sum(6, 5, 2) → 13	13	OK	
lucky_sum(13, 2, 3) → 0	0	OK	
lucky_sum(13, 2, 13) → 0	0	OK	
lucky_sum(13, 13, 2) → 0	0	OK	
lucky_sum(9, 4, 13) → 13	13	OK	
lucky_sum(8, 13, 2) → 8	8	OK	
lucky_sum(7, 2, 1) → 10	10	OK	
lucky_sum(3, 3, 13) → 6	6	OK	
other tests
OK	

All Correct
"""

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


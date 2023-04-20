"""Warmup-1 > sleep_in
prev  |  next  |  chance
The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation. We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.


sleep_in(False, False) → True
sleep_in(True, False) → False
sleep_in(False, True) → True"""

def sleep_in(weekday, vacation):
    if (not weekday or vacation):
        return True
    else:
        return False

def sleep_in(weekday, vacation):
  if (weekday == False and vacation == False):
    return True
  elif (weekday == True and vacation == False):
    return False
  elif (weekday == False and vacation == True):
    return True
  else:
    return True

def sleep_in(weekday, vacation):
    return (not weekday or vacation)

"""Expected	Run		
sleep_in(False, False) → True	True	OK	
sleep_in(True, False) → False	False	OK	
sleep_in(False, True) → True	True	OK	
sleep_in(True, True) → True	True	OK	

All Correct"""

"""Warmup-1 > monkey_trouble
prev  |  next  |  chance
We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling. We are in trouble if they are both smiling or if neither of them is smiling. Return True if we are in trouble.


monkey_trouble(True, True) → True
monkey_trouble(False, False) → True
monkey_trouble(True, False) → False"""

def monkey_trouble(a_smile, b_smile):
  if (a_smile == True and b_smile == True):
    return True
  elif (a_smile == False and b_smile == False):
    return True
  elif (a_smile == True and b_smile == False):
    return False
  elif (a_smile == False and b_smile == True):
    return False
  
def monkey_trouble(a_smile, b_smile):
    if (a_smile and b_smile):
        return True
    elif (not a_smile and not b_smile):
        return True
    else:
        return False

def monkey_trouble(a_smile, b_smile):
  if a_smile and b_smile:
    return True
  if not a_smile and not b_smile:
    return True
  return False

def monkey_trouble(a_smile, b_smile):
    return ((a_smile and b_smile) or (not a_smile and not b_smile))

def monkey_trouble(a_smile, b_smile):
    return (a_smile == b_smile)

"""Expected	Run		
monkey_trouble(True, True) → True	True	OK	
monkey_trouble(False, False) → True	True	OK	
monkey_trouble(True, False) → False	False	OK	
monkey_trouble(False, True) → False	False	OK	

All Correct"""

"""Warmup-1 > sum_double
prev  |  next  |  chance
Given two int values, return their sum. Unless the two values are the same, then return double their sum.


sum_double(1, 2) → 3
sum_double(3, 2) → 5
sum_double(2, 2) → 8"""

def sum_double(a, b):
    if (a == b):
        return (a+b)*2
    else:
        return (a+b)

def sum_double(a, b):
    sum = a + b
    if a == b:
        sum = sum*2
    return sum

"""Expected	Run		
sum_double(1, 2) → 3	3	OK	
sum_double(3, 2) → 5	5	OK	
sum_double(2, 2) → 8	8	OK	
sum_double(-1, 0) → -1	-1	OK	
sum_double(3, 3) → 12	12	OK	
sum_double(0, 0) → 0	0	OK	
sum_double(0, 1) → 1	1	OK	
sum_double(3, 4) → 7	7	OK	

All Correct"""

"""Warmup-1 > diff21
prev  |  next  |  chance
Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.


diff21(19) → 2
diff21(10) → 11
diff21(21) → 0"""

def diff21(n):
    if (n > 21):
        return 2 * abs(n - 21)
    else:
        return abs(n - 21)

def diff21(n):
  if n <= 21:
    return 21 - n
  else:
    return (n - 21) * 2

"""Expected	Run		
diff21(19) → 2	2	OK	
diff21(10) → 11	11	OK	
diff21(21) → 0	0	OK	
diff21(22) → 2	2	OK	
diff21(25) → 8	8	OK	
diff21(30) → 18	18	OK	
diff21(0) → 21	21	OK	
diff21(1) → 20	20	OK	
diff21(2) → 19	19	OK	
diff21(-1) → 22	22	OK	
diff21(-2) → 23	23	OK	
diff21(50) → 58	58	OK	

All Correct"""


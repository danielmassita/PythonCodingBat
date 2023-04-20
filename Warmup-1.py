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

"""Warmup-1 > parrot_trouble
prev  |  next  |  chance
We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23. We are in trouble if the parrot is talking and the hour is before 7 or after 20. Return True if we are in trouble.


parrot_trouble(True, 6) → True
parrot_trouble(True, 7) → False
parrot_trouble(False, 6) → False"""

def parrot_trouble(talking, hour):
    return (talking == True and ((hour < 7) or (hour > 20)))

def parrot_trouble(talking, hour):
  if (talking == True and (hour < 7 or hour > 20)):
    return True
  else:
    return False

def parrot_trouble(talking, hour):
  return (talking and (hour < 7 or hour > 20))
  # Need extra parenthesis around the or clause
  # since and binds more tightly than or.
  # and is like arithmetic *, or is like arithmetic +

"""Expected	Run		
parrot_trouble(True, 6) → True	True	OK	
parrot_trouble(True, 7) → False	False	OK	
parrot_trouble(False, 6) → False	False	OK	
parrot_trouble(True, 21) → True	True	OK	
parrot_trouble(False, 21) → False	False	OK	
parrot_trouble(False, 20) → False	False	OK	
parrot_trouble(True, 23) → True	True	OK	
parrot_trouble(False, 23) → False	False	OK	
parrot_trouble(True, 20) → False	False	OK	
parrot_trouble(False, 12) → False	False	OK	

All Correct"""

"""Warmup-1 > makes10
prev  |  next  |  chance
Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.


makes10(9, 10) → True
makes10(9, 9) → False
makes10(1, 9) → True"""

def makes10(a, b):
    return (a==10 or b==10) or (a + b == 10)

def makes10(a, b):
  return (a == 10 or b == 10 or a+b == 10)

"""Expected	Run		
makes10(9, 10) → True	True	OK	
makes10(9, 9) → False	False	OK	
makes10(1, 9) → True	True	OK	
makes10(10, 1) → True	True	OK	
makes10(10, 10) → True	True	OK	
makes10(8, 2) → True	True	OK	
makes10(8, 3) → False	False	OK	
makes10(10, 42) → True	True	OK	
makes10(12, -2) → True	True	OK	

All Correct"""

"""Warmup-1 > near_hundred
prev  |  next  |  chance
Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes the absolute value of a number.


near_hundred(93) → True
near_hundred(90) → True
near_hundred(89) → False"""

def near_hundred(n):
    return (90 <= n <= 110) or (190 <= n <= 210)

def near_hundred(n):
#  if ((90 <= n) and (n <= 110)):
#    return True
#  elif (190 <= n and n <= 210):
#    return True
#  else: 
#    return False 
  if n in range(90, 111):
    return True
  elif n in range(190, 211):
    return True
  else: 
    return False

def near_hundred(n):
  return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10))

"""Expected	Run		
near_hundred(93) → True	True	OK	
near_hundred(90) → True	True	OK	
near_hundred(89) → False	False	OK	
near_hundred(110) → True	True	OK	
near_hundred(111) → False	False	OK	
near_hundred(121) → False	False	OK	
near_hundred(-101) → False	False	OK	
near_hundred(-209) → False	False	OK	
near_hundred(190) → True	True	OK	
near_hundred(209) → True	True	OK	
near_hundred(0) → False	False	OK	
near_hundred(5) → False	False	OK	
near_hundred(-50) → False	False	OK	
near_hundred(191) → True	True	OK	
near_hundred(189) → False	False	OK	
near_hundred(200) → True	True	OK	
near_hundred(210) → True	True	OK	
near_hundred(211) → False	False	OK	
near_hundred(290) → False	False	OK	

All Correct"""

"""Warmup-1 > pos_neg
prev  |  next  |  chance
Given 2 int values, return True if one is negative and one is positive. Except if the parameter "negative" is True, then return True only if both are negative.


pos_neg(1, -1, False) → True
pos_neg(-1, 1, False) → True
pos_neg(-4, -5, True) → True"""

def pos_neg(a, b, negative):
  if negative == True and a<0 and b<0:
    return True
  elif a > 0 and b < 0 and negative == False:
    return True
  elif a < 0 and b > 0 and negative == False:
    return True
  else:
    return False

def pos_neg(a, b, negative):
  if negative:
    return (a < 0 and b < 0)
  else:
    return ((a < 0 and b > 0) or (a > 0 and b < 0))

""" LEARNING WITH MISTAKES 
WRONG 
def pos_neg(a, b, negative):
  if ((negative == True) and (a <0 and b < 0)):
    return True
  elif (a>0 and b<0):
    return True
  elif (a<0 and b>0):
    return True
  else:
    return False

pos_neg(-4, 5, True) → False	True	X	
pos_neg(1, -1, True) → False	True	X	
pos_neg(-1, 1, True) → False	True	X
pos_neg(-5, 6, True) → False	True	X

HOW TO CORRECT

def pos_neg(a, b, negative):
  if ((negative == True) and (a <0 and b < 0)):
    return True
  elif (a>0 and b<0) and negative == False:
    return True
  elif (a<0 and b>0) and negative == False:
    return True
  else:
    return False
"""


"""Expected	Run		
pos_neg(1, -1, False) → True	True	OK	
pos_neg(-1, 1, False) → True	True	OK	
pos_neg(-4, -5, True) → True	True	OK	
pos_neg(-4, -5, False) → False	False	OK	
pos_neg(-4, 5, False) → True	True	OK	
pos_neg(-4, 5, True) → False	False	OK	
pos_neg(1, 1, False) → False	False	OK	
pos_neg(-1, -1, False) → False	False	OK	
pos_neg(1, -1, True) → False	False	OK	
pos_neg(-1, 1, True) → False	False	OK	
pos_neg(1, 1, True) → False	False	OK	
pos_neg(-1, -1, True) → True	True	OK	
pos_neg(5, -5, False) → True	True	OK	
pos_neg(-6, 6, False) → True	True	OK	
pos_neg(-5, -6, False) → False	False	OK	
pos_neg(-2, -1, False) → False	False	OK	
pos_neg(1, 2, False) → False	False	OK	
pos_neg(-5, 6, True) → False	False	OK	
pos_neg(-5, -5, True) → True	True	OK	

All Correct"""

"""Warmup-1 > not_string
prev  |  next  |  chance
Given a string, return a new string where "not " has been added to the front. However, if the string already begins with "not", return the string unchanged.


not_string('candy') → 'not candy'
not_string('x') → 'not x'
not_string('not bad') → 'not bad'"""

def not_string(str):
    if str[0:3] == 'not':
        return str
    else:
        return 'not '+str

def not_string(str):
  if len(str) >= 3 and str[:3] == "not":
    return str
  return "not " + str
  # str[:3] goes from the start of the string up to but not
  # including index 3

"""Expected	Run		
not_string('candy') → 'not candy'	'not candy'	OK	
not_string('x') → 'not x'	'not x'	OK	
not_string('not bad') → 'not bad'	'not bad'	OK	
not_string('bad') → 'not bad'	'not bad'	OK	
not_string('not') → 'not'	'not'	OK	
not_string('is not') → 'not is not'	'not is not'	OK	
not_string('no') → 'not no'	'not no'	OK	

All Correct"""

"""Warmup-1 > missing_char
prev  |  next  |  chance
Given a non-empty string and an int n, return a new string where the char at index n has been removed. The value of n will be a valid index of a char in the original string (i.e. n will be in the range 0..len(str)-1 inclusive).


missing_char('kitten', 1) → 'ktten'
missing_char('kitten', 0) → 'itten'
missing_char('kitten', 4) → 'kittn'"""

def missing_char(str, n):
    letras = len(str)
    return str[0:n] + str[n+1:letras]

def missing_char(str, n):
  front = str[:n]   # up to BUT NOT including n (we skip n)
  back = str[n+1:]  # n+1 through end of str (after skip n)
  return front + back # we concatenate front ]n[ back

"""Expected	Run		
missing_char('kitten', 1) → 'ktten'	'ktten'	OK	
missing_char('kitten', 0) → 'itten'	'itten'	OK	
missing_char('kitten', 4) → 'kittn'	'kittn'	OK	
missing_char('Hi', 0) → 'i'	'i'	OK	
missing_char('Hi', 1) → 'H'	'H'	OK	
missing_char('code', 0) → 'ode'	'ode'	OK	
missing_char('code', 1) → 'cde'	'cde'	OK	
missing_char('code', 2) → 'coe'	'coe'	OK	
missing_char('code', 3) → 'cod'	'cod'	OK	
missing_char('chocolate', 8) → 'chocolat'	'chocolat'	OK	

All Correct"""

"""Warmup-1 > front_back
prev  |  next  |  chance
Given a string, return a new string where the first and last chars have been exchanged.


front_back('code') → 'eodc'
front_back('a') → 'a'
front_back('ab') → 'ba'"""

def front_back(str):
    if len(str) <= 1:
        return str # if it is one char or empty, samesame
    else:
        primeiraLetra = str[0]
        ultimaLetra = str[-1]
        return ultimaLetra + str[1:-1] + primeiraLetra

def front_back(str):
  if len(str) <= 1:
    return str
  mid = str[1:len(str)-1]  # can be written as str[1:-1]
  # last + mid + first
  return str[len(str)-1] + mid + str[0]

"""Expected	Run		
front_back('code') → 'eodc'	'eodc'	OK	
front_back('a') → 'a'	'a'	OK	
front_back('ab') → 'ba'	'ba'	OK	
front_back('abc') → 'cba'	'cba'	OK	
front_back('') → ''	''	OK	
front_back('Chocolate') → 'ehocolatC'	'ehocolatC'	OK	
front_back('aavJ') → 'Java'	'Java'	OK	
front_back('hello') → 'oellh'	'oellh'	OK	

All Correct"""

"""Warmup-1 > front3
prev  |  next  |  chance
Given a string, we'll say that the front is the first 3 chars of the string. If the string length is less than 3, the front is whatever is there. Return a new string which is 3 copies of the front.


front3('Java') → 'JavJavJav'
front3('Chocolate') → 'ChoChoCho'
front3('abc') → 'abcabcabc'"""

def front3(str):
    if len(str) < 3:
        return str*3
    else:
        return str[0:3]*3

def front3(str):
  # Figure the end of the front
  front_end = 3
  if len(str) < front_end:
    front_end = len(str)
  front = str[:front_end]
  return front + front + front   
  # Could omit the if logic, and write simply front = str[:3]
  # since the slice is silent about out-of-bounds conditions.

"""Expected	Run		
front3('Java') → 'JavJavJav'	'JavJavJav'	OK	
front3('Chocolate') → 'ChoChoCho'	'ChoChoCho'	OK	
front3('abc') → 'abcabcabc'	'abcabcabc'	OK	
front3('abcXYZ') → 'abcabcabc'	'abcabcabc'	OK	
front3('ab') → 'ababab'	'ababab'	OK	
front3('a') → 'aaa'	'aaa'	OK	
front3('') → ''	''	OK	

All Correct"""

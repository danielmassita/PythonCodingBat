"""
String-2 chance
Medium python string problems -- 1 loop.. Use + to combine strings, len(str) is the number of chars in a String, str[i:j] extracts the substring starting at index i and running up to but not including index j.

double_char H	        count_hi H      	  cat_dog
count_code        	  end_other H     	  xyz_there
"""

"""
String-2 > double_char
prev  |  next  |  chance
Given a string, return a string where for every char in the original, there are two chars.


double_char('The') → 'TThhee'
double_char('AAbb') → 'AAAAbbbb'
double_char('Hi-There') → 'HHii--TThheerree'

Hint:
In Python, the loop "for i in range(len(str)):" loops i through each index in the string, 0, 1, 2, .. len-1.
"""
def double_char(str):
  word = ''
  for char in str:
    word += char * 2 
  return word

# Our Solution:

def double_char(str):
  result = ""
  for i in range(len(str)):
    result += str[i] + str[i]
  return result
"""
Expected	Run		
double_char('The') → 'TThhee'	'TThhee'	OK	
double_char('AAbb') → 'AAAAbbbb'	'AAAAbbbb'	OK	
double_char('Hi-There') → 'HHii--TThheerree'	'HHii--TThheerree'	OK	
double_char('Word!') → 'WWoorrdd!!'	'WWoorrdd!!'	OK	
double_char('!!') → '!!!!'	'!!!!'	OK	
double_char('') → ''	''	OK	
double_char('a') → 'aa'	'aa'	OK	
double_char('.') → '..'	'..'	OK	
double_char('aa') → 'aaaa'	'aaaa'	OK	
other tests
OK	

All Correct
Good job -- problem solved. You can see our solution as an alternative.
"""

"""
String-2 > count_hi
prev  |  next  |  chance
Return the number of times that the string "hi" appears anywhere in the given string.


count_hi('abc hi ho') → 1
count_hi('ABChi hi') → 2
count_hi('hihi') → 2
Hint:
Use the "for i in range(len(str)-1):" loop to look at each index in the string, except the last. For each i, extract the string starting at i and up to but not including i+2. Check if that string is 'hi', and count how many times that happens.
"""
def count_hi(str):
  count = 0
  tamanho = len(str) # tamanho será uma INT
  
  for i in range(tamanho-1): # o i vai iterar pelo range INT tamanho-1 (pois começa em zero)
    if str[i:i+2] == 'hi':
      count += 1
  return count
  
Our Solution:

def count_hi(str):
  sum = 0
  ## Loop to length-1 and access index i and i+1
  ## in the loop.
  for i in range(len(str)-1):
    if str[i:i+2] == 'hi':
      sum = sum + 1
  return sum
"""
Expected	Run		
count_hi('abc hi ho') → 1	1	OK	
count_hi('ABChi hi') → 2	2	OK	
count_hi('hihi') → 2	2	OK	
count_hi('hiHIhi') → 2	2	OK	
count_hi('') → 0	0	OK	
count_hi('h') → 0	0	OK	
count_hi('hi') → 1	1	OK	
count_hi('Hi is no HI on ahI') → 0	0	OK	
count_hi('hiho not HOHIhi') → 2	2	OK	
other tests
OK	

All Correct
Good job -- problem solved. You can see our solution as an alternative. 
"""

"""
String-2 > cat_dog
prev  |  next  |  chance
Return True if the string "cat" and "dog" appear the same number of times in the given string.


cat_dog('catdog') → True
cat_dog('catcat') → False
cat_dog('1cat1cadodog') → True
"""
def cat_dog(string):
    count_cat = 0
    count_dog = 0

    for i in range(len(string) - 2):
        if string[i:i+3] == 'cat':
            count_cat += 1
        elif string[i:i+3] == 'dog':
            count_dog += 1

    return count_cat == count_dog
  
"""
Expected	Run		
cat_dog('catdog') → True	True	OK	
cat_dog('catcat') → False	False	OK	
cat_dog('1cat1cadodog') → True	True	OK	
cat_dog('catxxdogxxxdog') → False	False	OK	
cat_dog('catxdogxdogxcat') → True	True	OK	
cat_dog('catxdogxdogxca') → False	False	OK	
cat_dog('dogdogcat') → False	False	OK	
cat_dog('dogogcat') → True	True	OK	
cat_dog('dog') → False	False	OK	
cat_dog('cat') → False	False	OK	
cat_dog('ca') → True	True	OK	
cat_dog('c') → True	True	OK	
cat_dog('') → True	True	OK	
other tests
OK	

All Correct
"""

"""
String-2 > count_code
prev  |  next  |  chance
Return the number of times that the string "code" appears anywhere in the given string, except we'll accept any letter for the 'd', so "cope" and "cooe" count.


count_code('aaacodebbb') → 1
count_code('codexxcode') → 2
count_code('cozexxcope') → 2
"""

def count_code(string):
    count = 0
    for i in range(len(string) - 3):
        if string[i:i+2] == 'co' and string[i+3] == 'e':
            count += 1
    return count
  
"""
Expected	Run		
count_code('aaacodebbb') → 1	1	OK	
count_code('codexxcode') → 2	2	OK	
count_code('cozexxcope') → 2	2	OK	
count_code('cozfxxcope') → 1	1	OK	
count_code('xxcozeyycop') → 1	1	OK	
count_code('cozcop') → 0	0	OK	
count_code('abcxyz') → 0	0	OK	
count_code('code') → 1	1	OK	
count_code('ode') → 0	0	OK	
count_code('c') → 0	0	OK	
count_code('') → 0	0	OK	
count_code('AAcodeBBcoleCCccoreDD') → 3	3	OK	
count_code('AAcodeBBcoleCCccorfDD') → 2	2	OK	
count_code('coAcodeBcoleccoreDD') → 3	3	OK	
other tests
OK	

All Correct
"""
  

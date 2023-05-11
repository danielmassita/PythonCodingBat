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

"""
Warmup-2 chance
Medium warmup string/list problems with loops (solutions available)

 string_times H   	    front_times H	    string_bits H
 string_splosion H  	  last2 H	          array_count9 H
 array_front9 H	       array123 H   	    string_match H
 """

"""
Warmup-2 > string_times
prev  |  next  |  chance
Given a string and a non-negative int n, return a larger string that is n copies of the original string.


string_times('Hi', 2) → 'HiHi'
string_times('Hi', 3) → 'HiHiHi'
string_times('Hi', 1) → 'Hi'
"""

def string_times(str, n):
  front = 3
  tamanho = len(str)
  result = ""
  
  if tamanho < 3:
    front = str[0:tamanho]
    result = str*n
    return result
  else:
    return str*n

# Our Solution:
def string_times(str, n):
  result = ""
  for i in range(n):  # range(n) is [0, 1, 2, .... n-1]
    result = result + str  # could use += here
  return result   

"""
Expected	Run		
string_times('Hi', 2) → 'HiHi'	'HiHi'	OK	
string_times('Hi', 3) → 'HiHiHi'	'HiHiHi'	OK	
string_times('Hi', 1) → 'Hi'	'Hi'	OK	
string_times('Hi', 0) → ''	''	OK	
string_times('Hi', 5) → 'HiHiHiHiHi'	'HiHiHiHiHi'	OK	
string_times('Oh Boy!', 2) → 'Oh Boy!Oh Boy!'	'Oh Boy!Oh Boy!'	OK	
string_times('x', 4) → 'xxxx'	'xxxx'	OK	
string_times('', 4) → ''	''	OK	
string_times('code', 2) → 'codecode'	'codecode'	OK	
string_times('code', 3) → 'codecodecode'	'codecodecode'	OK	

All Correct
next  |  chance
"""

"""
Warmup-2 > front_times
prev  |  next  |  chance
Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars, or whatever is there if the string is less than length 3. Return n copies of the front;


front_times('Chocolate', 2) → 'ChoCho'
front_times('Chocolate', 3) → 'ChoChoCho'
front_times('Abc', 3) → 'AbcAbcAbc'
"""

def front_times(str, n):  # str é a string (pode ser vazia? talvez... entender str = ""); n é o número não negativo (pode ser zero? talvez...)
  result = ""
  front = str[0:3] # chars de zero, um, dois - três EXcluso...
  for i in range(n):
    result += front
  return result

def front_times(str, n): # Resposta alternativa, usando uma sintaxe mais pythonic str[0:3]*n, mas precisa ver casos menores que len(str) < 3... 
  if len(str) < 3:
    return str*n
  else:
    return str[0:3]*n
   
# Our Solution:
def front_times(str, n):
  front_len = 3
  if front_len > len(str):
    front_len = len(str)
  front = str[:front_len]
  
  result = ""
  for i in range(n):
    result = result + front
  return result

 """
 Expected	Run		
front_times('Chocolate', 2) → 'ChoCho'	'ChoCho'	OK	
front_times('Chocolate', 3) → 'ChoChoCho'	'ChoChoCho'	OK	
front_times('Abc', 3) → 'AbcAbcAbc'	'AbcAbcAbc'	OK	
front_times('Ab', 4) → 'AbAbAbAb'	'AbAbAbAb'	OK	
front_times('A', 4) → 'AAAA'	'AAAA'	OK	
front_times('', 4) → ''	''	OK	
front_times('Abc', 0) → ''	''	OK	

All Correct
"""
 
 
 
"""
Warmup-2 > string_bits
prev  |  next  |  chance
Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".


string_bits('Hello') → 'Hlo'
string_bits('Hi') → 'H'
string_bits('Heeololeo') → 'Hello'
"""

def string_bits(str):
  tamanho = len(str);
  return str[0:tamanho:2]

# Solution:
def string_bits(str):
  result = ""
  # Many ways to do this. This uses the standard loop of i on every char,
  # and inside the loop skips the odd index values.
  for i in range(len(str)):
    if i % 2 == 0:
      result = result + str[i]
  return result
 
 """
 Expected	Run		
string_bits('Hello') → 'Hlo'	'Hlo'	OK	
string_bits('Hi') → 'H'	'H'	OK	
string_bits('Heeololeo') → 'Hello'	'Hello'	OK	
string_bits('HiHiHi') → 'HHH'	'HHH'	OK	
string_bits('') → ''	''	OK	
string_bits('Greetings') → 'Getns'	'Getns'	OK	
string_bits('Chocoate') → 'Coot'	'Coot'	OK	
string_bits('pi') → 'p'	'p'	OK	
string_bits('Hello Kitten') → 'HloKte'	'HloKte'	OK	
string_bits('hxaxpxpxy') → 'happy'	'happy'	OK	

All Correct
 """

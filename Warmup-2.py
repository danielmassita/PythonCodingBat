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

 
"""
Warmup-2 > string_splosion
prev  |  next  |  chance
Given a non-empty string like "Code" return a string like "CCoCodCode".


string_splosion('Code') → 'CCoCodCode'
string_splosion('abc') → 'aababc'
string_splosion('ab') → 'aab'
"""

"""
str[0]
str[0:1]
str[0:2]
[str[0:3]
...
str[:i]
"""

def string_splosion(str):
 tamanho = len(str)
 result = ""
 for i in range(tamanho+1):
  strings = str[:i]
  result += strings
 return ressult

# Solution:
def string_splosion(str):
  result = ""
  # On each iteration, add the substring of the chars 0..i
  for i in range(len(str)):
    result = result + str[:i+1]
  return result

"""
Expected	Run		
string_splosion('Code') → 'CCoCodCode'	'CCoCodCode'	OK	
string_splosion('abc') → 'aababc'	'aababc'	OK	
string_splosion('ab') → 'aab'	'aab'	OK	
string_splosion('x') → 'x'	'x'	OK	
string_splosion('fade') → 'ffafadfade'	'ffafadfade'	OK	
string_splosion('There') → 'TThTheTherThere'	'TThTheTherThere'	OK	
string_splosion('Kitten') → 'KKiKitKittKitteKitten'	'KKiKitKittKitteKitten'	OK	
string_splosion('Bye') → 'BByBye'	'BByBye'	OK	
string_splosion('Good') → 'GGoGooGood'	'GGoGooGood'	OK	
string_splosion('Bad') → 'BBaBad'	'BBaBad'	OK	

All Correct
"""

"""
Warmup-2 > last2
prev  |  next  |  chance
Given a string, return the count of the number of times that a substring length 2 appears in the string and also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).


last2('hixxhi') → 1
last2('xaxxaxaxx') → 1
last2('axxxaaxx') → 2
"""
# Aqui veio do Amigo... 

def last2(str):
    if len(str) < 2:
        return 0
    
    last2 = str[-2:]
    count = 0
    
    for i in range(len(str) - 2):
        if str[i:i+2] == last2:
            count += 1
    
    return count
   
 # Aqui veio do meu antigo exercício...
 def last2(str):
  postFix = str[-2:0] # 'hixxaaxx[hi]' > [hi] == last2 > if loop 'ch' == [hi] > count++ 
  count = 0
  
  for ch in str:
    if ch == postFix:
      count += 1
  return count
    
# Solution:
def last2(str):
  # Screen out too-short string case.
  if len(str) < 2:
    return 0
  # last 2 chars, can be written as str[-2:]
  last2 = str[len(str)-2:]
  count = 0
  
  # Check each substring length 2 starting at i
  for i in range(len(str)-2):
    sub = str[i:i+2]
    if sub == last2:
      count = count + 1

  return count
 
 """
 Expected	Run		
last2('hixxhi') → 1	1	OK	
last2('xaxxaxaxx') → 1	1	OK	
last2('axxxaaxx') → 2	2	OK	
last2('xxaxxaxxaxx') → 3	3	OK	
last2('xaxaxaxx') → 0	0	OK	
last2('xxxx') → 2	2	OK	
last2('13121312') → 1	1	OK	
last2('11212') → 1	1	OK	
last2('13121311') → 0	0	OK	
last2('1717171') → 2	2	OK	
last2('hi') → 0	0	OK	
last2('h') → 0	0	OK	
last2('') → 0	0	OK	

All Correct
 """

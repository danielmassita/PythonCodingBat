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

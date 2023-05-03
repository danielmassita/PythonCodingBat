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

   
"""

"""

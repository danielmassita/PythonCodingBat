"""
Logic-1 > cigar_party
prev  |  next  |  chance
When squirrels get together for a party, they like to have cigars. A squirrel party is successful when the number of cigars is between 40 and 60, inclusive. Unless it is the weekend, in which case there is no upper bound on the number of cigars. Return True if the party with the given values is successful, or False otherwise.


cigar_party(30, False) → False
cigar_party(50, False) → True
cigar_party(70, True) → True
"""

def cigar_party(cigars, is_weekend):
  if is_weekend == True: 
    if cigars >= 40:
      return True
    else: 
      return False
  elif cigars >= 40 and cigars <= 60:
    return True
  else:
    return False
  
  
def cigar_party(cigars, is_weekend):
  if is_weekend:
    return (cigars >= 40)
  else:
    return (cigars >= 40 and cigars <= 60)
  
"""
Expected	Run		
cigar_party(30, False) → False	False	OK	
cigar_party(50, False) → True	True	OK	
cigar_party(70, True) → True	True	OK	
cigar_party(30, True) → False	False	OK	
cigar_party(50, True) → True	True	OK	
cigar_party(60, False) → True	True	OK	
cigar_party(61, False) → False	False	OK	
cigar_party(40, False) → True	True	OK	
cigar_party(39, False) → False	False	OK	
cigar_party(40, True) → True	True	OK	
cigar_party(39, True) → False	False	OK	
other tests
OK	

All Correct
"""

"""
Logic-1 > date_fashion
prev  |  next  |  chance
You and your date are trying to get a table at a restaurant. The parameter "you" is the stylishness of your clothes, in the range 0..10, and "date" is the stylishness of your date's clothes. The result getting the table is encoded as an int value with 0=no, 1=maybe, 2=yes. If either of you is very stylish, 8 or more, then the result is 2 (yes). With the exception that if either of you has style of 2 or less, then the result is 0 (no). Otherwise the result is 1 (maybe).


date_fashion(5, 10) → 2
date_fashion(5, 2) → 0
date_fashion(5, 5) → 1
"""

def date_fashion(you, date):
  if you <= 2 or date <= 2:
    return 0
  elif you >= 8 or date >= 8:
    return 2
  else: 
    return 1

def date_fashion(you, date):
  ## Check the <=2 case first, since it takes precedence
  ## over the >=8 case.
  if (you <= 2) or (date <= 2):
    return 0
  elif (you >= 8) or (date >= 8):
    return 2
  else:
    return 1
  
"""
Expected	Run		
date_fashion(5, 10) → 2	2	OK	
date_fashion(5, 2) → 0	0	OK	
date_fashion(5, 5) → 1	1	OK	
date_fashion(3, 3) → 1	1	OK	
date_fashion(10, 2) → 0	0	OK	
date_fashion(2, 9) → 0	0	OK	
date_fashion(9, 9) → 2	2	OK	
date_fashion(10, 5) → 2	2	OK	
date_fashion(2, 2) → 0	0	OK	
date_fashion(3, 7) → 1	1	OK	
date_fashion(2, 7) → 0	0	OK	
date_fashion(6, 2) → 0	0	OK	
other tests
OK	

All Correct
"""

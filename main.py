# assignment-03

# no other imports needed
from collections import defaultdict
import math

### PARENTHESES MATCHING

#### Iterative solution
def plus(a,b):
  return a + b

  
def iterate(f,x,a):
  if len(a) == 0:
    return x
  else:
    return iterate(f,f(x,a[0]), a[1:])

def reduce(f, id_, a):
  if len(a) == 0:
    return id_
  elif len(a) == 1:
    return a[0]
  else:
    return f(reduce(f,id_,a[:len(a) // 2]), reduce(f,id_,a[len(a) // 2:]))

def parens_match_iterative(mylist):
  count = iterate(parens_update,0,mylist)
  if(count == 0):
    return True
  if (len(count) >= 1):
    return False
  else:
    return True
    

def parens_update(current_output, next_input):
  if(current_output == 0):
    return next_input
  if(current_output[-1] == '(' and next_input == ')'):
    if (len(current_output) == 1):
      return 0
    else:
      return current_output[:-1]
  if (next_input == '(' or next_input == ')'):
    return current_output + next_input
  else:
    return current_output
    

def test_parens_match_iterative():
    assert parens_match_iterative(['(', ')']) == True
    assert parens_match_iterative(['(']) == False
    assert parens_match_iterative([')']) == False


#### Scan solution

def parens_match_scan(mylist):
  list = []
  for element in mylist:
    list.append(paren_map(element))
  if(list[0] == -1 or list[len(list)-1] == 1):
    return False
  if(scan(plus,0,list)[1] != 0 and reduce(plus,0,list) != 0):
    return False
  else:
    return True
    

def scan(f, id_, a):
    """
    This is a horribly inefficient implementation of scan
    only to understand what it does.
    We saw a more efficient version in class. You can assume
    the more efficient version is used for analyzing work/span.
    """
    return (
            [reduce(f, id_, a[:i+1]) for i in range(len(a))],
             reduce(f, id_, a)
           )

def paren_map(x):
  
    if x == '(':
        return 1
    elif x == ')':
        return -1
    else:
        return 0

def min_f(x,y):
    if x < y:
        return x
    return y

def test_parens_match_scan():
    assert parens_match_scan(['(', ')']) == True
    assert parens_match_scan(['(']) == False
    assert parens_match_scan([')']) == False

#### Divide and conquer solution

def parens_match_dc(mylist):
    n_unmatched_left, n_unmatched_right = parens_match_dc_helper(mylist)
    return n_unmatched_left==0 and n_unmatched_right==0

def parens_match_dc_helper(mylist):
  if(len(mylist) == 0):
    return 0,0
  if(mylist[-1] == '(' or mylist[0] == ')'):
    return 1,1
  if(len(mylist) == 1):
    if(mylist[0] == ')'):
      return 1,0
    elif(mylist[0] == '('):
      return 0,1
    else:
      return 0,0
    x = len(mylist)
    left = parens_match_dc_helper(mylist[x // 2:])
    right = parens_match_dc_helper(mylist[:x // 2])
    left = reduce(plus,0,left)
    right = reduce(plus,0,right)
    while(left > 0 and right > 0):
      left -= 1
      right -= 1
    return (left,right)
      
   
    

def test_parens_match_dc():
    assert parens_match_dc(['(', ')']) == True
    assert parens_match_dc(['(']) == False
    assert parens_match_dc([')']) == False

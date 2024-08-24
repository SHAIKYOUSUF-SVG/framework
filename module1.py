### module1

def add_nums(x,y):
  """sum of two numbers"""
  return x+y
  
def sub_nums(x,y):
  """ difference of two numbers"""
  return x-y
  
def mul_nums(x,y):
   """multiplication of two numbers"""
   return x*y 

def div_nums(x,y):
    """ multiplicaton of two numbers """
    return x/y
    
def even_nums(x1):
   x = []
   for i in x1:
     if i%2 == 0:
        x.append(i)
   return x
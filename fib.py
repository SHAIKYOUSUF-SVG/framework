

def fib_series(int1):

  

  x = []

  for i in range (0,int1):
   
    if i < 2:
         x.append(i)
    else:
         x.append(x[i-1]+x[i-2])
  return (x)   
     
     

y = (fib_series(int(input("enter input "))))



for i in (y):
   print(i)
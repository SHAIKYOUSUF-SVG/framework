n = 91
l3 =[]


for i in range (0,n):
   l1 = True
   for j in range (2,round(n/2)):
      if i%j == 0:
         l1 = False
     
   if l1 == True:
        l3.append(i)
print(l3)
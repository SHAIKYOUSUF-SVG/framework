


def asc_list(list1):




 
 for i in range (0,len(list1)):


  
   for j in range(i+1,len(list1)):
      if list1[i] > list1[j]:
         list1[i],list1[j] = list1[j],list1[i]
 return list1



x = list((input('enter list ')))



y = ((asc_list(x)))
for i in y:
   if i == "," :
    y.remove(",")
   else:
    continue
print(y)

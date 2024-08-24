list1 = [1,2,2,4,5,7,1]

list2 = []
list3 =[]

for i in (list1):
   if i not in list2 :
     list2.append(i)
   else:
     list3.append(i)
for j in  list2:
   if j not in list3:
     print(j)   
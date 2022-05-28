other_list = []
list = [2,4,7,8,4,1,3]
for x in list: 
    print (x)
list.append(70)
for x in  list:
    other_list.append(x)
    print (other_list) 
list_1 = [1,5,6,2]
list_2 = [elem for elem in list_1]
print (list_2)

other_list = []
list = [2,4,7,8,4,1,3]
for x  in list:
     if x%2 == 0:
         other_list.append(x)
     print (other_list)
def add (a,b):
    return (a+b)
result = add (4,5)
print (result)



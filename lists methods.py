          #LISTS
subjects = ["math","bio","swa"]
subjects.append ("phyc") # add things to lists
print (subjects)
subjects.remove ("bio") #removing things from lists
print (subjects)
subjects.pop (2) #removing things from lists using indexes
print (subjects)
my_subjects = subjects.pop(1)
print(subjects)
print (my_subjects)
subjects_2 = ["chem","eng",]
subjects_3 = (subjects) + (subjects_2)# adding two lists using plus sign
print (subjects_3)
subjects.extend(subjects_2) #extend combines two lists into one(adds list 2 to list one)
subjects_2.clear()#clears contents of list 2
print (subjects_2)#empty
print (subjects)#combined

          #TUPLES (can't remove or add items)
lessons = ("art","music","french")
print (lessons)
print (lessons[1])
new_list = list(lessons) #converting tuples to lists
new_list.append("spanish")
lessons = tuple(new_list) #converting lists back to tuples
print (lessons)

          #SETS (doesn't allow duplicate values like lists and tuples)
cities = {"nairobi","eldoret","nakuru","mombasa","nairobi","nakuru"}
print (cities)

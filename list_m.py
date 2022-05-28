
#for loops with lists
words = ["I","DID","A"]
for word in words :
    print (word + "!")

str = "hello guys welcome back to my class"
count = 0
for x in str :
    if(x =="o"):
         count+=1
print ("the number of o's is:",count)


str = "hello guys welcome back to my class"
for x in str :
    if(x =="l"):
        continue
    else :
        print (x)

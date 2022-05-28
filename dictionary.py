#dictionaries in python
mydict = {
    "book" : "dynamics",
    "publisher" : "longhorn",
    "year" : 2001,
    "authors" : ["kianna","kiarra","temina"]
}


#accesing item
x = mydict["year"]
print(x)

#accesing using get()
y = mydict["year"]
print(y)

#allkeys
x = mydict.keys()
print(x)

#allvalues
x = mydict.values()
print(x)

#checking if keys exist
if "publisher" in mydict :
    print ("publisher is one of the keys")
print (len(mydict))

#dictionaries cannot contain duplicates
#dictionaries can hold different datatypes

x = mydict["authors"]
print (x)
f_num = float(input("input the first number"))
s_num = float(input("input the second number"))
function =input("input the function")
p = 0
if function == "+":
    p = f_num + s_num
    print("your answer is",p)
elif function == "-":
    p = s_num-f_num
    print("your answer is",p)
elif function =="*":
    p = f_num*s_num
    print("your answer is",p)
elif function =="/":
    p = f_num/s_num
    print("your answer is",p)
elif function == "sqrt":
    p = f_num ** 0.5
    print("your answer is",p)
elif function == "cbrt":
    p = f_num **(1./3)
    print("your answer is",p)
elif function == "sqr":
    p = f_num*f_num
    print("your answer is",p)
elif function == "cb":
    p = f_num*f_num*f_num
    print("your answer is",p)
elif function == "^2" :
    p = f_num**(2)
    print("your answer is",p)
else:
    print("input valid function")


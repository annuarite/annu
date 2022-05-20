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
else:
    print("input valid function")

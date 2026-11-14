import operator
print("Hello, friends. It's my first preview release. If there are some bugs, please tell me.")
a=int(input("Your first number:"))
c=int(input("Your second number:"))
b=input("Your symbol:")

ops = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
try:
    d = ops[b](a, c)
except (KeyError, ZeroDivisionError) as e:
    d = "Error: Invalid input or division by zero"

print(d)
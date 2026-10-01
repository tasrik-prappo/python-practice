a = float(input("Enter first number: "))
op = input("Enter the operator (e.g +,-,*,/,%,//,**): ")
b = float(input("Enter second number: "))

if op == '+':
    print(a+b)
elif op == '-':
    print(a-b)
elif op == '/':
    print(a/b)
elif op == '*':
    print(a*b)
elif op == '%':
    print(a%b)
elif op == '//':
    print(a//b)
elif op == '**':
    print(a**b)
else:
    print("Invalid operator. Please choose +,-,*,/,%,//,** among these operators")
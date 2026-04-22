num1=float(input("enter a number: "))
num2=float(input("enter a number: "))

print("select operation: ")

print("enter 1 for addition\n enter 2 for subtracion\n enter 3 for multiplicattion\n " \
"enter 4 for division\n ")
choice=float(input("enter choice (1/2/3/4): "))


if choice==1:
    print(num1+num2)
elif choice==2:
    print(num1-num2)
elif choice==3:
    print(num1 *num2)
elif choice==4:
    print(num1/num2)
else:
    print ("invalid")
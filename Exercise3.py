#Write a Python program to parse a string to Float or Integer.

a = int(15.5)

print(a)

#Given variables x=30 and y=20, write a Python program to print t "30+20=50".
x = 30
y = 20
c = x+y

print(c)

#Enter the value with the input. Convert the entered value to integer.
# Print the value obtained by dividing that value by 2, 3, 5, and 10.
x = int(input("enter the number x "))
v1=x//2
v2=x//3
v3=x//5
v4=x//10

v=(v1,v2,v3,v4)

print("Results ", v)


#Enter the value with the input. Convert the entered value to integer.
# Print the remainder of the value divided by 2, 3, 5, and 10.
a = int(input("Please enter the value a "))
b1 = x % 2
b2 = x % 3
b3 = x % 5
b4 = x % 10

v = (b1, b2, b3, b4)

print("Print the remainder of the value " + str(v))

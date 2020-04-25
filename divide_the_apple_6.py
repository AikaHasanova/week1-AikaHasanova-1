#n schoolchildren divide k apples evenly,
# the residue remains in the basket. How many apples remains in the basket?

#Input
#two integers n and k not greater than 1500 - rarely happens in school more pupils,
# and where to find such a basket?
n = int(input("Enter the number of schoolchildren "))
k = int(input("Enter the number of apples "))

#Output
#Print the number of apples in the basket.
if (n < 1500) and (k < 1500):
    total = k//n
    print("Each student gets", total, " apples")
else:
    print("This number is more than 1500")




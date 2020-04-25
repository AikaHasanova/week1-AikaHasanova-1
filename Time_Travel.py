from math import sqrt

c = 299792458
p = int(input("Please Enter the velocity (Percentage of speed of light ): "))
print("Ship is travelling at", p, "% of the speed of light")
v =(c * p)/100

f = 1/sqrt(1-(v*v)/(c*c))

w = int(input("Please enter the weight of the shuttle "))
weight = w*f
AC = 4.3/f
BS = 6.0/f
B = 309 /f
Andr =2000000/f

print("At this speed:"""
      "\n weight of the shuttle is:", weight,
      "\nPerceived time to travel Alpha Centauri", AC,
      "years.\nPerceived time to travel Barnard's Star",BS,
      "years.\nBetelgeuse ", B,
      "years.\nAndromeda Galaxy )", Andr, "years")



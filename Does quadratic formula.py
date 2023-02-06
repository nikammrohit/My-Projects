#Does quadratic formula
import cmath

a = int(input("What is a?"))
b = int(input("What is b?"))
c = int(input("What is c?"))

d = (b**2)-(4*a*c)
f1 = (-b+cmath.sqrt(d))/(2*a)
f2 = (-b-cmath.sqrt(d))/(2*a)

print("the functions are",f1, "and",f2)
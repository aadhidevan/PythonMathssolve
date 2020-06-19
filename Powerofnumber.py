import math
while True:
 try:
     x = float(input("Number to find power?>>   "))
     y = float(input("power?>>   "))
     z = math.pow(x , y)
     print(z)
 except ValueError:
     print("Invalid Value.power can be only used for numbers")


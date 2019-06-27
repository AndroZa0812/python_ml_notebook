import math

a = float(input("Please enter a:"))
b = float(input("Please enter b:"))
c = float(input("Please enter c:"))

if (b**2 - (4 * a * c)) >= 0:
    print("x1 is {} and x2 is {}".format((-b + math.sqrt(b**2 - (4 * a * c))) / (2 * a),
                                         (-b - math.sqrt(b**2 - (4 * a * c))) / (2 * a)))
else:
    print("There are no x1,2 for the given numbers")

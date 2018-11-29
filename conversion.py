"""
convert from f to c, and c to f
"""
degree = input("enter c for celsius, or f for fahreiheit:")
temperature = int(input("enter the temperature:"))

if degree =='f':
    c = (temperature - 32) * 5/9
    print("the tempature in celsius is",round(c))
elif degree == 'c':
    f= temperature * 9/5 + 32
    print("the tempatuer in fahreiheit",round(f))
else:
    print("there is no such type of degree like", degree)
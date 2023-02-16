# if statement:
a = 5
b = 2
if a > b:
    print("a is greater than b")

# if ... else statement:
rain = True
if rain == True:
    print("School e jabo na.")
else:
    print("School e jabo.")

# if ... elif ... else statement:
print(10-4 == 6 and 10-5 == 15) # False
print(10-4 == 6 or 10-5 == 15) # True
print(not (10-5 == 15)) # True

# problem:
marks = 85
if marks >= 90 and marks <= 100:
    print("2 ta candy pabe")
elif marks >= 80 and marks <= 89:
    print("1 ta candy pabe")
else:
    print("kichu e pabe na")
# problem-1
length = int(input())
breadth = int(input())
if length == breadth:
    print("It's a square")
else:
    print("It's not a square")

# problem-2
a = input()
b = input()
c = input()
if a > b and a > c:
    print("a is the largest number")
elif b > a and b > c:
    print("b is the largest number")
else:
    print("c is the largest number")

# problem-3
num = int(input())
if num % 2 == 0:
    print(num, "is even")
else:
    print(num, "is odd")

# problem-4
mark = int(input())
if mark > 90:
    print("your grade is A")
elif mark > 80 and mark < 90:
    print("your grade is B")
elif mark >= 60 or mark <= 80:
    print("your grade is C")
else:
    print("your grade is D")

# problem-5
year = int(input())
if (year % 400 == 0 and year % 100 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")
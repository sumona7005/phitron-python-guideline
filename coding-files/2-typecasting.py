age = int(input())
weight = float(input())
# str and int can't be compared so used int, float

if age >= 18:
    print("you are adult")
else:
    print("you are child")

print(weight)
print(int(weight))
print(type(weight)) # check type

new_weight = int(weight)
print(new_weight)
print(type(new_weight)) # display int

new_new_weight = float(new_weight)
print(new_new_weight)
print(type(new_new_weight)) # display float
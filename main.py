
print("hello, world!")

list_e24 = list()

with open("e24.txt", "r") as file:
    for line in file:
        list_e24.append(float(line.strip()))


print(list_e24)

def calculate_resistor(r1, r2):
    r1 = 1/r1
    r2 = 1/r2
    result = r1 + r2
    return 1/result

val = 5.8

print(calculate_resistor(2, 1))




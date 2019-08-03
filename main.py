from resistor import Resistor

print("hello, world!")

list_e24 = list()

with open("E24.resistor", "r") as file:
    for line in file:
        list_e24.append(float(line.strip()))


print(list_e24)

for val1 in list_e24:
    for val2 in list_e24:
        r1 = Resistor(val=val1)
        r2 = Resistor(val=val2)
        rp = r1.parallel_with(r2)
        if 5.75 < rp.value() < 5.85:
            print(r1.value(), r2.value(), "result:", rp.value())

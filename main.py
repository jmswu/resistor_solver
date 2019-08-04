from resistor_data import ResistorData
from resistor_solver import ResistorSolver

print("hello, world!")

solver = ResistorSolver(target=5.8, tolerance=0.005)

data = ResistorData()

for item in data.get_resistor_dataset():
    print("name:", item.name(), "data:", item.data())

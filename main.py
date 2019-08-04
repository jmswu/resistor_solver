from resistor_solver import ResistorSolver

print("hello, world!")

solver = ResistorSolver(target=5.8, tolerance=0.005)

result = solver.solution()

for item in result:
    print(item)

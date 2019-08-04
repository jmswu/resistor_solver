from resistor_solver import ResistorSolver

VER_MAJOR = 0
VER_MINOR = 1
AUTHOR = "James Wu"
EMAIL = "jameswu62@yahoo.co.nz"

print("Resistor Solver, v%i.%i, by %s - %s" % (VER_MAJOR, VER_MINOR, AUTHOR, EMAIL))

try:
    target = float(input("Please enter target value:"))
    tolerance = float(input("Please enter tolerance:"))
    solver = ResistorSolver(target=target, tolerance=tolerance)
    result = solver.solution()
    for item in result:
        print(item)
except ValueError:
    print("Wrong value enter.")

from resistor_data import ResistorData
from resistor_solver import ResistorSolver

VER_MAJOR = 0
VER_MINOR = 1
AUTHOR = "James Wu"
EMAIL = "jameswu62@yahoo.co.nz"

name = ResistorData().get_names()

print("[Over complicated] Resistor Solver, v%i.%i, by %s - %s" % (VER_MAJOR, VER_MINOR, AUTHOR, EMAIL))
print("Available data set:", end=' ')
print(*name)

try:
    # get user inputs
    target = float(input("Please enter target value:"))
    tolerance = float(input("Please enter tolerance:"))

    # find a solution
    solver = ResistorSolver(target=target, tolerance=tolerance)
    result = solver.solution()

    # sort output according to error
    result.sort(key=lambda x :abs(x[4]))

    # print result
    for item in result:
        print("%s, R1=%f, R2=%.2f, RParallel=%.4f, error=%.4f" % (item[0], item[1], item[2], item[3], item[4]))
except ValueError:
    print("Wrong value enter.")

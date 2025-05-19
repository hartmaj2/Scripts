from pysat.formula import CNF
from pysat.solvers import Solver


# create a satisfiable CNF formula "(-x1 ∨ x2) ∧ (-x1 ∨ -x2)":
cnf = CNF(from_clauses=[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]])

# create a SAT solver for this formula:
with Solver(bootstrap_with=cnf) as solver:
    # 1.1 call the solver for this formula:
    print('formula is', f'{"s" if solver.solve() else "uns"}atisfiable')

    # 1.2 the formula is satisfiable and so has a model:
    print('and the model is:', solver.get_model())

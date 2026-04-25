"""2変数の連立一次方程式を Pyomo で解く。

  x + y  = 3
  2x - y = 0
"""

import pyomo.environ as pyo

model = pyo.ConcreteModel()

model.x = pyo.Var(domain=pyo.Reals)
model.y = pyo.Var(domain=pyo.Reals)

model.eq1 = pyo.Constraint(expr=model.x + model.y == 3)
model.eq2 = pyo.Constraint(expr=2 * model.x - model.y == 0)

model.obj = pyo.Objective(expr=0.0)

solver = pyo.SolverFactory("appsi_highs")
result = solver.solve(model)

print(f"termination: {result.solver.termination_condition}")
print(f"x = {pyo.value(model.x)}")
print(f"y = {pyo.value(model.y)}")

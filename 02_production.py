"""2製品の生産計画問題 (LP) を Pyomo で解く。

ある工場で 2 つの製品 A, B を生産する。
製品 1 個あたりの所要時間と利益、各機械の利用可能時間は以下:

                 製品A   製品B   利用可能時間
  機械1 [h/個]    1       2       8
  機械2 [h/個]    2       1       8
  利益  [円/個]   3       5

利益を最大化する生産量 x (A の個数), y (B の個数) を求める。

  max  3x + 5y
  s.t. x + 2y <= 8
       2x + y <= 8
       x, y >= 0
"""

import pyomo.environ as pyo

model = pyo.ConcreteModel()

model.x = pyo.Var(domain=pyo.NonNegativeReals)
model.y = pyo.Var(domain=pyo.NonNegativeReals)

model.profit = pyo.Objective(expr=3 * model.x + 5 * model.y, sense=pyo.maximize)

model.machine1 = pyo.Constraint(expr=model.x + 2 * model.y <= 8)
model.machine2 = pyo.Constraint(expr=2 * model.x + model.y <= 8)

solver = pyo.SolverFactory("appsi_highs")
result = solver.solve(model)

print(f"termination: {result.solver.termination_condition}")
print(f"x (製品A) = {pyo.value(model.x):.4f}")
print(f"y (製品B) = {pyo.value(model.y):.4f}")
print(f"利益       = {pyo.value(model.profit):.4f}")

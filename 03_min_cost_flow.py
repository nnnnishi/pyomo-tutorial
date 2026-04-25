"""最小費用流問題 (Minimum Cost Flow) を Pyomo で解く。

有向グラフ G = (N, A) 上で、各ノード i に供給/需要 b[i] (正=供給, 負=需要, 0=中継)、
各辺 (i,j) にコスト c[i,j] と容量 u[i,j] が与えられたとき、

  min  Σ c[i,j] * x[i,j]
  s.t. Σ_{j: (i,j)∈A} x[i,j] − Σ_{j: (j,i)∈A} x[j,i] = b[i]   ∀ i ∈ N
       0 ≤ x[i,j] ≤ u[i,j]                                    ∀ (i,j) ∈ A

を満たす流量 x を求める。

例題:

  ノード 1 (供給 +20) → ノード 4 (需要 -20)
  ノード 2, 3 は中継 (b=0)

  辺          cost   capacity
  (1, 2)       4       15
  (1, 3)       4        8
  (2, 3)       2       20
  (2, 4)       6        8
  (3, 4)       1       15
"""

import pyomo.environ as pyo

# --- データ ---
nodes = [1, 2, 3, 4]
arcs = [(1, 2), (1, 3), (2, 3), (2, 4), (3, 4)]
supply = {1: 20, 2: 0, 3: 0, 4: -20}
cost = {(1, 2): 4, (1, 3): 4, (2, 3): 2, (2, 4): 6, (3, 4): 1}
capacity = {(1, 2): 15, (1, 3): 8, (2, 3): 20, (2, 4): 8, (3, 4): 15}

# --- モデル ---
m = pyo.ConcreteModel()

m.N = pyo.Set(initialize=nodes)
m.A = pyo.Set(initialize=arcs, dimen=2)

m.b = pyo.Param(m.N, initialize=supply)
m.c = pyo.Param(m.A, initialize=cost)
m.u = pyo.Param(m.A, initialize=capacity)

m.x = pyo.Var(m.A, domain=pyo.NonNegativeReals)


def capacity_rule(m, i, j):
    return m.x[i, j] <= m.u[i, j]


m.cap_con = pyo.Constraint(m.A, rule=capacity_rule)


def flow_balance_rule(m, i):
    out_flow = sum(m.x[i, j] for (ii, j) in m.A if ii == i)
    in_flow = sum(m.x[j, i] for (j, ii) in m.A if ii == i)
    return out_flow - in_flow == m.b[i]


m.balance_con = pyo.Constraint(m.N, rule=flow_balance_rule)

m.obj = pyo.Objective(
    expr=sum(m.c[i, j] * m.x[i, j] for (i, j) in m.A),
    sense=pyo.minimize,
)

# --- 求解 ---
solver = pyo.SolverFactory("appsi_highs")
result = solver.solve(m)

print(f"termination: {result.solver.termination_condition}")
print(f"total cost : {pyo.value(m.obj):.2f}")
print("flows:")
for i, j in arcs:
    flow = pyo.value(m.x[i, j])
    if flow > 1e-9:
        print(f"  {i} -> {j} : {flow:6.2f}  (cap {capacity[i, j]}, cost {cost[i, j]})")

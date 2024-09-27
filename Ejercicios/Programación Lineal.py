import pulp

lp_problem = pulp.LpProblem("Problema Buses", pulp.LpMinimize)

# Variables
x1 = pulp.LpVariable('x1', lowBound=0, cat='Integer')
x2 = pulp.LpVariable('x2', lowBound=0, cat='Integer')
x3 = pulp.LpVariable('x3', lowBound=0, cat='Integer')
x4 = pulp.LpVariable('x4', lowBound=0, cat='Integer')
x5 = pulp.LpVariable('x5', lowBound=0, cat='Integer')
x6 = pulp.LpVariable('x6', lowBound=0, cat='Integer')

# Función objetivo
lp_problem += x1 + x2 + x3 + x4 + x5 + x6

# Restricciones
lp_problem += x1 + x2 >= 8, "R1"
lp_problem += x2 + x3 >= 10, "R2"
lp_problem += x3 + x4 >= 7, "R3"
lp_problem += x4 + x5 >= 12, "R4"
lp_problem += x5 + x6 >= 4, "R5"
lp_problem += x6 + x1 >= 4, "R6"

# Solucion
lp_problem.solve()

# Resultados
for variable in lp_problem.variables():
    print("{} = {}".format(variable.name, variable.varValue))
print(f"\nEl número mínimo de autobuses es {lp_problem.objective.value()}")

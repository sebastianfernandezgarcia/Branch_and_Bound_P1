# Search methods

import search

ab = search.GPSProblem('A', 'B'
                       , search.romania)
ch = search.GPSProblem('C', 'H'
                       , search.romania)
ar = search.GPSProblem('A', 'R'
                       , search.romania)
du = search.GPSProblem('D', 'U'
                       , search.romania)
ep = search.GPSProblem('E', 'P'
                       , search.romania)

#print(search.breadth_first_graph_search(ab).path() + " : " + print(search.breadth_first_graph_search(ab).total_path_cost()))
#print(search.depth_first_graph_search(ab).path())
print("------------------------Del nodo A al B-------------------------")
print("B&B base->           ", search.branch_and_bound_graph_search(ab).path())
print("B&B con heurística-> ", search.branch_and_bound_heuristic_search(ab).path())

print("\n------------------------Del nodo C al H-------------------------")
print("B&B base->           ", search.branch_and_bound_graph_search(ch).path())
print("B&B con heurística-> ", search.branch_and_bound_heuristic_search(ch).path())

print("\n------------------------Del nodo A al R-------------------------")
print("B&B base->           ", search.branch_and_bound_graph_search(ar).path())
print("B&B con heurística-> ", search.branch_and_bound_heuristic_search(ar).path())

print("\n------------------------Del nodo D al U-------------------------")
print("B&B base->           ", search.branch_and_bound_graph_search(du).path())
print("B&B con heurística-> ", search.branch_and_bound_heuristic_search(du).path())

print("\n------------------------Del nodo E al P-------------------------")
print("B&B base->           ", search.branch_and_bound_graph_search(ep).path())
print("B&B con heurística-> ", search.branch_and_bound_heuristic_search(ep).path())

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450

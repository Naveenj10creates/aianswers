import networkx as nx
import matplotlib.pyplot as plt

# (i) Given dataset (Adjacency List Representation)
department_hierarchy_graph = {
    "Director": ["Finance", "Technology", "Operations"],
    "Finance": ["Budgeting", "Accounting"],
    "Technology": ["Software", "Hardware", "Cybersecurity"],
    "Operations": ["Logistics", "Procurement"],
    "Budgeting": ["Planning", "Audit"],
    "Accounting": [],
    "Software": ["AI Lab", "Web Development"],
    "Cybersecurity": [],
    "Hardware": ["R&D"],
    "Logistics": ["Domestic", "International"],
    "Procurement": ["Vendors"],
    "Planning": [],
    "Audit": [],
    "AI Lab": [],
    "Web Development": [],
    "R&D": [],
    "Domestic": [],
    "International": [],
    "Vendors": []
}

# (ii) DFS Function
def dfs_path(graph, start, goal, path=None):
    if path is None:
        path = []
    path = path + [start]
    if start == goal:
        return path
    if start not in graph:
        return None
    for node in graph[start]:
        if node not in path:
            newpath = dfs_path(graph, node, goal, path)
            if newpath:
                return newpath
    return None

# Example usage:
start_dept = "Director"
target_dept = "R&D"

dfs_result = dfs_path(department_hierarchy_graph, start_dept, target_dept)
print("DFS Path from", start_dept, "to", target_dept, ":", dfs_result)

# (iii) Visualize the Graph
G = nx.DiGraph()

for dept, subdepts in department_hierarchy_graph.items():
    for sub in subdepts:
        G.add_edge(dept, sub)

pos = nx.spring_layout(G, seed=42)

# Draw the full hierarchy
plt.figure(figsize=(10, 8))
nx.draw(G, pos, with_labels=True, node_color="lightblue", node_size=2000, font_size=9, font_weight='bold', arrows=True)

# Highlight the DFS path
if dfs_result:
    path_edges = list(zip(dfs_result, dfs_result[1:]))
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=3)
    nx.draw_networkx_nodes(G, pos, nodelist=dfs_result, node_color='orange')

plt.title(f"Department Hierarchy and DFS Path ({start_dept} → {target_dept})", fontsize=12)
plt.show()

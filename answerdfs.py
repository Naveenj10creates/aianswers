# BFS CODE
G = nx.Graph({
    "Research": ["Development", "Analytics", "Innovation"],
    "Development": ["Research", "Quality Assurance", "IT Support"],
    "Analytics": ["Research", "Marketing", "Finance"],
    "Innovation": ["Research", "Design", "Strategy"],
    "Quality Assurance": ["Development", "Production"],
    "IT Support": ["Development", "HR", "Logistics"],
    "Finance": ["Analytics", "Procurement"],
    "Marketing": ["Analytics", "Sales", "Design"],
    "Design": ["Innovation", "Marketing"],
    "Strategy": ["Innovation", "Procurement"],
    "Procurement": ["Finance", "Strategy", "Logistics"],
    "Production": ["Quality Assurance", "Logistics"],
    "HR": ["IT Support", "Admin"],
    "Admin": ["HR", "Logistics"],
    "Logistics": ["IT Support", "Procurement", "Production", "Admin"],
    "Sales": ["Marketing", "Customer Support"],
    "Customer Support": ["Sales"]
})
start = "Research"
end = "Customer Support"
path = nx.shortest_path(G, source=start, target=end)
print("Shortest collaboration path:")
print(" -> ".join(path))
pos = nx.spring_layout(G, seed=42)
plt.figure(figsize=(10, 8))
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_weight='bold')
nx.draw_networkx_nodes(G, pos, nodelist=path, node_color='orange')
nx.draw_networkx_edges(G, pos, edgelist=list(zip(path, path[1:])), edge_color='red', width=2)
plt.title("Department Collaboration Network")
plt.show()
























# DFS CODE
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






# UFS CODE
import networkx as nx
import matplotlib.pyplot as plt

# Your original graph definition (unweighted, so cost = 1 for all edges)
G = nx.Graph({
    "Research": ["Development", "Analytics", "Innovation"],
    "Development": ["Research", "Quality Assurance", "IT Support"],
    "Analytics": ["Research", "Marketing", "Finance"],
    "Innovation": ["Research", "Design", "Strategy"],
    "Quality Assurance": ["Development", "Production"],
    "IT Support": ["Development", "HR", "Logistics"],
    "Finance": ["Analytics", "Procurement"],
    "Marketing": ["Analytics", "Sales", "Design"],
    "Design": ["Innovation", "Marketing"],
    "Strategy": ["Innovation", "Procurement"],
    "Procurement": ["Finance", "Strategy", "Logistics"],
    "Production": ["Quality Assurance", "Logistics"],
    "HR": ["IT Support", "Admin"],
    "Admin": ["HR", "Logistics"],
    "Logistics": ["IT Support", "Procurement", "Production", "Admin"],
    "Sales": ["Marketing", "Customer Support"],
    "Customer Support": ["Sales"]
})

start_node = "Research"
goal_node = "Customer Support" # Define a target/goal node for the search

# Find the shortest path (UCS with cost 1 per edge)
try:
    ucs_path = nx.shortest_path(G, source=start_node, target=goal_node)
    ucs_path_length = nx.shortest_path_length(G, source=start_node, target=goal_node)
except nx.NetworkXNoPath:
    ucs_path = []
    ucs_path_length = 0

print(f"Start Node: {start_node}")
print(f"Goal Node: {goal_node}")
print("Uniform Cost Search (Shortest Path) Result:")
print(f"Path: {' -> '.join(ucs_path)}")
print(f"Cost (Length): {ucs_path_length}")

# --- Visualization for UCS/Shortest Path ---
pos = nx.spring_layout(G, seed=42)
plt.figure(figsize=(10, 8))

# Draw the full graph
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_weight='bold', edge_color='gray')

# Highlight the path nodes and edges
if ucs_path:
    # Highlight path nodes in orange
    nx.draw_networkx_nodes(G, pos, nodelist=ucs_path, node_color='orange', node_size=2000)
    
    # Highlight path edges in red
    path_edges = list(zip(ucs_path, ucs_path[1:]))
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=3)

plt.title(f"Uniform Cost Search (Shortest Path) from {start_node} to {goal_node}")
plt.show()





















##
'''
% ----- Rules ----- prolog something 

hobby(Person, Activity) :- likes(Person, Activity), leisure(Activity).
works(Person, Company) :- employed(Person, Company), has_skill(Person, Skill), requires(Company, Skill).
knows(Person1, Person2) :- interacted_professionally(Person1, Person2).
knows(Person1, Person2) :- interacted_socially(Person1, Person2).
plays(Person, Sport) :- participates(Person, Sport).
parent(Person1, Person2) :- biological_parent(Person1, Person2).
parent(Person1, Person2) :- legal_parent(Person1, Person2).
mentors(Person1, Person2) :- works(Person1, Company), works(Person2, Company), professional_relation(Person1, Person2).
manages(Person, Team) :- works(Person, Company), leadership_role(Person, Team).

% ----- Facts -----

employed(alice, alphatech).
employed(bob, alphatech).
employed(charlie, betatech).
employed(dana, betatech).

has_skill(alice, programming).
has_skill(bob, management).
has_skill(charlie, research).
has_skill(dana, swimming).

requires(alphatech, programming).
requires(alphatech, management).
requires(betatech, research).
requires(betatech, swimming).

leisure(swimming).
leisure(painting).
leisure(tennis).
leisure(football).

likes(alice, tennis).
likes(bob, painting).
likes(charlie, swimming).
likes(dana, swimming).

participates(alice, tennis).
participates(charlie, football).

biological_parent(alice, charlie).
biological_parent(bob, charlie).

interacted_professionally(alice, bob).
interacted_socially(alice, charlie).
interacted_professionally(bob, dana).

% ----- Example Queries -----

% (a)
% ?- likes(Person, swimming), works(Person, alphatech).

% (b)
% ?- works(Person, Company), works(alice, Company), plays(Person, tennis).

% (c)
% ?- parent(AliceOrBob, Child), (AliceOrBob = alice; AliceOrBob = bob).

% (d)
% ?- likes(bob, Hobby), likes(Person, Hobby), Person \= bob.

% (e)
% ?- knows(Person, alice), knows(Person, charlie).
'''





''' WUMPUS PROBlEM
# wumpus code
grid_size(4,4).

pit(3, 3).
pit(1, 3).
pit(4, 4).
wumpus(1, 3).
gold(2, 3).

agent(1, 1).

:- dynamic(agent/2).
:- dynamic(wumpus/2).
:- dynamic(gold/2).


% ===================================================================
% PART 2: SENSE RULES (How the Agent Perceives the World)
% ===================================================================

% A square (X,Y) has a breeze if a pit (A,B) is adjacent to it.
breeze(X,Y) :-
    pit(A,B),
    adjacent((A,B), (X,Y)).

% A square (X,Y) has a stench if a wumpus (A,B) is adjacent to it.
stench(X,Y) :-
    wumpus(A,B),
    adjacent((A,B), (X,Y)).

% A square (X,Y) has a glitter if the gold is on that same square.
glitter(X,Y) :-
    gold(X,Y).


% ===================================================================
% PART 3: HELPER RULE (Adjacency Logic)
% ===================================================================

% Defines what it means for two squares to be adjacent (no diagonals).
% (X2,Y2) is adjacent to (X1,Y1) if:
adjacent((X1,Y1), (X2,Y2)) :-
    (X2 is X1 + 1, Y2 is Y1);  % One step right
    (X2 is X1 - 1, Y2 is Y1);  % One step left
    (X2 is X1, Y2 is Y1 + 1);  % One step up
    (X2 is X1, Y2 is Y1 - 1).  % One step down


% ===================================================================
% PART 4: ACTION RULES (How the Agent Interacts with the World)
% ===================================================================

% move(X,Y): Moves the agent to a new, adjacent, safe square.
move(X,Y) :-
    agent(A,B),             % 1. Get current agent location (A,B)
    adjacent((A,B),(X,Y)),  % 2. Check if new location (X,Y) is adjacent
    \+ pit(X,Y),            % 3. Check if there is NOT a pit at (X,Y)
    \+ wumpus(X,Y),         % 4. Check if there is NOT a wumpus at (X,Y)
    
    % If all checks pass, update the agent's position:
    retract(agent(A,B)),    % 5. Remove the old fact
    assert(agent(X,Y)),     % 6. Add the new fact
    
    write('Agent moved to '), write((X,Y)), nl. % 7. Print confirmation

% grab_gold: Picks up the gold if on the same square.
grab_gold :-
    agent(X,Y),             % 1. Get current agent location
    gold(X,Y),              
    write('*** Gold grabbed at '), write((X,Y)), write('! ***'), nl,
    retract(gold(X,Y)).    

% shoot: Kills the wumpus if it is in an adjacent square.
% (Note: This simple version assumes only one wumpus)
shoot :-
    agent(X,Y),                                 % 1. Get current agent location
    adjacent((X,Y),(WumpusX,WumpusY)),          % 2. Find an adjacent square (WumpusX, WumpusY)
    wumpus(WumpusX,WumpusY),                    % 3. Check if the wumpus is actually there
    write('>>> Wumpus shot at '), write((WumpusX,WumpusY)), write('! <<<'), nl,
    retract(wumpus(WumpusX,WumpusY)).            % 4. Remove the wumpus from the world

'''




''' classic bfs 
import networkx as nx
import matplotlib.pyplot as plt
import queue
import time


# -----------------------------
# Part 1: BFS Algorithm (Logic)
# -----------------------------
def bfs(graph, start):
    visited = set()
    q = queue.Queue()
    q.put(start)
    bfs_order = []
    edges_traversed = []

    while not q.empty():
        node = q.get()
        if node not in visited:
            visited.add(node)
            bfs_order.append(node)
            for neighbor in graph.neighbors(node):
                if neighbor not in visited:
                    q.put(neighbor)
                    edges_traversed.append((node, neighbor))
    return bfs_order, edges_traversed


# --------------------------------------
# Part 2: Visualization (Separate Logic)
# --------------------------------------
def visualize_bfs(graph, bfs_order, edges_traversed):
    pos = nx.spring_layout(graph, seed=42)
    node_colors = {node: 'red' for node in graph.nodes()}  # initially all red

    plt.ion()
    for node in bfs_order:
        # mark node as visited
        node_colors[node] = 'green'

        plt.clf()
        nx.draw(
            graph,
            pos,
            with_labels=True,
            node_color=[node_colors[n] for n in graph.nodes()],
            node_size=800,
            font_size=14,
            font_weight='bold'
        )
        plt.title(f"Visited: {node}")
        plt.draw()
        plt.pause(0.1)
        time.sleep(0.8)

        # highlight edges as explored
        for edge in edges_traversed:
            if edge[0] == node:
                plt.clf()
                nx.draw(
                    graph,
                    pos,
                    with_labels=True,
                    node_color=[node_colors[n] for n in graph.nodes()],
                    edgelist=[edge],
                    edge_color='blue',
                    width=3,
                    node_size=800,
                    font_size=14,
                    font_weight='bold'
                )
                plt.title(f"Exploring edge: {edge[0]} → {edge[1]}")
                plt.draw()
                plt.pause(0.1)
                time.sleep(0.8)

    plt.ioff()
    plt.show()


# -----------------------------
# Run BFS + Visualization
# -----------------------------
G = nx.Graph()
edges = [
    ('A', 'B'), ('A', 'C'),
    ('B', 'D'), ('B', 'E'),
    ('C', 'F'), ('E', 'F'),
    ('F', 'G')
]
G.add_edges_from(edges)

start_node = 'A'
bfs_order, edges_traversed = bfs(G, start_node)

print("\n✅ BFS Traversal Path:", " → ".join(bfs_order))

visualize_bfs(G, bfs_order, edges_traversed)


'''

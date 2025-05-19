# This program generates a CNF formula in set form so it is possible to use in pysat solver
# It generates the formula from a graph and the formula encodes whether a coloring of the graph exists

def encode_each_node_needs_some_color(n,k,file,mapping):
    for i in range(n):
        file.write("[")
        for j in range(k):
            number_to_map_to = i * k + j + 1
            proposition_string = f"{str(i+1)} {str(j+1)}"
            mapping[proposition_string] = number_to_map_to
            file.write(str(number_to_map_to))
            if j != k-1:
                file.write(",")
        file.write("]")
        if i != n-1:
            file.write(",")

def encode_each_edge_needs_different_colors(edges,k,file,mapping):
    for e in range(len(edges)):
        for i in range(k):
            a = mapping[f"{edges[e][0]} {i+1}"]
            b = mapping[f"{edges[e][1]} {i+1}"]
            file.write(f"[-{a},-{b}]")
            if i != k-1:
                file.write(",")
        if e != len(edges) - 1:
            file.write(",")

def write_mapping_to_file(mapping):
    with open('mapping.out', 'w') as file:
        for key in mapping.keys():
            x_num,b_num = key.split()
            file.write(f"x{x_num}b{b_num} -> {mapping[key]}\n")

mapping = dict()
n = 0
k = 0
edges = []
with open('graph2.in', 'r') as file:
    first_line = file.readline().split()
    n = int(first_line[1])
    second_line = file.readline().split()
    k = int(second_line[1])
    for line in file:
        a,b = [int(x) for x in line.split()]
        edges.append([a,b])

print(f"{n} nodes, {k} colors, {len(edges)} edges: {edges}")

with open('encoded_graph.out', 'w') as file:
    encode_each_node_needs_some_color(n,k,file,mapping)
    file.write(",")
    encode_each_edge_needs_different_colors(edges,k,file,mapping)
    write_mapping_to_file(mapping)

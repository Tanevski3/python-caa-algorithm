import matplotlib.pyplot as plt
import networkx as nx
from graph import Graph

print("Welcome to CAA!- You are a lion trying to escape the jungle maze...")

def convert_to_networkx_graph(graph):
    """

    :rtype: object
    """
    G = nx.Graph(name = "CAA implementation")
    for n in graph.get_graph():
        G.add_node(n.get_name())

    for key, values in graph.get_graph().items():
        for v in values:
            G.add_edge(key.get_name(), v.get_name())
    return G


while True:

    # full_name = input("Enter your name king: ")
    # if not full_name:
    #     continue

    # print("Let the games begin `" + full_name + "`")

    maze = [[0, 0, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 1],
            [0, 0, 0, 1, 0, 0],
            [0, 1, 1, 0, 0, 1],
            [0, 1, 0, 0, 1, 0],
            [0, 1, 0, 0, 0, 2]]

    dict = {
        'A': ['B', 'F'],
        'B': ['C'],
        'C': ['D', 'H'],
        'D': ['E'],
        'E': ['J'],
        'F': ['G', 'K'],
        'G': ['L'],
        'H': ['I'],
        'I': ['N', 'J'],
        'J': ['K'],
        'K': ['L','P'],
        'L': ['M'],
        'M': ['R'],
        'N': ['S', 'O'],
        'O': ['P'],
        'P': ['Q'],
        'Q': ['R'],
        'R': ['S'],
        'S': ['T'],
        'T': []

    }

    g = Graph(dict, start='A', directed=False, whos_happy=['O'], whos_sad=['J', 'H', 'T'])

    print("W connected to N: " + str(g.is_connected('W', 'N')))

    print("A connected to B: " + str(g.is_connected('A', 'B')))

    print("Path from 'A' to 'B': " + str(g.find_path('A', 'B')))

    print("Path from 'A' to 'D': " + str(g.find_path('A', 'D')))

    print("Path from 'A' to 'E': " + str(g.find_path('A', 'E')))

    print("Path from 'A' to 'T': " + str(g.find_path('A', 'T')))

    print("You start at: " + str(g.current()))
    print("Next: " + str(g.next()))
    print("Previous: " + str(g.previous()))
    print("Go to: " + str(g.go_to('B')))
    print("Current: " + str(g.current()))
    print("Next: " + str(g.next()))
    print("Previous: " + str(g.previous()))
    print("Go to: " + str(g.go_to('C')))
    print("Current: " + str(g.current()))
    print("Next: " + str(g.next()))
    print("Previous: " + str(g.previous()))
    print("Go to: " + str(g.go_to('B')))
    print("Current: " + str(g.current()))
    print("Next: " + str(g.next()))
    print("Previous: " + str(g.previous()))

    print("Output: " + g.__str__())

    visual_graph = convert_to_networkx_graph(g)
    pos=nx.spring_layout(visual_graph,iterations=100)

    filename = nx.draw(visual_graph, pos, with_labels=True, node_size=500, font_size=16)
    plt.show()
    exit(1)
from graph import Node
from graph import Graph

print("Welcome to CAA!- You are a lion trying to escape the jungle maze...")

while True:

    # full_name = input("Enter your name king: ")
    # if not full_name:
    #     continue
    #
    # print("Let the games begin `" + full_name + "`")

    maze = [[0, 0, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 1],
            [0, 0, 0, 1, 0, 0],
            [0, 1, 1, 0, 0, 1],
            [0, 1, 0, 0, 1, 0],
            [0, 1, 0, 0, 0, 2]]

    happy = ['O']
    sad = ['J', 'H', 'T']
    g = Graph([('A', 'B'), ('A', 'F'), ('B', 'C'), ('C', 'D'), ('C', 'H'), ('D', 'E'), ('C', 'H'), ('E', 'J'),
               ('F', 'G'), ('F', 'K'), ('G', 'L'), ('H', 'I'), ('I', 'N'), ('I', 'J'),
               ('K', 'L'), ('K', 'P'), ('L', 'M'), ('M', 'R'), ('N', 'S'), ('N', 'O'),
               ('P', 'Q'), ('R', 'S'), ('S', 'T')], start='A', directed=False, whos_happy=happy, whos_sad=sad)
    #
    # print("W connected to N: " + str(g.is_connected('W', 'N')))
    #
    # print("A connected to B: " + str(g.is_connected('A', 'B')))
    #
    # print("Path from 'A' to 'B': " + str(g.find_path('A', 'B')))
    #
    # print("Path from 'A' to 'D': " + str(g.find_path('A', 'D')))
    #
    # print("Path from 'A' to 'E': " + str(g.find_path('A', 'E')))
    #
    #
    # print("Path from 'A' to 'T': " + str(g.find_path('A', 'T')))

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

    print("Output: "+ g.__str__())

    exit(1)
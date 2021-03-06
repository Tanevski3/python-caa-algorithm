import random

class Node:
    def __init__(self, name= "?", happy=None, start=None):
        self.__name = name
        self.__happy = happy
        self.__start = start

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_happy(self):
        return self.__happy

    def set_happy(self, happy):
        self.__happy = happy

    def get_start(self):
        return self.__start

    def set_start(self, start):
        self.__start = start

    def __str__(self):
        return self.__name

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        """Override the default Equals behavior"""
        if isinstance(other, self.__class__):
            return self.__name == other.__name
        return NotImplemented

    def __ne__(self, other):
        """Define a non-equality python-caa-algorithm"""
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    def __hash__(self) -> int:
        return hash(self.__name)

class Connection:
    def __init__(self, node1, node2, weight=0):
        self.__f = node1
        self.__t = node2
        self.__weight = weight


    def get_weight(self):
        return self.__weight

    def inc_weight(self):
        self.__weight = self.__weight + 1

    def f(self):
        return self.__f

    def t(self):
        return self.__t

    def has_node(self, node):
        return self.__f == node or self.__t == node

    def __str__(self):
        return '{' + self.__f.name + "->" + self.__t.name + '}' + str(self.__weight)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        """Override the default Equals behavior"""
        if isinstance(other, self.__class__):
            return self.__f == other.__f and self.__t == other.__t
        return NotImplemented

    def __ne__(self, other):
        """Define a non-equality python-caa-algorithm"""
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    def __hash__(self) -> int:
        return hash(self.__f.name) + hash(self.__t.name)

class CaaLgorithmIterator:

    def __init__(self, graph, start):
        self._graph = graph
        self._current = Node(start)
        self._history = []
        self._history.add(self._current.clone())

    public
    List < Node > adjacent()
    {
    return this.graph.getAdjacentNodes(this.current.getName());
    }

    public
    Node
    current()
    {
    return this.current;

}

public
List < Node > history()
{
return this.history;
}

public
Node
last()
{
return this.history.get(this.history.size() - 1);
}

@Override


public
boolean
hasNext()
{
return !this.current.isHappy();
}

@Override


public
Node
next()
{
this.applyAlgorithm();
return this.current;
}

private
void
applyAlgorithm()
{
if (!this.hasNext()) {
System.out.println("Already REACHED happy node. No more iterations");
return;
}

List < Connection < Node >> adjacent = this.graph.getAdjacent(this.current.getName());
Optional < Connection < Node >> pickedConnection = adjacent.stream().min((con1, con2) -> {
if (!con1.getWeight().equals(con2.getWeight())) {
return con1.getWeight() - con2.getWeight();
} else {
boolean
pickFirst = random.nextBoolean();
return pickFirst ? 0: -1;
}
});

this.history.add(this.current.clone());
this.current = pickedConnection.orElse(new
Connection <> (this.current, this.current)).to();
if (!this.hasNext()) {
    this.history.add(this.current.clone());
}
this.graph.incWeight(this.last(), this.current);
}


class Graph:
    """ Graph data structure, undirected by default. """

    def __init__(self, nodes_and_connections, start=None, bidirectional=True, whos_happy=[], whos_sad=[]):
        self._nodes = []
        self._connections = []
        self._bidirectional = bidirectional
        self._whos_happy = whos_happy
        self._whos_sad = whos_sad
        self._create_all_nodes(nodes_and_connections, start, self._whos_happy, self._whos_sad)
        self._connect_all_nodes(nodes_and_connections)
        self._current = self.__get_node(start)
        self._previous = self.__get_node(start)
        self._iterator = CaaLgorithmIterator(self, start);

    def current(self):
        return self._current

    def previous(self):
        return self._previous

    def next(self):
        return self._graph[self._current]

    def go_to(self, node_name):
        previous_node = self._current
        next_node = self.__get_node(node_name)
        # nodes = self.__get_node_appearances(previous_node)
        # [n.inc_weight() for n in nodes]
        self._previous = previous_node
        next_node.inc_weight()
        self._current = next_node
        return self._current

    def __get_node_appearances(self,node):
        nodes = []
        for key, value in self._graph.items():
            if node in self._graph[key]:
                nodes.append(node)

        return nodes

    def __get_node(self,node_name):
        for key in self._graph:
            if key.get_name() == node_name:
                return key

        raise ValueError('No node found for name ' + node_name)

    def _create_all_nodes(self, nodes_and_connections, start, whos_happy=[], whos_sad=[]):

        for key in nodes_and_connections:
            self._create_node(key, start, whos_happy, whos_sad)

    def _create_node(self, node_name, start, whos_happy=[], whos_sad=[]):

        node = Node(node_name)

        if node_name in whos_happy: node.set_happy(True)
        if node_name in whos_sad: node.set_happy(False)
        if node_name == start:
            node.set_start(True)
            node.inc_weight()

        self._graph[node] = []

    def _connect_all_nodes(self, nodes_and_connections):
        """ Add connections (list of tuple pairs) to graph """
        for key, values in nodes_and_connections.items():
            for value in values:
                self._connect_nodes(key, value)
                if not self._directed:
                    self._connect_nodes(value, key)

    def _connect_nodes(self, node1, node2):
        node1 = self.__get_node(node1)
        node2 = self.__get_node(node2)
        self._graph[node1].append(node2)

    def remove(self, node):
        node = Node(node)
        """ Remove all references to node """
        for key, value in self._graph.items():
            try:
                value.remove(node)
            except ValueError:
                pass
        try:
            del self._graph[node]
        except KeyError:
            pass

    def is_connected(self, node1, node2):
        node1 = Node(node1)
        node2 = Node(node2)
        return node1 in self._graph and node2 in self._graph[node1]

    def find_path(self, node1, node2, path=[]):
        """ Find any path between node1 and node2 (may not be shortest) """

        if isinstance(node1, str):
            node1 = Node(node1)
        if isinstance(node2, str):
            node2 = Node(node2)

        path = path + [node1]
        if node1 == node2:
            return path
        if node1 not in self._graph:
            return None
        for node in self._graph[node1]:
            if node not in path:
                new_path = self.find_path(node, node2, path)
                if new_path:
                    return new_path
        return None

    def get_graph(self):
        return self._graph

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, self._graph)


# tests
# g = Graph([('A', 'B'), ('B', 'C'), ('B', 'D'), ('C', 'D'), ('E', 'F'), ('F', 'C')], directed=False)
#
# print(g._graph)
#
# g.add('E', 'D')
#
# print(g._graph)
#
# g.remove('D')
#
# print(g._graph)
#
# print("W connected to N: " + str(g.is_connected('W', 'N')))
#
# print("A connected to B: " + str(g.is_connected('A', 'B')))
#
# g = Graph([('A', 'B'), ('B', 'C'), ('B', 'D'), ('C', 'D'), ('E', 'F'), ('F', 'C')], directed=False)
#
# print("Path from 'A' to 'B': " + str(g.find_path('A', 'B')))
#
# print("Path from 'A' to 'D': " + str(g.find_path('A', 'D')))
#
# print("Path from 'A' to 'E': " + str(g.find_path('A', 'E')))

# x = NodeName('A')
#
# print(x)
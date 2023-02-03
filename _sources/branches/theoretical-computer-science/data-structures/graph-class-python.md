layout: algorithm
categories: branches,theoretical-computer-science, data-structures
nodeid: bookofproofs$244
orderid: 50
parentid: bookofproofs$6217
title: Graph (Python)
description: GRAPH ★ bring your math skills to the graduate level ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: 
keywords: graph,python,class
contributors: bookofproofs


---
If `\(n = |V|\)` is the number of vertices of the initial graph, the running times of the algorithms are the following:


Graph Class Algorithm | Average Case | Worst Case | Remark
:------------- |:------------- |:------------- |:-------------
 Constructor | `\(\mathcal{O(k\cdot n^2)}\)`| `\(\mathcal{O(n^3)}\)`| `\(k=\)` average number of neighbours to be added for all vertices in the graph
 Conversion to String | `\(\mathcal{O(n^2)}\)`| `\(\mathcal{O(n^2)}\)`|
 getVertices| `\(\mathcal{O(1)}\)`| `\(\mathcal{O(1)}\)`|
 listVertexIDs| `\(\mathcal{O(1)}\)`| `\(\mathcal{O(1)}\)`|
 addVertex| `\(\mathcal{O(1)}\)`| `\(\mathcal{O(1)}\)`|
 addVertexByID| `\(\mathcal{O(1)}\)`| `\(\mathcal{O(1)}\)`|
 getVertexByID| `\(\mathcal{O(1)}\)`| `\(\mathcal{O(1)}\)`|
 addNeighboursToVertex| `\(\mathcal{O(k\cdot n^2)}\)`| `\(\mathcal{O(k\cdot n^2)}\)`| `\(k=\)` number of neighbours to be added
 setProperties| `\(\mathcal{O(n)}\)`| `\(\mathcal{O(n)}\)`|
 getOrder| `\(\mathcal{O(1)}\)`| `\(\mathcal{O(1)}\)`|
 getNumbOfEdges| `\(\mathcal{O(n^2)}\)`| `\(\mathcal{O(n^2)}\)`|
 Vertex Class Algorithm| Average Case| Worst Case| Remark
 Constructor | `\(\mathcal{O(1)}\)`| `\(\mathcal{O(1)}\)`|
 getNumbOfNeighbours| `\(\mathcal{O(1)}\)`| `\(\mathcal{O(1)}\)`|
 getDegree| `\(\mathcal{O(n)}\)`| `\(\mathcal{O(n)}\)`|
 getID| `\(\mathcal{O(1)}\)`| `\(\mathcal{O(1)}\)`|
 getProperties| `\(\mathcal{O(1)}\)`| `\(\mathcal{O(1)}\)`|
 setProperties| `\(\mathcal{O(1)}\)`| `\(\mathcal{O(1)}\)`|
 getNeighbours| `\(\mathcal{O(1)}\)`| `\(\mathcal{O(1)}\)`|
 listNeighbourIDs| `\(\mathcal{O(n)}\)`| `\(\mathcal{O(n)}\)`|
 neighbourIndex| `\(\mathcal{O(n)}\)`| `\(\mathcal{O(n)}\)`|
 addNeighbour| `\(\mathcal{O(n)}\)`| `\(\mathcal{O(n)}\)`|
 Neighbour Class Algorithm| Average Case| Worst Case| Remark
 Constructor | `\(\mathcal{O(1)}\)`| `\(\mathcal{O(1)}\)`|
 getNeighboursVertexID| `\(\mathcal{O(1)}\)`| `\(\mathcal{O(1)}\)`|
 getMultiplicity| `\(\mathcal{O(1)}\)`| `\(\mathcal{O(1)}\)`|
 setMultiplicity| `\(\mathcal{O(1)}\)`| `\(\mathcal{O(1)}\)`|
 increaseMultiplicity| `\(\mathcal{O(1)}\)`| `\(\mathcal{O(1)}\)`|
 decreaseMultiplicity| `\(\mathcal{O(1)}\)`| `\(\mathcal{O(1)}\)`|

---

DIRECTED_GRAPH = True  # can be passed in the constructor as the first argument
UNDIRECTED_GRAPH = False  # can be passed in the constructor as the first argument
SIMPLE_GRAPH = True  # can be passed in the constructor as the second argument
MULTI_GRAPH = False  # can be passed in the constructor as the second argument
GRAPH_RAISE_ERRORS = True  # can be passed in the constructor as the third argument
GRAPH_IGNORE_ERRORS = False  # can be passed in the constructor as the third argument


class Graph:
    """ class Graph: Version 1.03, Licence CC BY-SA 4.0 by bookofproofs """
    vertices = None  # implemented as a Python dictionary
    isDirected = False
    isSimple = True
    raisesErrors = False

    def __init__(self, is_directed=False, is_simple=True, raises_errors=False, graph_definition=None):
        self.isDirected = is_directed  # if False, all functions make sure that each edge (a->b)
        # is also contained in the Graph as (b->a)
        self.isSimple = is_simple  # if True, all functions make sure this Graph will have no loops
        # and no multiple edges
        self.raisesErrors = raises_errors  # if True, all functions will raise errors if trying to change
        # the structure of Graph against constraints given by isDirected and isSimple
        self.vertices = {}
        # graph_definition is a python dictionary
        if graph_definition is None:
            graph_definition = {}
        if type(graph_definition) is dict:
            for vertex_id in graph_definition.keys():
                self.add_vertex_by_id(vertex_id)  # register all ids
            for vertex_id, neighbours in graph_definition.items():
                self.add_neighbours_to_vertex(vertex_id, neighbours)  # add all neighbours
        else:
            raise ValueError(
                'if you provide a graph_definition, it must be a dictionary of the form {vertexid1: '
                'listofneibourIDs1, ..., vertextidN:listofneibourIDs}')

    def get_vertices(self):
        """ return vertex dictionary """
        return self.vertices

    def list_vertex_ids(self):
        """ return only a list of vertex IDs"""
        return self.vertices.keys()

    def add_vertex(self, vertex):
        """ adds a Vertex object to this Graph and raises an error if Vertex already exists by id """
        if type(vertex) is Vertex:
            if vertex.get_id() in self.vertices.keys():
                raise RuntimeError(
                    "a Vertex object with the ID " + str(vertex.get_id()) + " already exists in this Graph object")
            else:
                # add vertex only, if it does not exist
                self.vertices[vertex.get_id()] = vertex
        else:
            raise ValueError('Vertex object required')
        return vertex

    def add_vertex_by_id(self, vertex_id):
        """ creates a Vertex with id and properties and adds it to this Graph, raises an error if id already exists"""
        v = Vertex(vertex_id)
        return self.add_vertex(v)

    def get_vertex_by_id(self, vertex_id):
        """ returns the Vertex by vertexid """
        return self.vertices[vertex_id]

    def add_neighbours_to_vertex(self, vertex_id, list_of_neighbour_ids):
        """ adds a list of neighbours to a Vertex by increasing their mulitiplicities """
        if vertex_id in self.vertices.keys():
            for neighbour_id in list_of_neighbour_ids:
                if neighbour_id in self.vertices.keys():
                    # if neighbour to be added to the vertex exists itself as a vertex then
                    # add it to the neighbors if the vertex
                    self.vertices[vertex_id].add_neighbour(self.vertices[neighbour_id], self.isSimple,
                                                           self.raisesErrors)
                    if not self.isDirected:
                        # if this Graph is undirected, then make sure that each edge (a->b) will be also added as (b->a)
                        self.vertices[neighbour_id].add_neighbour(self.vertices[vertex_id], self.isSimple,
                                                                  self.raisesErrors)
                else:
                    if self.raisesErrors:
                        raise IndexError("Cannot add a non-existing vertex " + str(
                            neighbour_id) + " as a neighbour of the vertex " + str(vertex_id))
                    else:
                        # register missing vertices first before adding new neighbours
                        self.add_vertex_by_id(neighbour_id)
                        # now add the neighbor to the neighbors if the vertex
                        self.vertices[vertex_id].add_neighbour(self.vertices[neighbour_id], self.isSimple,
                                                               self.raisesErrors)
                        if not self.isDirected:
                            # if this Graph is undirected, then make sure that each edge
                            # (a->b) will be also added as (b->a)
                            self.vertices[neighbour_id].add_neighbour(self.vertices[vertex_id], self.isSimple,
                                                                      self.raisesErrors)
        else:
            raise IndexError("Vertex " + str(vertex_id) + " does not exist")

    def __str__(self):
        """ generate string representation of Graph
            Each row defines one vertex, its properties (if any) and its neighbours (if any).
            The properties of each vertex are a user-defined dictionary.
            The neighbours of each vertex is a list of strings of the following kind
                vertexid +"(" + multiplicity of vertex +")".
        """

        s = "Graph: isDirected=" + str(self.isDirected) + ", isSimple=" + str(self.isSimple) + "\n"
        for vertexid, vertex in self.vertices.items():
            s += str(vertexid) + ": properties=" + str(self.vertices[vertexid].get_properties()) + ", neighbours=["
            neighbours = vertex.get_neighbours()
            for n in neighbours:
                s += str(n.get_neighbours_vertex_id()) + "(#" + str(n.get_multiplicity()) + "), "
            if len(neighbours) > 0:
                s = s[0:-2] + "]\n"
            else:
                s += "]\n"
        return s[0:-1]

    def set_properties(self, vertex_properties):
        """ set the properties for vertices specified in the dictionary vertex_properties consisting of pairs
        of vertex ids and property dictionaries
        """
        if type(vertex_properties) is dict:
            for vertex_id, props in vertex_properties.items():
                self.vertices[vertex_id].set_properties(props)
        else:
            if self.raisesErrors:
                raise RuntimeError("vertex_properties must be a dictionary")

    def get_order(self):
        """ return the order of this Graph """
        return len(self.vertices)

    def get_numb_of_edges(self):
        numb_of_edges = 0
        for var in self.vertices:
            numb_of_edges += self.vertices[var].get_degree()
        if not self.isDirected:
            numb_of_edges = numb_of_edges // 2
        return numb_of_edges


class Vertex:
    vertex_id = 0  # each vertex has a unique id. The uniqueness will be ensured in the class Graph
    vertex_properties = {}  # each vertex can have a user-defined list of properties
    neighbours = []  # each vertex can have a user-defined list of neighbours

    def __init__(self, vertex_id):
        if type(vertex_id) is int:
            self.vertex_id = vertex_id
            self.neighbours = []
            self.vertex_properties = {}
        else:
            raise ValueError('Vertex id must be an integer')

    def get_numb_of_neighbours(self):
        """ return number of vertex neighbors """
        return len(self.neighbours)

    def get_degree(self):
        """ return the degree of the Vertex """
        deg = 0
        for i in range(0, len(self.neighbours)):
            deg += self.neighbours[i].get_multiplicity()
        return deg

    def get_id(self):
        """ return the id of the vertex """
        return self.vertex_id

    def get_properties(self):
        """ return the properties of the vertex """
        return self.vertex_properties

    def set_properties(self, props):
        if type(props) is dict:
            self.vertex_properties = props
        else:
            raise ValueError('Vertex properties must be a dictionary')

    def get_neighbours(self):
        """ return the list of neighbors of the vertex """
        return self.neighbours

    def list_neighbour_ids(self):
        """ return the list of neighbours of the vertex """
        keys = []
        for i in range(0, len(self.neighbours)):
            keys.append(self.neighbours[i].get_id())
        return keys

    def neighbour_index(self, neighbour_vertex):
        """ returns None, if this vertex does not has v as a neighbour vertex
            otherwise returns the index of the neighbour in the list neighbours
        """
        found = False
        i = 0
        for i, n in enumerate(self.neighbours):
            if n.get_neighbours_vertex_id() == neighbour_vertex.get_id():
                found = True
                break
        if found:
            return i
        else:
            return None

    def add_neighbour(self, neighbour_vertex, is_simple, raise_errors):
        """ adds as new neighbour v to self vertex
            if isSimple = True, then multiplicities will never exceed 1 and no loops will be allowed """
        n = self.neighbour_index(neighbour_vertex)
        if n is not None:
            # if vertex already in neighbours than only increase its multiplicity, unless isSimple=True
            if is_simple and self.neighbours[n].get_multiplicity() >= 1:
                if raise_errors:
                    raise RuntimeError("Cannot add multiple edge " + str(self.get_id()) + "->" + str(
                        neighbour_vertex.get_id()) + " to a simple Graph")
            else:
                self.neighbours[n].increase_multiplicity()
            return self.neighbours[n]  # and return the found neighbour object
        else:
            if is_simple and neighbour_vertex.get_id() == self.get_id():
                if raise_errors:
                    raise RuntimeError("Cannot add loop " + str(neighbour_vertex.get_id()) + " to a simple Graph")
            else:
                neighbour = Neighbour(neighbour_vertex.get_id())  # create a Neighbour object
                self.neighbours.append(neighbour)
                return neighbour  # and return the created neighbour object


class Neighbour:
    """ Neighbour is a class adding the multiplicity functionality to a Vertex """
    vertex_id = None
    multiplicity = 0

    def __init__(self, vertex_id):
        if type(vertex_id) is int:
            self.vertex_id = vertex_id
            self.multiplicity = 1  # equals 1 at minimum. If the neighbour
            # vertex is added multiple times, then only its multiplicity increases
        else:
            raise ValueError('vertex id (int) required to construct a neighbour')

    def get_neighbours_vertex_id(self):
        return self.vertex_id

    def get_multiplicity(self):
        return self.multiplicity

    def set_multiplicity(self, mulitiplicity):
        if mulitiplicity >= 1:
            self.multiplicity = mulitiplicity

    def increase_multiplicity(self):
        self.multiplicity += 1

    def decrease_multiplicity(self):
        if self.multiplicity > 1:
            self.multiplicity -= 1


# creating an undirected simple graph
g = Graph(UNDIRECTED_GRAPH, SIMPLE_GRAPH, GRAPH_RAISE_ERRORS, {0: [1, 2], 1: [^2], 2: []})
print(g)
1. will output
1. Graph: isDirected=False, isSimple=True
1. 0: properties={}, neighbours=[1(#1), 2(#1)]
1. 1: properties={}, neighbours=[0(#1), 2(#1)]
1. 2: properties={}, neighbours=[0(#1), 1(#1)]

# creating a directed simple graph
g = Graph(DIRECTED_GRAPH, SIMPLE_GRAPH, GRAPH_RAISE_ERRORS, {0: [1, 2], 1: [^2], 2: []})
print(g)
1. will output
1. Graph: isDirected=True, isSimple=True
1. 0: properties={}, neighbours=[1(#1), 2(#1)]
1. 1: properties={}, neighbours=[2(#1)]
1. 2: properties={}, neighbours=[]

# creating an undirected multigraph with loops and parallel edges
g = Graph(UNDIRECTED_GRAPH, MULTI_GRAPH, GRAPH_RAISE_ERRORS, {0: [1, 2], 1: [2, 1], 2: [2, 0, 1]})
print(g)
1. will output
1. Graph: isDirected=False, isSimple=False
1. 0: properties={}, neighbours=[1(#1), 2(#2)]
1. 1: properties={}, neighbours=[0(#1), 2(#2), 1(#2)]
1. 2: properties={}, neighbours=[0(#2), 1(#2), 2(#2)]

# creating a directed simple graph with loops, ignoring errors (e.g. ignoring creating loops)
g = Graph(DIRECTED_GRAPH, SIMPLE_GRAPH, GRAPH_IGNORE_ERRORS, {0: [1, 2], 1: [2, 1], 2: [^2]})
print(g)
1. will output
1. Graph: isDirected=True, isSimple=True
1. 0: properties={}, neighbours=[1(#1), 2(#1)]
1. 1: properties={}, neighbours=[2(#1)]
1. 2: properties={}, neighbours=[]

# setting properties of all vertices the existing graph
properties = {0: {"visited": False, "color": "black"}, 1: {"visited": True, "color": "white"},
              2: {"visited": False, "color": "red"}}
g.set_properties(properties)
print(g)
1. will output
1. Graph: isDirected=True, isSimple=True
1. 0: properties={'visited': False, 'color': 'black'}, neighbours=[1(#1), 2(#1)]
1. 1: properties={'visited': True, 'color': 'white'}, neighbours=[2(#1)]
1. 1: properties={'visited': True, 'color': 'white'}, neighbours=[2(#1)]

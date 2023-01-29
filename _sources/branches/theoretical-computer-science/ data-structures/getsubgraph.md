layout: algorithm
categories: branches,theoretical-computer-science, data-structures
nodeid: bookofproofs$6218
orderid: 100
parentid: bookofproofs$6217
title: getSubgraph
description: GETSUBGRAPH &#9733; bring your math skills to the graduate level &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$1591
keywords: getsubgraph
contributors: bookofproofs


---
Making use of the "graph.py module":https://www.bookofproofs.org/branches/graph/, the following algorithm calculates 

* for a given [undirected graph][bookofproofs$523] `\(G(V,E,\gamma)\)` and a given list of vertices `\(v_1,\ldots,v_k\in V\)` the [subgraph induced][bookofproofs$390] by the vertices  `\(G[v_1,\ldots,v_k]\)`, or
* for a given [digraph][bookofproofs$524] `\(D=(V,E,\alpha,\omega)\)` and a given list of vertices `\(v_1,\ldots,v_k\in V\)` the [subdigraph induced][bookofproofs$1171] by the vertices  `\(D[v_1,\ldots,v_k]\)`.

---

from graph import *

def getSubgraph(graph, vertexIDs):
    '''
    Creates a subgraph of graph spanned by the vertices with IDs listed in vertexIDs

    IN: graph=Graph object, vertexIDs=list of vertex IDs (integers)
    OUT: proper subgraph of graph consisting of vertices (new copy Objects will be returned)
    if verticesIDs is not a proper subset of graph.getVertexIDs(), then additional vertices will be added to the subgraph.
    '''

    if not (type(graph) is Graph):
        raise TypeError("g must be a Graph object")
    if not (type(vertexIDs) is list):
        raise TypeError("vertexIDs must be a list of vertex IDs (integers)")

    # the subgraph will gain the same properties as the supergraph
    subgraph = Graph(graph.isDirected, graph.isSimple, graph.raisesErrors)

    # add all vertices to subgraph
    graphvertexIDs = graph.listVertexIDs()
    for vID in vertexIDs:
        vertex = subgraph.addVertexByID(vID)
        if vID in graphvertexIDs:
            # iv vID exists in original graph, copy the properties of the vertex from graph into the subgraph
            vertex.setProperties(graph.getVertexByID(vID).getProperties())

    # create edges of subgraph according to the existing edges in graph
    for vID in vertexIDs:
        currentVertex = subgraph.getVertexByID(vID)
        # check if vID is a vertex of graph
        if vID in graphvertexIDs:
            # if yes, take the list of all neighbours in graph
            neighbours = graph.getVertices()[vID].getNeighbours()
            for n in neighbours:
                # and also check for each neighbour, if it is in the list of vertexIDs of subgraph
                if n.getNeighboursVertexID() in vertexIDs:
                    # if so, create edge in subgraph between vertex vID and neighbour, according to its multiplicitity in graph
                    neighbour = currentVertex.addNeighbour(subgraph.getVertexByID(n.getNeighboursVertexID()), graph.isSimple, graph.raisesErrors)
                    # and correct its multiplicity
                    neighbour.setMultiplicity(n.getMultiplicity())

    return subgraph


1. usage of getSubgraph() :
1. create digraph
graph = Graph(DIRECTEDGRAPH, MULTIGRAPH, GRAPHRAISEERRORS, {1: [2, 4], 2: [^3], 3: [1, 4, 4], 4: [3, 4]})
print(graph)
# create 3 subgraphs of the digraph
subgraph1 = getSubgraph(graph, [1, 2, 3])
subgraph2 = getSubgraph(graph, [3, 4])
subgraph3 = getSubgraph(graph, [1, 3, 4])
print(subgraph1)
print(subgraph2)
print(subgraph3)
''' will output
Graph: isDirected=True, isSimple=False
1: properties={}, neighbours=[2(#1), 4(#1)]
2: properties={}, neighbours=[3(#1)]
3: properties={}, neighbours=[1(#1), 4(#2)]
4: properties={}, neighbours=[3(#1), 4(#1)]
Graph: isDirected=True, isSimple=False
1: properties={}, neighbours=[2(#1)]
2: properties={}, neighbours=[3(#1)]
3: properties={}, neighbours=[1(#1)]
Graph: isDirected=True, isSimple=False
3: properties={}, neighbours=[4(#2)]
4: properties={}, neighbours=[3(#1), 4(#1)]
Graph: isDirected=True, isSimple=False
1: properties={}, neighbours=[4(#1)]
3: properties={}, neighbours=[1(#1), 4(#2)]
4: properties={}, neighbours=[3(#1), 4(#1)]
'''

print()
# create undirected multigraph
graph = Graph(UNDIRECTEDGRAPH, MULTIGRAPH, GRAPHRAISEERRORS, {1: [2, 4], 2: [^3], 3: [1, 4, 4], 4: [3, 4]})
print(graph)
# create 4 subgraphs of the multigraph
subgraph1 = getSubgraph(graph, [1, 2, 3])
subgraph2 = getSubgraph(graph, [3, 4])
subgraph3 = getSubgraph(graph, [3, 4, 5]) # note that intentionally 5 is not a vertex of graph for demo purposes
subgraph4 = getSubgraph(graph, [1, 3, 4])
print(subgraph1)
print(subgraph2)
print(subgraph3)
print(subgraph4)
''' will output
Graph: isDirected=False, isSimple=False
1: properties={}, neighbours=[2(#1), 4(#1), 3(#1)]
2: properties={}, neighbours=[1(#1), 3(#1)]
3: properties={}, neighbours=[2(#1), 1(#1), 4(#3)]
4: properties={}, neighbours=[1(#1), 3(#3), 4(#2)]
Graph: isDirected=False, isSimple=False
1: properties={}, neighbours=[2(#1), 3(#1)]
2: properties={}, neighbours=[1(#1), 3(#1)]
3: properties={}, neighbours=[2(#1), 1(#1)]
Graph: isDirected=False, isSimple=False
3: properties={}, neighbours=[4(#3)]
4: properties={}, neighbours=[3(#3), 4(#2)]
Graph: isDirected=False, isSimple=False
3: properties={}, neighbours=[4(#3)]
4: properties={}, neighbours=[3(#3), 4(#2)]
5: properties={}, neighbours=[]
Graph: isDirected=False, isSimple=False
1: properties={}, neighbours=[4(#1), 3(#1)]
3: properties={}, neighbours=[1(#1), 4(#3)]
4: properties={}, neighbours=[1(#1), 3(#3), 4(#2)]
'''

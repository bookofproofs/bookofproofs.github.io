layout: algorithm
categories: branches,graph-theory
nodeid: bookofproofs$1220
orderid: 700
parentid: bookofproofs$159
title: Get All Components of a Graph
description: GET ALL COMPONENTS OF A GRAPH &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$570
keywords: all,components,get,graph
contributors: bookofproofs

---
Let `\(G(V,E)\)` be a [undirected graph][bookofproofs$523]. Then the following algorithm `get_components(G)` obtains correctly the set of all components of `\(G\)` and its time complexity is `\(\mathcal O(|V|+|E|)\)`.

---
§§§1

---
§§§1
``` { .python linenos=true linenostart=1 }
function get_components(G):
    G.unvisit_all_vertices()

    C=set()  # initiate empty set of all components  
    m=0
    for v in G.V:
        if not v.is_visited():
            m += 1  # increase the component number 
            C = C.union(getCOMPONENT(G,v,m))  # obtain the m-th component and add it as an element of C  
        # at this stage, the 'visited' argument of all vertices of the last component is marked by m. 
    return C # return the set of all components
``` 
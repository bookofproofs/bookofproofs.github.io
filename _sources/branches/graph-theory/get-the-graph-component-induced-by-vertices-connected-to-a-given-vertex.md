layout: algorithm
categories: branches,graph-theory
nodeid: bookofproofs$1216
orderid: 1300
parentid: bookofproofs$159
title: Get the Component Induced by Vertices Connected to a Given Vertex
description: GET THE COMPONENT INDUCED BY VERTICES CONNECTED TO A GIVEN VERTEX &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$570
keywords: component,connected,get,given,graph,induced,vertex,vertices
contributors: bookofproofs

---
Let `\(G(V,E)\)` be a [directed][bookofproofs$524] or [undirected graph][bookofproofs$523] and let `\(f\)` be its [adjacency list representation][bookofproofs$1215]. Let `\(v\in V\)` be one of its vertices and `\(m\in\mathbb N\)`. 

The following algorithm `\(\mathtt{getCOMPONENT(G,v,m)}\)` obtains correctly the [component][bookofproofs$1220] containing `\(v\)`.

The time complexity of the algorithm is `\(\mathcal O (|V|+|E|)\)`.



#### Implementation notes

Please note that the for-next loop in the lines `\(1\)` to `\(3\)` has to be omitted, if the algorithm is used as a subprogram of more general algorithms also making use of the array `visited`, e.g. the algorithm to obtain all components of a graph `get_components(G)`. Otherwise, this loop would destroy the information about visited nodes obtained during the more general algorithm.

---

FOR v_i\in V\setminus\{v\}
visited[v_i]:=NIL; // unmark all other vertices in `\(G\)` (still unvisited)
NEXT
visited[v]:=m; // mark `\(v\)` as visited


L:=(v); // create a list `\(L\)` containing only the vertex `\(v\)`
WHILE L\neq () DO // while L is not empty
u:=L.removeFirst(); // remove the first node from `\(L\)` and denoted it by `\(u\)` 
FOR n\in f(u)// for all successors (neighbors) `\(n\)` of `\(u\)` 
IF visited[n] = NIL THEN // if the neighbor `\(n\)` has not yet been visited
visited[n]:=m; // visit neighbor node
L.append(n); // and append it to the list `\(L\)`
ENDIF
NEXT
ENDWHILE

G':=\emptyset; // create an empty graph
FOR v\in V
IF visited[v]\neq NIL THEN
G':=G' + G[v]; // add all visited vertices to the component `\(G'\)` (including all adjacent edges) 
ENDIF
NEXT

RETURN G';// return component induced by all visited nodes in `\(G\)`.

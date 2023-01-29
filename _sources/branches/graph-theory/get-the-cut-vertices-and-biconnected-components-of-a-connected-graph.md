layout: algorithm
categories: branches,graph-theory
nodeid: bookofproofs$1240
orderid: 1400
parentid: bookofproofs$159
title: Get the Cut Vertices and Biconnected Components of a Connected Graph
description: GET THE CUT VERTICES AND BICONNECTED COMPONENTS OF A CONNECTED GRAPH &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$624
keywords: biconnected,components,connected,cut,get,graph,vertices,biconnected components
contributors: bookofproofs

---
Let `\(G(V,E)\)` be a [connected undirected graph][bookofproofs$1166]. The following algorithm `\(\mathtt{getBICONNECTEDCOMPONENTS(G)}\)` obtains correctly all of its [cutvertices][bookofproofs$1166] and [biconnected components][bookofproofs$1227] in the time complexity `\(\mathcal O(|V|+|E|)\)`.

---

FOR v\in V
visited[v]:=NIL; // unmark all vertices in `\(G\)` 
NEXT

B=\emptyset; // initiate empty set of all biconnected components  
S=\text{empty stack}; // initiate empty stack
enum:=-1; 

FOR v\in V
IF visited[v]=NIL THEN 
CALL \{\mathtt{calculateLowpoint(G,v,B,S,enum)}\}; // print all cutvertices and store biconnected components in `\(B\)`; 
ENDIF
NEXT

RETURN B; // return all found biconnected components

; // Function `\(\mathtt{calculateLowpoint(G,v,B,S,m)}\)` calculates the lowpoint of `\(v\)`.
; // The lowpoint is lowest depth of all descendants of v in the depth-first-search tree  

FUNCTION \mathtt{calculateLowpoint(G,v,B,S,enum)}
enum:=enum+1;
visited[v]:=enum;
numberOfDescendants[v]:=0; // set the number of descendants to 0
lowpoint:=enum;
S.push(v); // put `\(v\)` on a stack
FOR n\in f(v)// for all (neighbors) `\(n\)` of `\(v\)` 
IF visited[n] = NIL THEN // if the neighbor `\(n\)` has not yet been visited

numberOfDescendants[v]:=numberOfDescendants[v]+1; // increase the number of descendants
lowpointneighbor:=\mathtt{calculateLowpoint(G,n,B,S,enum)}; // depth-first search for the next neighbor `\(n\)`

IF lowpointneighbor < lowpoint THEN
lowpoint:=lowpointneighbor;
ENDIF

IF visited[v]==0 THEN
;// special case for root of DFS
;// root is an cutvertex iif there are two or more descendants
IF numberOfDescendants[v]\ge 2 THEN
outputComponent(G,B,S,v); // a new cutvertex `\(v\)` and a new biconnected component found
ENDIF
ELSE
IF (lowpointneighbor \ge visited[v] THEN
outputComponent(G,B,S,v); // a new cutvertex `\(v\)` and a new biconnected component found
ENDIF
ENDIF
ELSE
IF visited[n] < lowpoint THEN
 lowpoint=visited[n]; 
ENDIF
ENDIF
NEXT
RETURN lowpoint;
ENDFUNCTION

; // function `\(\mathtt{outputComponent(G,B,S,v)}\)` prints the cutvertex `\(v\)` 
; // and returns a subgraph of `\(G\)`,
; // which is its biconnected component 
FUNCTION outputComponent(G,B,S,v)
PRINT v; // new cutvertex found
V:=\emptyset; // initiate an empty set of vertices
REPEAT
x:=S.pull(); // pull vertex from stack
V:=V\cup \{x\}; // add vertex to set `\(V\)`
UNTIL x=v; // until the vertex `\(v\)` is reached
B:=B\cup \{G[V]\}; // output the subgraph of `\(G\)` induced by `\(V\)` (=biconnected component of `\(G\)`) 
S.push(v); // put cutvertex `\(v\)` on a stack as part of the next biconnected component 
ENDFUNCTION

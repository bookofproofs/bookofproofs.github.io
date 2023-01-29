layout: definition
categories: branches,graph-theory
nodeid: bookofproofs$1215
orderid: 100
parentid: bookofproofs$471
title: Adjacency List Representation
description: ADJACENCY LIST REPRESENTATION &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$570
keywords: adjacency,adjacency list,list,representation,adjacency list representation,adjacency lists,adjacency list definition,adjacency list in c
contributors: bookofproofs


---


---

The data structure [linked list][bookofproofs$1214] allows another[^1] representation for digraphs or a graphs to be used in computers, which is convenient in cases where the number of edges is not too big (e.g. less then the square of the number of vertices `\(|E| < |V|^2\)`).  

Let `\(D=(V,E,\alpha,\omega)\)` be a [digraph][bookofproofs$524] and let `\(L\)` be the set of all [linked lists][bookofproofs$1214] of vertices in `\(V\)`, i.e. 

`\[L:=\{(n_{i_1},n_{i_2},\ldots),~n_{i_j}\in V\}\]`

An **adjacency list** of `\(D\)` is a [function][bookofproofs$592].
`\[ f:=\cases{
V   \to  L \\
n_i  \to  (n_{i_1},n_{i_2},\ldots)\Longleftrightarrow n_{i_j}\in N^+(n_i),
} \]`

i.e. `\(f\)` assigns to each vertex `\(n_i\)` a list of all of its [adjacent successors][bookofproofs$544]  `\(n_{i_j}\)`, i.e. the edges `\(n_in_{i_j}\)` exist and the vertex `\(n_i\)` is their initial vertex, while the vertices `\(n_{i_j}\)` are their terminal vertices.

The **adjacency list** for an [undirected graph][bookofproofs$523] `\(G=(V,E,\gamma)\)` is defined correspondingly:

`\[ f:=\cases{
V   \to  L \\
n_i  \to  (n_{i_1},n_{i_2},\ldots)\Longleftrightarrow n_{i_j}\in N(n_i),
} \]`

i.e. `\(f\)` assigns to each vertex `\(n_i\)` a list of all of its [neighbors][bookofproofs$525] `\(n_{i_j}\)`, i.e. the edges `\(n_in_{i_j}\)` exist and the vertices `\(n_i\)` and `\(n_{i_j}\)` are adjacent.


#### Examples:


Digraph | Adjacency list
:------------- |:-------------
|
![graphs5](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/examples/graphs5.jpg?raw=true) A digraph `\(D\)` with `\(6\)` vertices and some edges.|`\[

\begin{array}{ccl}
a & \rightarrow & (b,c,d)\cr
b & \rightarrow & (a,a) \cr
c & \rightarrow & (b,b,b) \cr
d & \rightarrow & (e,e) \cr
e & \rightarrow & (e) \cr
f & \rightarrow & () \cr
\end{array}
\]`Please note that in an adjacency list representation of a digraph  
* the order of the successors in each list is irrelevant, all that counts is the number of occurrences of each successor,
* if a vertex is in its own list, this indicates a loop, 
* multiple occurrences of nodes in the list indicate multiple edges,
* empty lists `\(()\)` indicate isolated nodes (like for the node `\(f\)`). |
 Graph| Adjacency list
|
![graphs6](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/examples/graphs6.jpg?raw=true) A graph `\(G\)` with `\(6\)` vertices and some edges.|`\[

\begin{array}{ccl}
a & \rightarrow & (b,b,b,c,d)\cr
b & \rightarrow & (a,a,a,c,c,c) \cr
c & \rightarrow & (a,b,b,b) \cr
d & \rightarrow & (a,e,e) \cr
e & \rightarrow & (d,d,e) \cr
f & \rightarrow & () \cr
\end{array}
\]`Please note that in an adjacency list representation of a digraph  
* the order of the neighbors in each list is irrelevant, all that counts is the number of occurrences of each neighbor,
* if a vertex is in its own list, this indicates a loop, 
* multiple occurrences of nodes in the list indicate multiple edges,
* empty lists `\(()\)` indicate isolated nodes (like for the node `\(f\)`). |

[^1]: see also [adjacency matrix][bookofproofs$1213].
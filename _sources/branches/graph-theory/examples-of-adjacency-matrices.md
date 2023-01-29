layout: example
categories: branches,graph-theory
nodeid: bookofproofs$7975
orderid: 50
parentid: bookofproofs$1213
title: Examples of Adjacency Matrices
description: EXAMPLES OF ADJACENCY MATRICES &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$570
keywords: adjacency,examples,matrices,adjacency matrix example,example of adjacency matrix,adjacency matrix examples,adjacency matrices,what is adjacency matrix with example,what is an adjacency matrix,adjency matrix,adjacency matric,adjacent matrix,adjaceny matrix,adjancency matrix,adjacency matrix,what is adjacency matrix with example?,adjacency matrix gra
contributors: bookofproofs

---


---

### A Digraph Example

The following figure shows a [digraph][bookofproofs$524] `\(D\)` with `\(6\)` vertices and some edges:


![graphs5](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/examples/graphs5.jpg?raw=true)


This digraph has the [adjacency matrix][bookofproofs$1213].
`$$\begin{array}{cccccccc}
&   & a & b & c & d & e & f \cr
&   & \downarrow & \downarrow & \downarrow & \downarrow & \downarrow & \downarrow \cr
a & \rightarrow & 0 & 1 & 1 & 1 & 0 & 0 \cr
b & \rightarrow & 2 & 0 & 0 & 0 & 0 & 0 \cr
c & \rightarrow & 0 & 3 & 0 & 0 & 0 & 0 \cr
d & \rightarrow & 0 & 0 & 0 & 0 & 2 & 0 \cr
e & \rightarrow & 0 & 0 & 0 & 0 & 1 & 0 \cr
f & \rightarrow & 0 & 0 & 0 & 0 & 0 & 0 \cr
\end{array}$$`

Please note that an adjacency matrix of a digraph
* is in general not symmetric,
* diagonal elements `\(\neq 0\)` indicate loops,
* elements of `\( > 1 \)` indicate multiple edges.

### A Graph Example

The figure below demonstrates a similar [graph][bookofproofs$523] with `\(G\)` with `\(6\)` vertices and some edges:


![graphs6](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/examples/graphs6.jpg?raw=true)


The adjacency matrix of this graph is given by

`$$
\begin{array}{cccccccc}
&   & a & b & c & d & e & f \cr
&   & \downarrow & \downarrow & \downarrow & \downarrow & \downarrow & \downarrow \cr
a & \rightarrow & 0 & 3 & 1 & 1 & 0 & 0 \cr
b & \rightarrow & 3 & 0 & 3 & 0 & 0 & 0 \cr
c & \rightarrow & 1 & 3 & 0 & 0 & 0 & 0 \cr
d & \rightarrow & 1 & 0 & 0 & 0 & 2 & 0 \cr
e & \rightarrow & 0 & 0 & 0 & 2 & 1 & 0 \cr
f & \rightarrow & 0 & 0 & 0 & 0 & 0 & 0 \cr
\end{array} $$`


Please note that an adjacency matrix of a graph is
* always symmetric,
* diagonal elements `\(\neq 0\)` indicate loops,
* elements of `\( > 1 \)` indicate multiple edges.

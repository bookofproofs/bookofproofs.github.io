layout: definition
categories: branches,theoretical-computer-science, data-structures
nodeid: bookofproofs$1214
orderid: 50
parentid: bookofproofs$153
title: Linked List, List Nodes
description: LINKED LIST, LIST NODES &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$1086
keywords: linked,linked list,list,list node,nodes,pointer
contributors: bookofproofs

---


---

A **list node** is a [data structure][bookofproofs$106], consisting of two elements:

`\[\mathtt{node}:=\cases{
\mathtt{content:Abstract Type;}\\
\mathtt{next:}\uparrow\mathtt {node};}\]`

A **linked list** is a [finite][bookofproofs$985] group of nodes `\(\mathtt{n_1,n_2,\ldots,n_k}\)`, such that

`\[
\mathtt{n_i\uparrow.next}=
\cases{
\mathtt{n_{i+1},\quad 1\le i\le k-1}\\
\mathtt{\boxtimes,\quad i=k}
},
\]`

i.e. the **pointer** `\(\mathtt{\uparrow.next}\)` of the `\(i\)`-th node "points" to the  `\((i+1)\)`-th node. The last node points to nothing, which is denoted by `\(\boxtimes\)` (sometimes also denoted by `\(\mathtt{NIL}\)` = "not in list").   

A linked list of `\(k\)` nodes is denoted by `\((n_1,n_2,...,n_k)\)`.

### Example

A list with three linked nodes: 


![408px-Singly-linked-list](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/examples/408px-Singly-linked-list.png?raw=true)

(Source: Uploaded by Lasindi: Public Domain)

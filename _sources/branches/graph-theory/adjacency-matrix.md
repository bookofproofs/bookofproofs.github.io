layout: definition
categories: branches,graph-theory
nodeid: bookofproofs$1213
orderid: 50
parentid: bookofproofs$471
title: Adjacency Matrix
description: ADJACENCY MATRIX &#9733; bring your math skills to the graduate level &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$570
keywords: adjacency,adjacency matrix,matrix
contributors: bookofproofs

---


---

An **adjacency matrix** of a [digraph][bookofproofs$524] `\(D=(V,E,\alpha,\omega)\)` is a [square matrix][bookofproofs$1056] of natural numbers `\(A\in M_{n\times n}(\mathbb N)\)`, whose matrix elements are defined by

`\[a_{ij}:=\cases{\text{number of edges }v_iv_j\text{ and }v'_iv'_j&\text{ if initial and terminal vertices are the same, i.e. }\alpha(v_iv_j)=\alpha(v'_iv'_j),~\omega(v_iv_j)=\omega(v'_iv'_j)\\
0&\text{ else.}}\]`


An **adjacency matrix** of a [graph][bookofproofs$523] `\(G=(V,E,\gamma)\)` is a [square matrix][bookofproofs$1056] of natural numbers `\(A\in M_{n\times n}(\mathbb N)\)`, whose matrix elements are defined by

`\[a_{ij}:=\cases{\text{number of edges }v_iv_j\text{ and }v'_iv'_j&\text{ if the ends are the same, i.e. }\gamma(v_iv_j)=\gamma(v'_iv'_j),\\
0&\text{ else.}}\]`

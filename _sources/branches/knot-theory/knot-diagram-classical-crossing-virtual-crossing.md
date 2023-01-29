layout: definition
categories: branches,knot-theory
nodeid: bookofproofs$6358
orderid: 50
parentid: bookofproofs$108
title: Knot Diagram, Classical Crossing, Virtual Crossing
description: KNOT DIAGRAM, CLASSICAL CROSSING, VIRTUAL CROSSING &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$6357,bookofproofs$6914
keywords: classical,classical crossing,crossing,diagram,double points,knot,knot diagram,virtual,virtual crossing
contributors: bookofproofs


---


---

Accoding to "Peter Guthrie Tait":https://www.bookofproofs.org/history/peter-guthrie-tait/, a **knot diagram** is a projection of a [closed curve][bookofproofs$1211] in three-dimensional space `\(\mathbb R^3\)` onto a plane. For instance, projecting the following curve onto a plane


![knotprojection](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/examples/knotprojection.jpg?raw=true)

(image source: bookofproofs) 

could result in the following knot diagram:


![knotdiagram](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/examples/knotdiagram.jpg?raw=true)

(image source: bookofproofs) 

Every knot diagram fulfills the following three properties:

1. The projected curve is smooth, i.e. there are no cusps and every point has a tangent line.
1. Points of intersection are formed by at most two segments of the curve. These points are called **double points**. In the above example, the points `\(A, B, C\)` and `\(D\)` are double points.
1. Every double point has exactly two different tangent lines (this eliminates the possibility of a double point with only one tangent line, where the curve does not actually cross itself but where two line segments still touch each other at a point). 
1. Each curve can be approximated by a finite number of line segments.

There are two types of double points:

* A **classical crossing** is a double point in a plane marked with under/overpassing information of the underlying three dimensional curve. In the above example, the double points `\(A,B\)` and `\(C\)` are classical crossings.
* A **virtual crossing** is a double point in a plane, which has no corresponding under/overpassing three dimensional curve. Rather, the idea is that the virtual crossing is not really there. In the above example, the point `\(D\)` is a virtual crossing. By convention, a virtual crossing is denoted by a small circle around it.

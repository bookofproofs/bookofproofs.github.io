layout: definition
categories: branches,geometry,euclidean-geometry,elements-euclid,book--1-plane-geometry
nodeid: bookofproofs$645
orderid: 300
parentid: bookofproofs$685
title: 1.04: Straight Line, Segment and Ray
description: 1.04: STRAIGHT LINE, SEGMENT AND RAY ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: 
keywords: euclidean distance,length,line,ray,segment,segments,straight line,straight lines,rays,lines
contributors: bookofproofs

---


---



> A **straight line** is any [line][bookofproofs$636] which lies evenly with [points][bookofproofs$631] on itself.

### Modern Definition

Note that Euclid does not distinguish between straight lines and segments. 

A [line][bookofproofs$636] connecting two given [points][bookofproofs$631] `\(A\)` and `\(B\)`, `$A\neq B,$` which is without a curve and infinite in length is called a **straight line** and denoted by `\(AB\)`.

The part of a straight line between the two [points][bookofproofs$631] `\(C\)` and `\(D\)` it connects is called a **line segment** (or simply a **segment**) and denoted by `\(\overline{CD}\)`. 

`\(C\)` and `\(D\)` are the **endpoints** of `\(\overline{CD}\)`.
 
Given a segment `\(\overline{EF}\)`, the part of the corresponding straight line `\(EF\)`, which begins at the endpoint `\(E\)`, connects it with the other endpoint `\(F\)` and is infinite in length is called a **ray**. We denote the ray with `\(\overline EF\)`.


Example of a straight line `\(AB\)`, a segment `\(\overline{CD}\)` and a ray `\(\overline EF\)`:


![Fig5p1p1](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/examples/Fig5p1p1.jpg?raw=true)


Given the Cartesian coordinates of two points in the `\(n\)`-dimensional [Euclidean metric space][bookofproofs$1206] `\(R^n\)`,

`\[\begin{array}{rcl}
A&=&(x_1,x_2,\ldots,x_n),\\
B&=&(y_1,y_2,\ldots,y_n)
\end{array}\]`


a segment can be described as a [total map][bookofproofs$592].
`\[
\overline{AB}:=\cases{[0,1]\to\mathbb R^n\\
t\to (x_1+t(y_1-x_1),x_2+t(y_2-x_2)\ldots,x_1+t(y_n-x_n))}
\]`

analogously, a ray can be described by 

`\[
\overline AB:=\cases{[0,\infty]\to\mathbb R^n\\
t\to (x_1+t(y_1-x_1),x_2+t(y_2-x_2)\ldots,x_1+t(y_n-x_n))}
\]`

and a straight line by


`\[
AB:=\cases{[-\infty,\infty]\to\mathbb R^n\\
t\to (x_1+t(y_1-x_1),x_2+t(y_2-x_2)\ldots,x_1+t(y_n-x_n)).}
\]`


The **length** of the segment `\(\overline {AB}\)` is given by the **Euclidean distance** of the two points:

`\[d(A,B):=\sqrt{(x_1+y_1)^2+(x_2+y_2)^2+\ldots+(x_n+y_n)^2}.\]`



### Try out an interactive demonstration:

<div id="boxE16491" class="jxgbox centered"  style="max-width:100%; width:500px; height:500px;"></div>
<div style ='clear:both'></div> 
 


§§§1

---

§§§1
<script type="text/javascript">
 var b = JXG.JSXGraph.initBoard('boxE16491', {boundingbox: [-5, 5, 5, -5]});
 
 var p1 = b.create('point',[-1.5,3], {name:'A',size:3});
 var p2 = b.create('point',[1.5,3], {name:'B',size:3});
 var p3 = b.create('point',[-1.5,0], {name:'C',size:3});
 var p4 = b.create('point',[1.5,-0], {name:'D',size:3});
 var p5 = b.create('point',[-1.5,-3], {name:'E',size:3});
 var p6 = b.create('point',[1.5,-3], {name:'F',size:3});
 
 var li1 = b.create('line',["A","B"], {straightFirst:true, straightLast:true, strokeWidth:2});
 var li2 = b.create('line',["C","D"], {straightFirst:false, straightLast:false, strokeWidth:2});
 var li3 = b.create('line',["E","F"], {straightFirst:false, straightLast:true, strokeWidth:2});

</script>
 

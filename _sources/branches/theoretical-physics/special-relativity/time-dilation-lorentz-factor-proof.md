layout: proof
categories: branches,theoretical-physics, special-relativity
nodeid: bookofproofs$6298
orderid: 50
parentid: bookofproofs$6297
title: 
description:  Proof of TIME DILATION, LORENTZ FACTOR &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$6267
keywords: dilation,factor,lorentz,lorentz factor,time,time dilation,proof
contributors: bookofproofs

---


---

Let `\(\mathcal I_1\)` and `\(\mathcal I_2\)` be two [inertial frames of reference][bookofproofs$6295].
Assume that a [light clock][bookofproofs$6275] is installed in `\(\mathcal I_2\)` with mirrors at a distance `\(d_2\)`. An observer `\(o_2\)`, who is situated in `\(\mathcal I_2\)`, will observe a tick duration of `\(t_2={d_2}/c\)`. 

Assume that `\(\mathcal I_1\)` and `\(\mathcal I_2\)` are moving relatively to each other with the constant speed `\(v\)` and that the light clock is positioned perpendicular to the direction of this movement. 

From the perspective of another observer `\(o_1\)` situated in `\(\mathcal I_1\)`, the light clock in `\(\mathcal I_2\)` will cover the distance `\(x\)` within the time of one "tick" of the light clock. Let the duration of this "tick" be `\(t_1\)`
from the perspective of the observer `\(o_1\)`. Note that from the perspective of the observer `\(o_1\)` 
the light will cover the distance `\(d_1\)`, which is given by hypotenuse the [right triangle][bookofproofs$688] `\(\triangle {ABC}\)`, as shown in the following figure:


![timedilation](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/examples/timedilation.png?raw=true)

(c) bookofproofs own work

According to the [Pythagorean theorem][bookofproofs$968], we get `\[d_1^2=x^2+d_2^2,\]` which is equivalent to 

`\[\begin{array}{rcl}&&(ct_1)^2=(vt_1)^2+(ct_2)^2\\
&\Leftrightarrow&c^2t_1^2=v^2t_1^2+c^2t_2^2\\
&\Leftrightarrow&c^2t_1^2-v^2t_1^2=c^2t_2^2\\
&\Leftrightarrow&t_1^2-\frac{v^2}{c^2}t_1^2=t_2^2\\
&\Leftrightarrow&t_1^2\left(1-\frac{v^2}{c^2}\right)=t_2^2.\\
\end{array}\quad\quad ( * )\]`

By hypothesis, `\(0\le v < c\)`, from which it follows `\[0\le \frac{v^2}{c^2} < 1\]` and `\[1\ge 1- \frac{v^2}{c^2} > 0.\quad\]`
Because the term `\(1- v^2/c^2\)` is non negative, is possible to calculate the [square root][bookofproofs$46], leading to the inequation 
`\[1\ge \sqrt{1- v^2/c^2} > 0.\quad\quad ( * * )\]` 

It follows together with  `\(( * )\)` that 

`\[t_1\sqrt{\left(1-\frac{v^2}{c^2}\right)}=t_2.\]`

Because `\(( * * )\)` is non zero, we can solve the equation for `\(t_1\)` leading to the equation

`\[t_1=t_2\frac 1{\sqrt{\left(1-\frac{v^2}{c^2}\right)}}.\quad\quad(0\le v < c)\]`

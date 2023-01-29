layout: proposition
categories: branches,geometry,euclidean-geometry,elements-euclid,book--6-similar-figures
nodeid: bookofproofs$2005
orderid: 1800
parentid: bookofproofs$1878
title: 6.19: Ratio of Areas of Similar Triangles
description: 6.19: RATIO OF AREAS OF SIMILAR TRIANGLES &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: 
keywords: areas,ratio,similar,triangles
contributors: bookofproofs

---


---

### (Proposition 19 from Book 6 of Euclid's “Elements”)

> [Similar][bookofproofs$1983] [triangles][bookofproofs$6432] are to one another in the squared[^1] ratio of (their) corresponding sides.
* Let `$ABC$` and `$DEF$` be [similar][bookofproofs$1983] [triangles][bookofproofs$6432] having the [angle][bookofproofs$650] at `$B$` equal to the (angle) at `$E$`, and `$AB$` to `$BC$`, as `$DE$` (is) to `$EF$`, such that `$BC$` corresponds to `$EF$`.
* I say that triangle `$ABC$` has a [squared ratio][bookofproofs$1948] to triangle `$DEF$` with respect to (that side) `$BC$` (has) to `$EF$`.


![fig19e](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/euclid/Book06/fig19e.png?raw=true)


### Modern Formulation

With `$a:=|\overline{AB}|,$` `$b:=|\overline{BC}|,$` `$\gamma=\angle{ABC},$` `$a':=|\overline{DE}|,$` `$b':=|\overline{EF}|,$` and `$\gamma'=\angle{DEF},$` this proposition states that if in two triangles `$\triangle{ABC}$` `$\triangle{DEF},$` the angles are equal `$\gamma=\gamma'$` and the corresponding sides being the legs of these angles are proportional `$\frac ab=\frac {a'}{b'}$` then `$$\frac{\operatorname{area}\triangle{ABC}}{\operatorname{area}\triangle{DEF}}=\frac {b^2}{b'^2}.$$`

### Modern Proof: 

`$$\begin{array}{rcll}
\frac {a}{b}&=&\frac {a'}{b'}&|\cdot \frac {b^2}{a'b'}\\
\frac {ab}{a'b'}&=&\frac {b^2}{b'^2}\\
\frac {\frac 12ab\sin(\gamma)}{\frac 12a'b'\sin(\gamma')}&=&\frac {b^2}{b'^2}&(\text{since }\gamma=\gamma')\\
\frac{\operatorname{area}\triangle{ABC}}{\operatorname{area}\triangle{DEF}}&=&\frac {b^2}{b'^2}
\end{array}$$`

[^1]: Literally, "double" (translator's note).

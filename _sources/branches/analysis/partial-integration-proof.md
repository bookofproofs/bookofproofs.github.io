layout: proof
categories: branches,analysis
nodeid: bookofproofs$8338
orderid: 50
parentid: bookofproofs$8337
title: 
description: PROOF OF PARTIAL INTEGRATION &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$581
keywords: partial integration,integration by parts,proof
contributors: bookofproofs

---


---

* By hypothesis, `$[a,b]$` is a [closed real interval][bookofproofs$1153] and `$f,g:I\to\mathbb R$` are [continouosly differentiable functions][bookofproofs$6812].
* Applying the [product rule][bookofproofs$1375] to the [function][bookofproofs$592] `$F=fg,$` we get `$$F'(x)=f'(x)g(x)+f(x)g'(x).$$`
* According to the [fundamental theorem of calculus][bookofproofs$6807], this gives us
`$$\int_a^bF'(x)dx=F(x)\;\Rule{1px}{4ex}{2ex}^b_a= f(x)g(x)\;\Rule{1px}{4ex}{2ex}^b_a=\int_a^bf'(x)g(x)dx+\int_a^bf(x)g'(x)dx.$$`
* It follows
`$$\int_a^bf(x)g'(x)dx=f(x)g(x)\;\Rule{1px}{4ex}{2ex}^b_a  -\int_{a}^{b}g(x)f'(x)dx.$$`

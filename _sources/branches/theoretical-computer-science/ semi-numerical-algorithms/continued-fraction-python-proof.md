layout: proof
categories: branches,theoretical-computer-science, semi-numerical-algorithms
nodeid: bookofproofs$2884
orderid: 50
parentid: bookofproofs$8247
title: 
description: PROOF OF CONTINUED FRACTION PYTHON &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$1357,bookofproofs$8186
keywords: continued,fraction,python,continued fraction python,python continued fraction,continued fractions python,python fraction,continued fraction algorithm python,continued fraction algorithm,fraction continue python,continued fraction,continued fractions algorithm,proof
contributors: bookofproofs

---


---

### Proof of correctness

* In the first step, the [floor][bookofproofs$280] (integer part) `$q_0:=\lfloor x\rfloor$` of `$x$` is extracted and appended to the list `$\mathtt{cf}.$` 
* After the step `$x_0:=x-q_0,$` the number `$x_0$` fulfills `$0\le x_0 < 1$` and contains the fractional part of the original `$x$` value.
* In the `$\mathtt{while}$` loop, we have `$q_{i+1}=\left\lfloor\frac{1}{x_i}\right\rfloor$`, `$x_{i+1}=\frac{1}{x_i}-q_{i+1}=\frac{1}{x_i}-\left\lfloor\frac{1}{x_i}\right\rfloor.$`
* On the other hand, we have in each step `$$x_i=\frac{1}{q_{i+1}+x_{i+1}}=\frac{1}{\left\lfloor\frac{1}{x_i}\right\rfloor+\frac{1}{x_i}-\left\lfloor\frac{1}{x_i}\right\rfloor}.$$`
* By iteration, we get 
`$$x=\lfloor x\rfloor + \frac{1}{q_1+x_1}=\lfloor x\rfloor + \frac{1}{q_1+\frac{1}{q_2+x_2}}=\ldots$$`
* By the definition of the [continued fractions][bookofproofs$8188], this means
`$$x=[x_0;q_1+x_1]=[x_0;q_1,q_2+x_1]=\ldots=[x_0;q_1,\ldots,q_{i-1},q_i+x_i].$$`

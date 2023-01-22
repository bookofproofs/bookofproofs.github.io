layout: example
categories: branches,algebra
nodeid: bookofproofs$7956
orderid: 3
parentid: bookofproofs$7951
title: The Gaussian Method in Practice
description: THE GAUSSIAN METHOD IN PRACTICE &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$7937
keywords: gaussian,method,practice,x3-a[0][1]
contributors: bookofproofs

---
The following example will demonstrate the [Gaussian method][bookofproofs$7955] by example. 

---

### Example 

We want to solve the system of linear equations with three unknowns 

`$$\begin{array}{rcr} 
x_1 -3x_2 +2x_3&=&1\\
5x_1 + 4x_2 -3x_3&=&4\\
2x_1 -8x_2 +4x_3&=& -2\\
\end{array}\quad\quad( * )$$` 

This system has the following [extended coefficient matrix][bookofproofs$7941]:

`$$A|\beta:= 
\left(\begin{array}{rrr|r}
1&-3&2&1\\ 
5&4&-3&4\\ 
2&-8&4&-2\\ 
\end{array}\right)$$`

In the following, we use SageMath. You will have to click the evaluate buttons to see the results.

§§§1

The resulting [upper-triangular][bookofproofs$7949] matrix is 
 
`$$A|\beta:= 
\left(\begin{array}{rrr|r}
1&-3&2&1\\ 
0&19&-13&-1\\ 
0&0&-\frac{26}{19}&-\frac{78}{19}\\ 
\end{array}\right)$$`

Now we can use the [backward substitution][bookofproofs$7949] to solve the system

§§§2

Therefore, `$x_1=1, x_2=2, x_3=3$` is the solution of the system `$( * ).$`

---

§§§1
```python
<div class='sage'>
print("Original extended matrix:\n")
A=matrix(QQ,[[1,-3,2,1],[5,4,-3,4],[2,-8,4,-2]])
print(A)
print("")
print("STEP 1: Bring the matrix to the upper-triangular form")
print("\nAdding the -5-fold multiple of the first row to the second:\n")
A1=A
A1[1]=A1[1]-5*A1[0]
print(A1)
print("\nAdding the -2-fold multiple of the first row to the third:\n")
A1[2]=A1[2]-2*A1[0]
print(A1)
print("\nAdding the 2/19-fold multiple of the second row to the third:\n")
A1[2]=A1[2]+2/19*A1[1]
print(A1)
</div>
```

§§§2
```python
<div class='sage'>
print("STEP 2: Backward substitution:\n")
A=matrix(QQ,[[1,-3,2,1],[0,19,-13,-1],[0,0,-26/19,-78/19]])
print(A)
print("\nSetting x3=-78/19*(-19/26), substituting x3 in second row, setting x2=...etc....\n")
x3=A[2][3]/A[2][2]
x2=(A[1][3]-A[1][2]*x3)/A[1][1]
x1=(A[0][3]-A[0][2]*x3-A[0][1]*x2)/A[0][0]
print("x3=", x3)
print("x2=", x2)
print("x1=", x1)

</div>
```
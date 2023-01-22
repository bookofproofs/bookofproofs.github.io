layout: proof
categories: branches,algebra
nodeid: bookofproofs$8685
orderid: 0
parentid: bookofproofs$6734
title: 
description: PROOF OF ABELIAN GROUP OF MATRICES UNDER ADDITION &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: 
keywords: abelian group matrix addition,proof
contributors: bookofproofs

---


---

The proof is very easy but long since it only requires the verification of the rules for the [matrices][bookofproofs$1048] `$M_{m\times n}(F)$` over a [field][bookofproofs$557] `$F$` component by component. We will use two different symbols to distinguish between the addition of the components `$"+"$` in the field `$F$` and the addition of matrices `$\oplus$` in `$M_{m\times n}(F)$`. 

### Ad `$(1)$`

* Let any three matrices `$A,B,C\in M_{m\times n}(F)$` be given.
* Let `$A=(a_{ij})$`, `$A=(b_{ij})$` and `$C=(c_{ij})$`, `$i=1,\ldots,m$`, `$j=1,\ldots,n$` be the components of `$A,B,C$`.
* Since `$(F,+)$` is itself an [Abelian group][bookofproofs$553], we have 
`$$a_{ij}+(b_{ij}+c_{ij})=(a_{ij}+(b_{ij})+c_{ij}$$`
for all `$i=1,\ldots,m$`, `$j=1,\ldots,n$`. 
* Thus, by the definition of [matrix addition][bookofproofs$8657], it follows `$$A\oplus(B\oplus C)=(A\oplus B)\oplus C.$$`

### Ad `$(2)$` 

* Let any two matrices `$A,B\in M_{m\times n}(F)$` be given.
* Let `$A=(a_{ij})$`, `$A=(b_{ij})$`, `$i=1,\ldots,m$`, `$j=1,\ldots,n$` be the components of `$A,B$`.
* Since `$(F,+)$` is itself an [Abelian group][bookofproofs$553], we have 
`$$a_{ij}+b_{ij}=b_{ij}+a_{ij}$$`
for all `$i=1,\ldots,m$`, `$j=1,\ldots,n$`. 
* Thus, by the definition of [matrix addition][bookofproofs$8657], it follows `$A\oplus B=B\oplus A.$`

### Ad `$(3)$` 

* Let `$A,O\in M_{m\times n}(F)$` be given, where `$O$` is the [zero matrix][bookofproofs$1052], with the components `$A=(a_{ij})$`, `$O=(b_{ij})$`, b_{ij}=0, `$i=1,\ldots,m$`, `$j=1,\ldots,n$` where `$0\in F.$` 
* It follows `$a_{ij}+0=0+a_{ij}=a_{ij}$` for all `$i=1,\ldots,m$`, `$j=1,\ldots,n$`. 
* Thus, `$A\oplus O=O\oplus A=A.$`

### Ad `$(4)$` 

* Let `$A\in M_{m\times n}(F)$` be given with the components `$A=(a_{ij})$`, `$i=1,\ldots,m$`, `$j=1,\ldots,n.$` 
* In `$(F,+)$` the element `$-a_{ij}$` is the [inverse element][bookofproofs$670] of the addition `$+$`. 
* Thus, `$a_{ij}+(-a_{ij})=-a_{ij}+a_{ij}=0$` for all `$i=1,\ldots,m$`, `$j=1,\ldots,n$`. 
* By setting `$-A$` as the matrix with the components `$(-a_{ij})$`, `$i=1,\ldots,m$`, `$j=1,\ldots,n,$` we get `$$A\oplus -A=-A\oplus A=O$$` with `$O$` being the zero matrix in `$M_{m\times n}(F)$`.

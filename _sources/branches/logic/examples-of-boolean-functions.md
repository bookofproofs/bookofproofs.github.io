layout: example
categories: branches,logic
nodeid: bookofproofs$7894
orderid: 50
parentid: bookofproofs$1316
title: Examples of Boolean Functions
description: EXAMPLES OF BOOLEAN FUNCTIONS &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: 
keywords: boolean,examples,functions
contributors: bookofproofs

---


---

### Example 1

The [Boolean constants][bookofproofs$1307] `$1$` and `$0$` are particular types of [prime propositions][bookofproofs$7867]. They define constant Boolean functions `$f(1)=1$` and `$f(0)=0$`.

### Example 2:

A [Boolean variable][bookofproofs$1307] `$x$` is another particular type of a prime proposition. They define an identity Boolean functions `$$f(x)=x=\cases{0&\text{if }x=0,\\1&\text{if }x=1.}$$`

### Example 3

Let `\(f(x_1,x_2)\)` be represented by the compound proposition `\(x_1\vee \neg x_2\)`. Note that this proposition involves two [connectives][bookofproofs$7867] - the negation "$\neg$", which is an unary connective and the disjunction "$\vee$", which is a binary connective. The compound propositions involves two variables `$x_1$` and `$x_2$`, which are prime propositions.

Using an [interpretation][bookofproofs$710] `$I$` and the corresponding [valuation function][bookofproofs$710] `$[[]]_I$` we can calculate the values of the Boolean function `$f$` by assigning all possible truth values to the two variables of `$f$`:

* `\(f(1,1)=[[1\vee \neg 1]]_I=[[1\vee 0]]_I=[[ 1 ]]_I=1,\)`
* `\(f(1,0)=[[1\vee \neg 0]]_I=[[1\vee 1]]_I=[[ 1 ]]_I=1,\)`
* `\(f(0,1)=[[0\vee \neg 1]]_I=[[0\vee 0]]_I=[[ 0 ]]_I=0,\)`
* `\(f(0,0)=[[0\vee \neg 0]]_I=[[0\vee 1]]_I=[[ 1 ]]_I=1.\)`

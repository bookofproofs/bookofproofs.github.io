layout: definition
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$718
orderid: 50
parentid: bookofproofs$103
title: Set-theoretic Definitions of Natural Numbers
description: SET-THEORETIC DEFINITIONS OF NATURAL NUMBERS ERNST ZERMELO 1908, JOHN VON NEUMANN 1923 &#9733; master graduate maths &#10004; visit BookOfProofs now!
references: bookofproofs$656
keywords: 1908,1923,definitions,ernst,john,natural,natural numbers,neumann,numbers,set,theoretic,von,zermelo,definition of natural numbers,von neumann natural numbers,construction of natural numbers,set of natural numbers,von neumann ordinals,natural numbers definition,natural number definition,set theoretic definition of natural numbers,zermelo ordinals
contributors: bookofproofs


---


---

The set of **natural numbers** `\(\mathbb N\)` is defined using the concept [ordinals][bookofproofs$723], as follows:

### Definition due to von Neumann (1923)

(1) The empty set (as the first ordinal)[^1] represents the first natural number:

`\[0:=\{\emptyset\}.\]`


![axiom2](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/examples/axiom2.jpg?raw=true)


(2) Once we have the ordinal `\(n=\alpha\)`, we can construct a bigger ordinal[^2] using recursively the [formula for constructing successors of ordinals][bookofproofs$774], denoting the successor `\(n^+\)` of the natural number `\(n\)`:
`\[n^+:=s(\alpha):=\alpha\cup\{\alpha\}=n\cup \{n\}.\]`
Applying the set axioms and this construction systematically, it gives us a chain of ordered ordinals 

`\[\begin{array}{rcl}0&:=&\emptyset,\\1&:=&0\cup\{0\}=\emptyset\cup\{\emptyset\}=\{\emptyset\},\\2&:=&1\cup\{1\}=\{\emptyset\}\cup\{\{\emptyset\}\}=\{\emptyset,\{\emptyset\}\},\\3&:=&2\cup\{2\}=\{\emptyset,\{\emptyset\}\}\cup\{\{\emptyset,\{\emptyset\}\}\}=\{\emptyset,\{\emptyset\},\{\emptyset,\{\emptyset\}\}\},\\&\vdots&\\n^+&:=&n\cup\{n\},\\&\vdots&\end{array}\]`

which can be visualized in the following figure


![axiom8](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/examples/axiom8.jpg?raw=true)


and for which we introduce the notation `\(0,1,2,3,\ldots\)`:

`\[0 < 1 < 2 < 3 < \ldots\]`

Due to the [axiom of infinity][bookofproofs$678] we can postulate the existence of an infinite set, which is "contains" all such sets.[^3] 

`\[\mathbb N:=\bigcup n=\{0,1,2,3,\ldots.\}\]`


[^1]: Please note that it is well defined due to the [axiom of existence of empty set][bookofproofs$666].
[^2]: [Ordinals][bookofproofs$723] are sets with some [interesting properties][bookofproofs$724], including "trichotomy":https://www.bookofproofs.org/branches/trichotomy-of-ordinals-cantor/, ensuring that all ordinals __can be compared with each other__ by the relation 
`\[\alpha < \beta:\Leftrightarrow \alpha\in\beta.\]`
For any two ordinals, and in particular for natural numbers, we can therefore always decide which one is "bigger", "smaller", or whether they are equal to each other.


[^3]: Please note that this infinite set is an [ordinal by definition][bookofproofs$723]. However, we have not built by the above construction formula, i.e. it is not a successor of any "previous" ordinal. 
In other words, `\(\mathbb N\)` is the first [limit ordinal][bookofproofs$780].
### Definition due to Ernst Zermelo (1908)

The [set][bookofproofs$550] `\(\mathbb N\)` of natural numbers is defined recursively by: `\[\begin{array}{rcl}0&:=&\emptyset,\\1&:=&\{0\}=\{\emptyset\},\\2&:=&\{1\}=\{\{\emptyset\}\},\\3&:=&\{2\}=\{\{\{\emptyset\}\}\},\\&\vdots&\\n^+&:=&\{n\}=\underbrace{\{\ldots\{ }_{n+1\text{ times}}\emptyset\underbrace{\}\ldots\} }_{n+1\text{ times}},\\&\vdots&\\\end{array}\]`

This definition can be visualized as follows:


![axiom8_1](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/examples/axiom8_1.jpg?raw=true)


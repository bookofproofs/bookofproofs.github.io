layout: example
categories: branches,logic
nodeid: bookofproofs$7845
orderid: 50
parentid: bookofproofs$709
title: Examples of Syntax
description: EXAMPLES OF SYNTAX &#9733; bring your math skills to the graduate level &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$577
keywords: examples,syntax
contributors: bookofproofs

---


---

We continue with the above [examples of formal languages][bookofproofs$7844] and define for them (more or less formally)  a [syntax][bookofproofs$709].
### Example 1


Let `$\Sigma:=\{a,b,c\}$` be our [alphabet][bookofproofs$708] and `$L\subseteq (\Sigma^*,\cdot)$` be the formal language containing only the words beginning with "`$a$`" and ending with "`$c$`", e.g.

> "`$acc$`", "`$aabbcc$`" are words of `$L$`, but "`$a$`", "`$aa$`", "`$aaaa$`", "`$bca$`", and "`$bbbaaa$`" are not words of `$L$`.

The syntax consists of the following rules:

* If `$s\in L$`, then `$s$` begins with the letter "`$a$`" and ends with the letter "`$c$`".

### Example 2

Let `$\Sigma$` be the set of all Capital and lowercase Latin letters, including the empty space, the comma, the point, the question mark, and the exclamation mark, and let `$L\subseteq (\Sigma^*,\cdot)$` be the formal language containing all English words. Thus

The syntax consists of these rules: 

* If, `$s\in L$`, then `$s$` is a concatenation of words `$w_1,\ldots,w_k$` from a given dictionary `$D$` of (finitely) many all English words such that
   * `$k\ge 1$`,
   * `$s=w_1z_1w_2z_2\ldots w_kz_{k}$`, where `$z_k$`  is either the empty word `$\epsilon$` or one of the characters `$\{``,",``.",``!",``?",``\;"\}$`

Please note that `$s$` might not be a sentence since it does not have to start with a capital letter and it can end with a comma or a blank. Neither does `$s$` have to make any sense in the natural English language. All it has to fulfill is the rules of the syntax.


### Example 3

Let `$\Sigma:=\{0,1,2,3,4,5,6,7,8,9,+,=\}$` and let `$L\subseteq (\Sigma^*,\cdot)$` be the formal language containing all words starting with some letter(s) except "=", then containing the letter "`$=$`" only once and then ending some letter(s) except "=".

Let `$\Sigma:=\{0,1,2,3,4,5,6,7,8,9,+,=\}$`. Let 

Thus, the syntax consists of these rules: 

* If `$s\in L,$` then there exist `$s_1,s_2\in \Sigma^*$` with  
   * `$s_1,s_2$` consist of at least one letter from `$\Sigma$` except `$"=",$` and 
   * `$s$` is the concatenation of `$s_1 \cdot "=" \cdot s_2$`.

layout: example
categories: branches,logic
nodeid: bookofproofs$7844
orderid: 50
parentid: bookofproofs$7842
title: Examples of Languages
description: EXAMPLES OF LANGUAGES ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: 
keywords: examples of languages
contributors: bookofproofs

---


---

We continue with the above [examples of strings over alphabets][bookofproofs$7843] and define for them [languages][bookofproofs$7842].
### Example 1

Let `$\Sigma:=\{a,b,c\}$` be our [alphabet][bookofproofs$708]. A formal language `$L\subseteq (\Sigma^*,\cdot)$` could be the subset containing only the words beginning with an `$a$` and ending with a `$c$`, e.g.

> "`$acc$`", "`$aabbcc$`" are words of `$L$`, but "`$a,$`", "`$aa$`", "`$aaaa$`", "`$bca$`", and "`$bbbaaa$`" are not words of `$L$`.

### Example 2

Let `$\Sigma$` be the set of all Capital and lowercase Latin letters, including the empty space, the comma, the point, the question mark, and the exclamation mark. A language `$L\subseteq (\Sigma^*,\cdot)$` containing all English words is a formal language. Thus

> "Socrates is a man." `$\in L$`

but

> "DLdfa hidb!zw. alsei?" `$\not\in L$`.

Please note that `$L$` is __not__ the natural English language. For instance, the following sentence would belong to the formal language `$L$`:

> "Is man Socrates run." `$\in L$`

because all the words are English words. However, the sentence does not make any sense in the natural English language.

### Example 3

Let `$\Sigma:=\{0,1,2,3,4,5,6,7,8,9,+,=\}$`. Let `$L\subseteq (\Sigma^*,\cdot)$` be the formal language containing all words starting with some letter(s) except "=", then containing the letter "`$=$`" only once and then ending some letter(s) except "=".

Thus

> `$"1=1",$` `$"1=0",$` and `$"1+1=2" \in L,$`

but

> `$"30014",$` `$"2222=333=+++",$` `$"=32",$` and `$"==="\not\in L.$`

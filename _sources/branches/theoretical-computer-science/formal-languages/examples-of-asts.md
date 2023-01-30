layout: example
categories: branches,theoretical-computer-science, formal-languages
nodeid: bookofproofs$8486
orderid: 300
parentid: bookofproofs$78
title: Examples of ASTs
description: EXAMPLES OF ASTS ★ bring your math skills to the graduate level ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$1086,bookofproofs$7895
keywords: examples of asts
contributors: bookofproofs

---


---

Assume that we have a simple example [grammar][bookofproofs$709] `$G=(V,T,R,S)$` such that:
* The set of variables `$V=\{S\}$` consist only of the [starting symbol][bookofproofs$709].
* The terminal symbols (alphabet) consists of the following four characters `$T=\{a,b,(,)\}.$`
* The grammar rules `$R$` are:
   * `$S\to \epsilon$`
   * `$S\to a$`
   * `$S\to b$`
   * `$S\to SS$`
   * `$S\to (S)$`

### Building the Abstract Syntax Tree

We want to build an [abstract syntax tree][bookofproofs$8484] `$\operatorname{AST}(\omega)$` of the string `$\omega=()ab()$`.

#1. Starting symbol
`$$\begin{array}{l}
S
\end{array}$$`

#2. Applying the rule `$S\to SS.$`
`$$\begin{array}{ll}
S
&\to S\\
&\to S
\end{array}$$`

#3. Apply the rule `$S\to (S).$`
`$$\begin{array}{lll}
S
&\to S&\to (\\
&&\to S\\
&&\to )\\
&\to S
\end{array}$$`

#4. Apply the rule `$S\to \epsilon.$`
`$$\begin{array}{lll}
S
&\to S&\to (\\
&&\to )\\
&\to S
\end{array}$$`

#5. Apply the rule `$S\to SS.$`
`$$\begin{array}{lll}
S
&\to S&\to (\\
&&\to )\\
&\to S&\to S\\
&&\to S\\
\end{array}$$`

#6. Apply the rule `$S\to a.$`
`$$\begin{array}{lll}
S
&\to S&\to (\\
&&\to )\\
&\to S&\to a\\
&&\to S\\
\end{array}$$`

#7. Apply the rule `$S\to SS.$`
`$$\begin{array}{llll}
S
&\to S&\to (\\
&&\to )\\
&\to S&\to a\\
&&\to S&\to S\\
&&&\to S\\
\end{array}$$`

#8. Apply the rule `$S\to b.$`
`$$\begin{array}{llll}
S
&\to S&\to (\\
&&\to )\\
&\to S&\to a\\
&&\to S&\to b\\
&&&\to S\\
\end{array}$$`

#9. Apply the rule `$S\to (S).$`
`$$\begin{array}{lllll}
S
&\to S&\to (\\
&&\to )\\
&\to S&\to a\\
&&\to S&\to b\\
&&&\to S&\to(\\
&&&&\to S\\
&&&&\to)\\
\end{array}$$`

#10. Apply the rule `$S\to \epsilon.$`
`$$\begin{array}{lllll}
S
&\to S&\to (\\
&&\to )\\
&\to S&\to a\\
&&\to S&\to b\\
&&&\to S&\to(\\
&&&&\to)\\
\end{array}$$`

### Another `$\operatorname{AST}_G(\omega)$` for `$()ab().$`

Please note that the grammar `$G$` is [ambiguous][bookofproofs$8485]. We can produce the same string using another [abstract syntax tree][bookofproofs$8484].

#1. Repeat the steps `$1$` to `$5$` as in the previous example

#6. Apply the rule `$S\to (S).$`
`$$\begin{array}{llll}
S
&\to S&\to (\\
&&\to )\\
&\to S&\to S\\
&&\to S&\to (\\
&&&\to S\\
&&&\to )\\
\end{array}$$`

#7. Apply the rule `$S\to SS.$`
`$$\begin{array}{llll}
S
&\to S&\to (\\
&&\to )\\
&\to S&\to S&\to S\\
&&&\to S\\
&&\to S&\to (\\
&&&\to S\\
&&&\to )\\
\end{array}$$`

#8. Apply the rule `$S\to \epsilon.$`
`$$\begin{array}{llll}
S
&\to S&\to (\\
&&\to )\\
&\to S&\to S&\to S\\
&&&\to S\\
&&\to S&\to (\\
&&&\to )\\
\end{array}$$`

#9. Apply the rule `$S\to a.$`
`$$\begin{array}{llll}
S
&\to S&\to (\\
&&\to )\\
&\to S&\to S&\to a\\
&&&\to S\\
&&\to S&\to (\\
&&&\to )\\
\end{array}$$`

#10. Apply the rule `$S\to b.$`
`$$\begin{array}{llll}
S
&\to S&\to (\\
&&\to )\\
&\to S&\to S&\to a\\
&&&\to b\\
&&\to S&\to (\\
&&&\to )\\
\end{array}$$`

### Unambiguous Grammars vs. Ambiguous Rule Productions

Please note that unambiguous grammars can have ambiguous rule productions. The criterion of [unambiguity of grammars][bookofproofs$8485] only means that all (even different) productions of the grammar of a given word lead to the same abstract syntax tree.

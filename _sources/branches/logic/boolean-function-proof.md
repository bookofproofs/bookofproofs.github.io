layout: proof
categories: branches,logic
nodeid: bookofproofs$1317
orderid: 100
parentid: bookofproofs$1316
title: 
description:  Proof of BOOLEAN FUNCTION &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$711
keywords: boolean,function,proof
contributors: bookofproofs

---


---

Now we will prove the above lemma by verifying that a Boolean function `$f_\phi$` is properly defined of any proposition `$\phi$`.

* Case 1: Assume that `$\phi$` is a [prime proposition][bookofproofs$7867].
   * Then `$\phi$` is by definition either a [Boolean constant][bookofproofs$1307] or a [Boolean variable][bookofproofs$1307]. 
   * For any given [interpretation][bookofproofs$710] `$I$` and the corresponding [valuation function][bookofproofs$710] `$[[]]_I$`, it follows from the definition of the [semantics of `$PL0$`][bookofproofs$7871] that 
`$$f_\phi=\cases{
[[ 1 ]]_I&\text{if }\phi\text{ is the Boolean constant }1,\\
[[ 0 ]]_I&\text{if }\phi\text{ is the Boolean constant }0,\\
[[x]]_I&\text{if }\phi\text{ is the Boolean variable }x,\\
}$$`
   * Therefore, `$f_\phi$` is well-defined.
* Case 2: Now assume that `$\phi$` is a [proposition compound of prime propositions][bookofproofs$7867], i.e. `$\phi=p_1\circ\ldots\circ p_n$` for an [$n$-ary connective][bookofproofs$7867] "$\circ$", all `$p_i$` being prime.
   * From Case 1 it follows that the Boolean functions `$f_{p_1},\ldots,f_{p_n}$` are well-defined.
   * The valuation function `$[[p_1\circ\ldots\circ p_n]]_I$` induces a composition of Boolean functions `$f_{\phi}=f_{p_1}\circ \ldots\circ f_{p_n}$`. 
   * We know that any [composition of functions is again a function][bookofproofs$1314]. This holds for functions in general, and for Boolean functions in particular.
   * Therefore, `$f_\phi$` is well-defined.
* General Case 3: Now assume that `$\phi$` is a [proposition compound of compound propositions][bookofproofs$7867] `$p_1,\ldots, p_n$`.
   * Since by Case 2,  `$f_{p_1},\ldots, f_{p_n}$` are well-defined and since any [composition of functions is again a function][bookofproofs$1314], therefore  `$f_\phi=f_{p_1}\circ \ldots\circ f_{p_n}$` is well-defined.

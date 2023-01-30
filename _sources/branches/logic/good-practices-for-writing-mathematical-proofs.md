layout: explanation
categories: branches,logic
nodeid: bookofproofs$6824
orderid: 500
parentid: bookofproofs$184
title: Good Practices for Writing Mathematical Proofs
description: GOOD PRACTICES FOR WRITING MATHEMATICAL PROOFS &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$6823
keywords: good,mathematical,practices,proofs,writing
contributors: bookofproofs

---


---

Many proofs can be written by following some standard guidelines or good practices to write a proof. 

bookofproofs.org will automatically suggest you the right proof template when you select a proof type, before posting a proof.

### Basic Template for Proofs

1. Set the context of the proof.
1. Assert the hypothesis.
1. List implications.
1. State the conclusion.

### Template for Proofs by Induction

1. Set the context of the proof.
1. Base Case: Prove that a statement `$S$` is true for the base case `$S(b).$`
1. Hypothesis: Assume that `$S(n)$` is true for some fixed natural number `$n:=k\ge b.$`
1. Induction Step: Using the fact that `$S(n)$` is true, prove that `$S(n+1)$` is true.
1. State the conclusion by [induction][bookofproofs$6841], i.e. conclude that `$S(n)$` is true for all natural numbers `$n\ge b$`.

### Proof by Contraposition

1. Set the context of the proof.
1. Provide the hypothesis which will lead to a contrapositive of an original conditional statement.
1. Provide the implication, e.g. "Since (refer here to the original conditional statement), it follows from the hypothesis by [contraposition][bookofproofs$1330] that (provide here the implication)."
1. As a conclusion, restate the main implication.

### Proof by Contradiction:

1. Set the context of the proof.
1. Assert the hypothesis that will lead to a contradiction.
1. List implications, leading to that contradiction
1. State the conclusion, e.g. "This is a [contradiction][bookofproofs$744] to the hypothesis."

### Proof of an implication

1. Set the context of the proof, i.e. state that you want to prove the implication `$P\Rightarrow Q$`, in which you replace `$P,Q$` by two statements, for which you want to show the implication. 
2. You have now two possibilities to continue the proof: 
   * Possibility 1: Direct Proof:
     1. Assert the hypothesis, i.e. take `$y$` and assume that `$P(y)$` is true.
     2. List implications, showing that then `$Q(y)$` must also be true.
     3. State the conclusion, e.g. "Therefore, it follows that `$P\Rightarrow Q.$`"
   * Possibility 2: Proof by contradiction: 
     1. Assert the hypothesis, i.e. take `$y$` and assume that both: `$P(y)$` is true and `$Q(y)$` is false.
     2. List implications, leading to that contradiction.
     3. State the conclusion, e.g. "This is a [contradiction][bookofproofs$744] to the hypothesis. Thus, it follows that `$P\Rightarrow Q$`".


### Proof of Equality of Sets

1. State the assumption that e.g. `$A$` and `$B$` are [sets][bookofproofs$550].
1. Part 1: Provide a proof of `$A\subseteq B$`, e.g. using one of the other proof templates.
1. Part 2: Provide a proof of `$B\subseteq A$`, e.g. using one of the other proof templates.
1. State the conclusion, e.g. "It follows from the [equality of sets][bookofproofs$6841] that `$A = B$`".

### Proof of Inclusion of two Sets `$A\subseteq B$`

1. Set the context of the proof, i.e. what is being assumed about the sets `$A$` and `$B$`.
1. Assert the hypothesis, e.g. "let `$x\in A$`". 
1. List implications, in particular, use the properties of the set `$A$` and `$B$` to show `$x$` belongs to the set `$B$`.
1. State the conclusion, e.g. "It follows that `$x\in B$`. Thus, by the [definition of subset][bookofproofs$552], `$A\subset B$`.

### Proof of a function `$f$` being surjective

1. Set the context of the proof, i.e. introduce the [function][bookofproofs$592] `$f: A\to B$`, its domain `$A$` and its domain `$B$`.
1. Assert the hypothesis, i.e. select an arbitrary element of the codomain, e.g. "let `$y\in B$`". 
1. List implications, i.e. exhibit a value `$x\in A$` with `$f(x)=y.$`
1. State the conclusion, e.g. "It follows by the [definition of surjective functions][bookofproofs$770] that `$f$` is surjective".

 
### Proof of a function `$f$` being injective

1. Set the context of the proof, i.e. introduce the [function][bookofproofs$592] `$f: A\to B$`, its domain `$A$` and its domain `$B$`.
1. Assert the hypothesis, i.e. select two values `$x_1,x_2\in A$` and assume that `$f(x_1)=f(x_2)$`.
1. List implications, i.e. show that `$x_1=x_2.$`
1. State the conclusion, e.g. "It follows by the [definition of injective functions][bookofproofs$769] that `$f$` is injective".

### Proof of a function `$f$` being bijective

1. Set the context of the proof, i.e. introduce the [function][bookofproofs$592] `$f: A\to B$`, its domain `$A$` and its domain `$B$`.
1. Prove that `$f$` is [injective][bookofproofs$769] (you might use the template listed above for injective functions).
1. Prove that `$f$` is [surjective][bookofproofs$770] (you might use the template listed above for surjective functions).
1. State the conclusion, e.g. "It follows by the [definition of bijective functions][bookofproofs$771] that `$f$` is bijective".

### Proof that a number `$L$` is the limit of a function `$f(x)$`, as `$x$` tends to a value `$a.$`

1. Set the context of the proof, i.e. introduce the [function][bookofproofs$592] `$f: A\to B$`, its domain `$A$` and its domain `$B$` and say what is known about the numbers `$a$` and `$L.$`
1. Assert the hypothesis, i.e.:
   * Select an arbitrary positive number `$\epsilon$`, e.g. "Given `$\epsilon > 0.$`"
   * Propose an appropriate value for `$\delta$`, e.g. "Let `$\delta:=\ldots$`"
   * Select `$x$` such that `$0 < |x-a| < \delta.$`
1. List implications, i.e. show that `$|f(x)-L| < \epsilon.$`
1. State the conclusion, e.g. "It follows by the [definition of function limit][bookofproofs$6683] that `$\lim_{x\to a}f(x)=L$`".

### Proof that a number `$L$` is the limit of a function `$f(x)$`, as `$x$` tends to infinity `$\infty.$`

1. Set the context of the proof, i.e. introduce the [function][bookofproofs$592] `$f: A\to B$`, its domain `$A$` and its domain `$B$` and say what is known about the number `$L$`.
1. Assert the hypothesis, i.e.:
   * Select an arbitrary positive number `$\epsilon$`, e.g. "Given `$\epsilon > 0$`."
   * Propose an appropriate value for a natural number `$N$`.
   * Select `$x > N$`
1. List implications, i.e. show that `$|f(x)-L| < \epsilon$`.
1. State the conclusion, e.g. "It follows by the [definition of function limit][bookofproofs$6683] that `$\lim_{x\to a}f(x)=L$`."

### Proof that the limit of a function `$f(x)$` does not exist, as `$x$` tends to a value `$a.$` 

1. Set the context of the proof, i.e. introduce the [function][bookofproofs$592] `$f: A\to B$`, its domain `$A$` and its domain `$B$` and say what is known about the number `$a.$`
1. Assert the hypothesis, i.e.:
   * Assume that `$L$` is the limit, i.e. `$\lim_{x\to a}f(x)=L.$`
   * Propose an appropriate value for a positive number `$\epsilon$`, e.g. "Let `$\epsilon:=\ldots$`"
   * Select an arbitrary value for `$\delta$`, e.g. "Given `$\delta > 0.$`"
   * Select appropriate values `$x_1,x_2$`, i.e. such that `$0 < |x_1-a| < \delta,$` `$0 < |x_2-a| < \delta,$` and that `$|f(x_1)-f(x_2)|$` exceedes `$2\epsilon.$`
1. List implications, i.e. 
   * Assume that `$|f(x_1)-L| < \epsilon$` and that `$|f(x_2)-L| < \epsilon.$` 
   * Using [triangle inequality][bookofproofs$588], show that `$2\epsilon =\epsilon + \epsilon > |f(x_1)-L|+|f(x_2)-L|=|f(x_1)-L|+|L-f(x_2)|\ge |f(x_1)-L+L-f(x_2)|=|f(x_1)-f(x_2)|.$`
   * State the contradiction, e.g. "This shows that `$2\epsilon > |f(x_1)-f(x_2)|,$` which is a [contradiction][bookofproofs$744].
1. State the conclusion, e.g. "Thus, it cannot hold that both `$|f(x_1)-L| < \epsilon$` and that `$|f(x_2)-L| < \epsilon.$` Therefore, the limit `$L$` does not exist.

### Proof that the limit of a function `$f(x)$` does not exist, if `$f$` is unbounded as `$x$` tends to a value `$a.$` 

1. Set the context of the proof, i.e. introduce the [function][bookofproofs$592] `$f: A\to B$`, its domain `$A$` and its domain `$B$`  and say what is known about the number `$a$`.
1. Assert the hypothesis, i.e.:
   * Assume that `$L$` is the limit, i.e. `$\lim_{x\to a}f(x)=L$`.
   * Propose "Let `$\epsilon:=1$` and let `$\delta > 0$` be given."
   * Select an appropriate number `$x$` such that `$0 < |x-a| < \delta$` (but suitable for implications to follow).
1. List implications, i.e. 
   * Show that `$f(x) > |L| + 1.$` 
   * Conclude that `$|f(x)-L| > |L|+1-L \ge 1.$`
   * State the contradiction, e.g. "This is a [contradiction][bookofproofs$744] to `$|f(x)-L| < \epsilon=1$`".
   * State the contradiction, e.g. "This is a [contradiction][bookofproofs$744] to `$|f(x)-L| < \epsilon=1$`".

layout: proof
categories: branches,analysis
nodeid: bookofproofs$6597
orderid: 50
parentid: bookofproofs$6596
title: 
description:  Proof of HEINE-BOREL THEOREM &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$582
keywords: borel,heine,theorem,heine borel theorem,heine borel theorem proof,proof of heine borel theorem,proof
contributors: bookofproofs

---


---

Let `\(A\subset\mathbb R^n\)` be a [subset][bookofproofs$552] `\(A\)` of the [$n$-dimensional metric space of real numbers][bookofproofs$1206] `$\mathbb R^n$`. 


### "$\Rightarrow$"

* Let `$A$` be [compact][bookofproofs$6575].
* Since `\(\mathbb R^n\)` is a [metric space][bookofproofs$617], `$A\subset X$` is a compact subset of a metric space.
* According to the [corresponding proposition][bookofproofs$6589], all compact subsets of metric spaces are [closed][bookofproofs$852] and [bounded][bookofproofs$6574].
* Thus, also `\(A\)` must be closed and bounded.

### "$\Leftarrow$"

* Let `$A$` be [closed][bookofproofs$852] and [bounded][bookofproofs$6574].
* Because `$A$` is bounded, it is contained in a sufficiently large closed `$n$`-dimensional cuboid `$Q$`.
* According to the [corresponding proposition][bookofproofs$6582], all closed `$n$`-dimensional cuboids are compact. 
* Thus, `$Q$` must be compact.
* Because `$A\subset Q$` by construction, it is a closed subset of a compact set.
* According to the [corresponding proposition][bookofproofs$6594], all closed subsets of compact sets are compact.
* Thus, `$A$` must be compact.

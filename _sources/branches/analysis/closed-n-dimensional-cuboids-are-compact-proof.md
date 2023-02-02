layout: proof
categories: branches,analysis
nodeid: bookofproofs$6588
orderid: 50
parentid: bookofproofs$6582
title: 
description:  Proof of CLOSED N-DIMENSIONAL CUBOIDS ARE COMPACT &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$582
keywords: are,closed,compact,cuboids,dimensional,proof
contributors: bookofproofs

---


---

* Let `\(a_\nu,b_\nu\in\mathbb R\)` be [real numbers][bookofproofs$1105] with `\(a_\nu \le b_\nu\)` for `\(\nu=1,\ldots,n\)`. 
* Consider the [closed][bookofproofs$852] `$n$`-dimensional cuboid `\(Q:=\{(x_1,\ldots,x_n)\in\mathbb R^n:\quad a_\nu \le x_\nu \le b_\nu\}\)`.
* It has to be shown that `\(Q\)` is a [compact][bookofproofs$6575] [subset][bookofproofs$552] of the [`\(n\)`-dimensional metric space of real numbers][bookofproofs$1206] `\(\mathbb R^n\)`.
   * Take any [open cover][bookofproofs$150] of `\((U_i)_{i\in I}\)` of `\(Q\)`.
   * Assume, there is no finite subcover `\(U_{i_k}\)` of `\(Q\)`.
      * Set `\(Q_0:=Q\)`, and `$I_{0,\nu}=[a_\nu,b_\nu]$`, where `$I_{0,\nu}$` are [closed real intervals][bookofproofs$1153] for `\(\nu=1,\ldots,n\)`. Note that `$Q_0=I_{0,1}\times\ldots\times I_{0,n}$`.
      * Bisect `$I_{0,\nu}$` by setting `$$I_{1,\nu}^L=\left[a_\nu,\frac {b_\nu-a_\nu}2\right],\quad I_{1,\nu}^R=\left[\frac {b_\nu-a_\nu}2, b_\nu,\right],$$` such that `$I_{0,\nu}=I_{1,\nu}^L\cup I_{1,\nu}^R$`, for `\(\nu=1,\ldots,n\)`.
      * From the bisected intervals, we can construct `$2^n$` new cuboids `$$Q_1^{(s_1,s_2,\ldots,s_n)}=I_{1,1}^{s_1}\times\ldots\times I_{1,n}^{s_n},\quad\quad ( * )$$` such that `$s_\nu$` assumes the values `\(L\)` for `$I_{1,\nu}^L$` or `$R$` for `$I_{1,\nu}^R$`, and `\(\nu=1,\ldots,n\)`.
      * Because, by assumption, `\(Q_0\)` has no finite subcover, there is at least one cuboid out of the `$2^n$` cuboids in `$ ( * )$`, which has no finite subcover. Let this cuboid be denoted by `\(Q_1\)`.
      * Please note that `$$\operatorname{diam}(Q_1)=\frac 12\operatorname{diam}(Q_0),$$` i.e. the [diameter][bookofproofs$6581] of `\(Q_1\)` is half the diameter of `\(Q_0\)`.
      * We can repeat this construction by finding even smaller cuboids, `\(Q_2,Q_3,\ldots\)` such that for `\(m\ge 1\)` they have the following two properties:
         * `$Q_m$` has no finite subcover, 
         * `$\operatorname{diam}(Q_m)=\frac 12\operatorname{diam}(Q_{m-1})=\frac 1{2^{m}}\operatorname{diam}(Q_{0})$`, and
         * `$Q_{m-1}\supset Q_m$`.
      * According to the [nested closed subset theorem][bookofproofs$127], there is a point `\(a\)` with `\(a\in Q_{m}\)` for all `\(m\in\mathbb N\)`.
      * Since `\((U_i)_{i\in I}\)`  is an  [open cover][bookofproofs$150] of of `\(Q\)`, there is an index `\(i_a\in I\)` such that `\(a\in U_{i_a}\)`. 
      * Because `$U_{i_a}$` is [open][bookofproofs$852], it is a [neighborhood][bookofproofs$849] of `\(a\)`.
      * Therefore there is an `\(\epsilon > 0\)` such that the [open ball][bookofproofs$849] `\(B(a,\epsilon)\)` is contained in `$U_{i_a}$`.
      * Take `\(m\)` big enough, such that `$\operatorname{diam}Q_m < \epsilon$`.
      * Because `$a\in Q_m$`, we have the inclusion chain
`$$Q_m\subset B(a,\epsilon)\subset U_{i_a}.$$`
      * This [contradicts][bookofproofs$744] that `$Q_m$` has no finite subcover.
      * This contradicts, that `$Q$` has no finite subcover.
   * Thus, `$Q$` has a finite subcover for any given [open cover][bookofproofs$150] of `\((U_i)_{i\in I}\)` of `\(Q\)`.
   * Thus, `\(Q\)` is a [compact][bookofproofs$6575] [subset][bookofproofs$552] of the [`\(n\)`-dimensional metric space of real numbers][bookofproofs$1206] `\(\mathbb R^n\)`.

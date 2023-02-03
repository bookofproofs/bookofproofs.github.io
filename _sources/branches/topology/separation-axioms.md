layout: axiom
categories: branches,topology
nodeid: bookofproofs$6199
orderid: 50
parentid: bookofproofs$8621
title: Separation Axioms
description: SEPARATION AXIOMS ★ bring your math skills to the graduate level ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$8336,bookofproofs$8560,bookofproofs$8613
keywords: separation axiom,separation axioms,kolmogorov space,frechet space,hausdorff space,vietoris space,tietze space,kolmogorov spaces,frechet spaces,hausdorff spaces,vietoris spaces,tietze spaces,t0 space,t1 space,t2 space,t3 space
contributors: bookofproofs


---


---

Let `$(X,\mathcal O)$` be a [topological space][bookofproofs$6189] `$X$` can be postulated to fulfill the following **separation axioms**:

### Kolmogorov Space `$T_0$`

Among any two different points only one has an open set containing it, formally `$$a,b\in X, a\neq b\Longrightarrow \exists O\in\mathcal O:\; (a\in O, b\not\in O)\vee (a\not\in O, b\in O).$$` In this case, `$X$` is called a **Kolmogorov space** ([Andrey Kolmogorov](https://mathshistory.st-andrews.ac.uk/Biographies/Kolmogorov/) (1903 - 1987)).


![separationt0](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/examples/separationt0.png?raw=true)


### Fréchet Space `$T_1$`

Among any two different points both have an open set containing only this point but not the other, formally `$$a,b\in X, a\neq b\Longrightarrow \exists O_a,O_b\in\mathcal O:\; (a\in O_a, b\not\in O_a)\wedge (a\not\in O_b, b\in O_b).$$` In this case, `$X$` is called a *Fréchet space* ([René Maurice Fréchet](https://mathshistory.st-andrews.ac.uk/Biographies/Frechet/) (1878 - 1973)).


![separationt1](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/examples/separationt1.png?raw=true)


### Hausdorff Space `$T_2$`

Two distinct points have to distinct open sets containing them, formally 
`$$a,b\in X, a\neq b\Longrightarrow \exists O_a,O_b\in\mathcal O:\; (a\in O_a)\wedge (b\in O_b)\wedge (O_a\cap O_b=\emptyset).$$` In this case, `$X$` is called a **Hausdorff space** 
([Felix Hausdorff](https://mathshistory.st-andrews.ac.uk/Biographies/Hausdorff/) (1868 - 1942)).


![separationt2](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/examples/separationt2.png?raw=true)


### Vietoris Space `$T_3$`

For every [closed set][bookofproofs$853] and every point not contained in it there are open sets containing them respectively, formally 
`$$x\not\in U\subset X\Longrightarrow \exists O_U,O_x\in\mathcal O:\; (U\subset O_U)\wedge (x\in O_x).$$` 
In this case, `$X$` is called a **Vietoris space** ([Leopold Vietoris](https://mathshistory.st-andrews.ac.uk/Biographies/Vietoris/) (1891 - 2002)).


![separationt3](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/examples/separationt3.png?raw=true)


### Tietze Space `$T_4$`

For any two disjoint [closed sets][bookofproofs$853] there are disjoint open sets containing them, formally 
`$$U,W\subset X\text{ closed }, U\cap W=\emptyset \Longrightarrow \exists O_U,O_W\in\mathcal O:\; (U\subset O_U)\wedge (W\subset O_W)\wedge (O_U\cap O_W=\emptyset).$$` 
In this case, `$X$` is called a **Tietze space** ([Franz Tietze](https://mathshistory.st-andrews.ac.uk/Biographies/Tietze/) (1880 - 1964)).


![separationt4](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/examples/separationt4.png?raw=true)


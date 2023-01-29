layout: proposition
categories: branches,geometry,euclidean-geometry,elements-euclid,book--8-continued-proportion
nodeid: bookofproofs$2023
orderid: 300
parentid: bookofproofs$1880
title: 8.04: Construction of Sequence of Numbers with Given Ratios
description: 8.04: CONSTRUCTION OF SEQUENCE OF NUMBERS WITH GIVEN RATIOS ★ graduate maths ✔ step by step ✚ visit BookOfProofs now!
references: bookofproofs$6419,bookofproofs$6908
keywords: construction,given,numbers,ratios,sequence
contributors: bookofproofs,@fitzpatrick

---


---

### (Proposition 4 from Book 8 of Euclid's “Elements”)

> For any multitude whatsoever of given [ratios][bookofproofs$1943], (expressed) in the least [numbers][bookofproofs$2315], to find the least [numbers][bookofproofs$2315] in [continued proportion][bookofproofs$6552] in these given [ratio][bookofproofs$1943].
* Let the given [ratio][bookofproofs$1943], (expressed) in the least [numbers][bookofproofs$2315], be the [ (ratios) ][bookofproofs$1943] of `$A$` to `$B$`, and of `$C$` to `$D$`, and, further, of `$E$` to `$F$`.
* So it is required to find the least [numbers][bookofproofs$2315] in [continued proportion][bookofproofs$6552] in the [ratio][bookofproofs$1943] of `$A$` to `$B$`, and of `$C$` to `$B$`, and, further, of `$E$` to `$F$`.


![fig04e](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/euclid/Book08/fig04e.png?raw=true)


### Modern Formulation

Let the [proportions][bookofproofs$2328] `$\frac AB,$` `$\frac CD,$` and `$\frac EF$` be given. It is to find least numbers `$N,O,M,P$` with `$\frac AB=\frac NO,$` `$\frac CD=\frac OM,$` and `$\frac EF=\frac MP.$`   

### Euclidean Algorithm to construct such a sequence of numbers 

To continue the continued proportion `$$\cfrac{a}{\cfrac{\vdots}{b}}$$` with the ratio `$\frac cd.$`
* Multiply each of the numbers in the proportion by `$\frac{\operatorname{lcm}(b,c)}{b}$`
* Continue the proportion with the number `$\frac{d\cdot \operatorname{lcm}(b,c)}{c}.$`

### Examples

To take `$\cfrac{4}{5}$` and continue it by `$\cfrac 23.$`
* Factor to multiply all numbers with: `$\frac{\operatorname{lcm}(5,2)}{5}=\frac{10}{5}=2.$`
* It follows `$\cfrac{4\cdot 2}{5\cdot 2}=\cfrac{8}{10}.$` 
* New number to continue with: `$\frac{3\cdot \operatorname{lcm}(5,2)}{2}=\frac{3\cdot 10}{2}=15.$`
* New continued proportion: `$$\cfrac{8}{\cfrac{10}{15}}.$$`

To take `$\cfrac{8}{\cfrac{10}{15}}$` and continue it by `$\cfrac 47.$`
* Factor to multiply all numbers with: `$\frac{\operatorname{lcm}(15,4)}{15}=\frac{60}{15}=4.$`
* It follows `$$\cfrac{8\cdot 4}{\cfrac{10\cdot 4}{15\cdot 4}}=\cfrac{32}{\cfrac{40}{60}}.$$` 
* New number to continue with: `$\frac{7\cdot \operatorname{lcm}(15,4)}{4}=\frac{7\cdot 60}{4}=105.$`
* New continued proportion: `$$\cfrac{32}{\cfrac{40}{\cfrac{60}{105}}}.$$`

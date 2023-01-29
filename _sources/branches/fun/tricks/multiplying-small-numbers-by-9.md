layout: example
categories: branches,fun,tricks
nodeid: bookofproofs$599
orderid: 0
parentid: bookofproofs$598
title: Multiplying small numbers by 9
description: MULTIPLYING SMALL NUMBERS BY 9 &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: 
keywords: multiplying,numbers,on the left side,on the right side,small,tenner,the ones
contributors: bookofproofs

---


---

If you want to multiply `\(n\times 9\)`, `\(n\in\{1,2,\ldots,10\}\)`, you do not have to memorize all 10 results. The trick is to look at your hands, find the `\(n\)`th-finger, and mentally split your 10 fingers into two groups: 

* first group being **on the left side** of your `\(n\)`th-finger (can be none, if `\(n=1\)`),
* second group being **on the right side** of your `\(n\)`th-finger (can be none, if `\(n=10\)`).

The following figures demonstrate this principle for `\(n=1,2,3\)` and `\(4\)`, respectively:

![recon1](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_assets/images/examples/recon1.png?raw=true) ![recon2](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_assets/images/examples/recon2.png?raw=true)

![recon3](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_assets/images/examples/recon3.png?raw=true) ![recon4](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_assets/images/examples/recon4.png?raw=true)

As you can see, the blue-marked fingers are **the ones** of the result, the orange-marked fingers are the **tenner** part of the result. The results above are:

* `\(1\times 9=9\Rightarrow\)`  zero tenner and nine ones in the left-upper figure,
* `\(2\times 9=18\Rightarrow\)`  one tenner and eight ones in the right-upper figure,
* `\(3\times 9=27\Rightarrow\)`  two tenner and seven ones in the left-bottom figure,
* `\(4\times 9=36\Rightarrow\)`  three tenner and six ones in the right-bottom figure.
* ...
* `\(n\times 9\Rightarrow\)`  `\(n-1\)` tenner and `\(10-n\)` ones 

#### Why does it work?

This works, since `\(n-1\)` tenner and `\(10-n\)` ones means:
`\[(n-1)\times 10 + (10-n)=10n - 10 + 10 - n=n\times 9. \]`

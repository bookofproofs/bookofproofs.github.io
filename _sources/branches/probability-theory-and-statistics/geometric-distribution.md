layout: proposition
categories: branches,probability-theory-and-statistics
nodeid: bookofproofs$429
orderid: 200
parentid: bookofproofs$324
title: Geometric Distribution
description: GEOMETRIC DISTRIBUTION &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: 
keywords: distribution,geometric,geometric distribution
contributors: bookofproofs

---


---

We repeat a [Bernoulli experiment][bookofproofs$1812] (if necessary, infinitely many times). Each time, we observe, if an [event][bookofproofs$857] `\(A\)` occurred or not. Let the probability of `\(A\)` to occur be constantly `\(p:=p(A)\)` during each repetition of the experiment. Let `\(X\)` be the [random variable][bookofproofs$1813] having the realization `\(k\)`, if and only if we observe `\(A\)` for the first time at `\(k\)`-th repetition of the experiment. Then, the [probability mass function][bookofproofs$1824] is given by 


`\[p(X = k)=\begin{cases}
p(1-p)^{k-1}&\text{for }k=1,2,3,\ldots \\\\
0&\text{else.}\end{cases}\]`

The **geometric distribution** (i.e. the [probability distribution][bookofproofs$1815] of the random variable `\(X\)`) is given by

`\[\begin{array}{rcll}
p(X \le x)&=&0&\text{for }x < 1\\
p(X \le x)&=&\sum_{k=1}^{k=x}p(1-p)^{k-1}&\text{for }1\le x 
\end{array}\]`

In the following interactive you can change the probability  `\(p\)` of observing an event `\(A\)` in a Bernoulli experiment repeated up to `\(30\)` times. Changing this probability will change the probability mass function for different values of `\(X\)` (red) of observing `\(A\)` exactly in the `\(k\)`-th repetition, and the probability distribution (blue):


<div id="box15328" class="jxgbox centered" style="max-width:500px; width:100%; height:500px;"></div>

<div id="box15328a" class="jxgbox centered" style="max-width:500px; width:100%;  height:100px;"></div>

§§§1

---

§§§1

<script type="text/javascript">
var brd1 = JXG.JSXGraph.initBoard('box15328a', {boundingbox: [-0.1, 0, 1.5, -4], showNavigation:false, showCopyright: false, axis:false});
var prob = brd1.create('slider',[[0,-2],[1,-2],[0,.5,1]], {name:'p'});


var brd = JXG.JSXGraph.initBoard('box15328', {boundingbox: [-1.5, 1.1, 31, -.1], axis:true, showCopyright:false});

brd1.addChild(brd);

var p1 = brd.create('point', [1, function() {return geometric(1, prob.Value());}], {name:''});
var p2 = brd.create('point', [2, function() {return geometric(2, prob.Value());}], {name:''});
var p3 = brd.create('point', [3, function() {return geometric(3, prob.Value());}], {name:''});
var p4 = brd.create('point', [4, function() {return geometric(4, prob.Value());}], {name:''});
var p5 = brd.create('point', [5, function() {return geometric(5, prob.Value());}], {name:''});
var p6 = brd.create('point', [6, function() {return geometric(6, prob.Value());}], {name:''});
var p7 = brd.create('point', [7, function() {return geometric(7, prob.Value());}], {name:''});
var p8 = brd.create('point', [8, function() {return geometric(8, prob.Value());}], {name:''});
var p9 = brd.create('point', [9, function() {return geometric(9, prob.Value());}], {name:''});
var p10 = brd.create('point', [10, function() {return geometric(10, prob.Value());}], {name:''});
var p11 = brd.create('point', [11, function() {return geometric(11, prob.Value());}], {name:''});
var p12 = brd.create('point', [12, function() {return geometric(12, prob.Value());}], {name:''});
var p13 = brd.create('point', [13, function() {return geometric(13, prob.Value());}], {name:''});
var p14 = brd.create('point', [14, function() {return geometric(14, prob.Value());}], {name:''});
var p15 = brd.create('point', [15, function() {return geometric(15, prob.Value());}], {name:''});
var p16 = brd.create('point', [16, function() {return geometric(16, prob.Value());}], {name:''});
var p17 = brd.create('point', [17, function() {return geometric(17, prob.Value());}], {name:''});
var p18 = brd.create('point', [18, function() {return geometric(18, prob.Value());}], {name:''});
var p19 = brd.create('point', [19, function() {return geometric(19, prob.Value());}], {name:''});
var p20 = brd.create('point', [20, function() {return geometric(20, prob.Value());}], {name:''});
var p21 = brd.create('point', [21, function() {return geometric(21, prob.Value());}], {name:''});
var p22 = brd.create('point', [22, function() {return geometric(22, prob.Value());}], {name:''});
var p23 = brd.create('point', [23, function() {return geometric(23, prob.Value());}], {name:''});
var p24 = brd.create('point', [24, function() {return geometric(24, prob.Value());}], {name:''});
var p25 = brd.create('point', [25, function() {return geometric(25, prob.Value());}], {name:''});
var p26 = brd.create('point', [26, function() {return geometric(26, prob.Value());}], {name:''});
var p27 = brd.create('point', [27, function() {return geometric(27, prob.Value());}], {name:''});
var p28 = brd.create('point', [28, function() {return geometric(28, prob.Value());}], {name:''});
var p29 = brd.create('point', [29, function() {return geometric(29, prob.Value());}], {name:''});
var p30 = brd.create('point', [30, function() {return geometric(30, prob.Value());}], {name:''});


var f = brd.create('functiongraph',[function(x){ 
  var dist=0;
  
  for (n=1; lt(n, 30 + 1); n++) {
    if (lt(x , n)) {
      return dist;
    } 
    dist=dist+geometric(n, prob.Value());
  }
  return dist; 
}]);


function geometric(k, p) {
    var coeff = p
    for (var x = 1; lt(x,k); x++) {
      coeff *= (1-p);
    }
    return coeff;
}



</script>


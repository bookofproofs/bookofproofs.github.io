layout: proposition
categories: branches,probability-theory-and-statistics
nodeid: bookofproofs$450
orderid: 300
parentid: bookofproofs$324
title: Binomial Distribution
description: BINOMIAL DISTRIBUTION &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$856,bookofproofs$1796
keywords: binomial,binomial distribution,distribution
contributors: bookofproofs

---


---

We repeat a [Bernoulli experiment][bookofproofs$1812] `\(n\)` times. Each time, we observe, if an [event][bookofproofs$857] `\(A\)` occurred or not. Let the probability of `\(A\)` to occur be constantly `\(p:=p(A)\)` during each repetition of the experiment. Let `\(X\)` be the [random variable][bookofproofs$1813] counting the number `\(k\)` of the realizations of `\(A\)`. Clearly, `\(A\)` can occur for `\(k\)` times with `\(0\le k\le n\)`. The [probability mass function][bookofproofs$1824] of `\(A\)` occurring exactly `\(k\)` times is given by 


`\[p(X = k)=\begin{cases}
\binom nk p^k(1-p)^{n-k}&\text{for }k=0,1,\ldots n\\\\
0&\text{else.}\end{cases}\]`


The **binomial distribution** (i.e. the [probability distribution][bookofproofs$1815] of the random variable `\(X\)`) is given by

`$$\begin{array}{rcll}
p(X \le x)&=&0&\text{for }x < 0\\
p(X \le x)&=&\sum_{k=0}^{k=x}\binom nk p^k(1-p)^{n-k}&\text{for }0\le x < n\\
p(X \le x)&=&1&\text{for }x \ge n\\
\end{array}$$`

In the following interactive you can change the probability  `\(p\)` of observing an event `\(A\)` in a Bernoulli experiment repeated `\(20\)` times. Changing this probability will change the probability mass function for different values of `\(X\)` (red) of observing `\(A\)` from `\(0\)` to `\(20\)` times and the probability distribution (blue):

<div id="box15329" class="jxgbox centered" style="max-width:500px; width:100%; height:500px;"></div>
<div id="box15329a" class="jxgbox centered" style="max-width:500px; width:100%; height:100px;"></div>

	 

§§§1

---

§§§1


<script type="text/javascript">
try{
var brd1 = JXG.JSXGraph.initBoard('box15329a', {boundingbox: [-0.1, 0, 1.5, -4], showNavigation:false, showCopyright: false, axis:false});
var prob = brd1.create('slider',[[0,-2],[1,-2],[0,.5,1]], {name:'p'});

var brd = JXG.JSXGraph.initBoard('box15329', {boundingbox: [-1, 1.1, 21, -.1], axis:true, showCopyright:false});

brd1.addChild(brd);

var p0 = brd.create('point', [0, function() {return binomial(20, 0, prob.Value());}], {name:''});
var p1 = brd.create('point', [1, function() {return binomial(20, 1, prob.Value());}], {name:''});
var p2 = brd.create('point', [2, function() {return binomial(20, 2, prob.Value());}], {name:''});
var p3 = brd.create('point', [3, function() {return binomial(20, 3, prob.Value());}], {name:''});
var p4 = brd.create('point', [4, function() {return binomial(20, 4, prob.Value());}], {name:''});
var p5 = brd.create('point', [5, function() {return binomial(20, 5, prob.Value());}], {name:''});
var p6 = brd.create('point', [6, function() {return binomial(20, 6, prob.Value());}], {name:''});
var p7 = brd.create('point', [7, function() {return binomial(20, 7, prob.Value());}], {name:''});
var p8 = brd.create('point', [8, function() {return binomial(20, 8, prob.Value());}], {name:''});
var p9 = brd.create('point', [9, function() {return binomial(20, 9, prob.Value());}], {name:''});
var p10 = brd.create('point', [10, function() {return binomial(20, 10, prob.Value());}], {name:''});
var p11 = brd.create('point', [11, function() {return binomial(20, 11, prob.Value());}], {name:''});
var p12 = brd.create('point', [12, function() {return binomial(20, 12, prob.Value());}], {name:''});
var p13 = brd.create('point', [13, function() {return binomial(20, 13, prob.Value());}], {name:''});
var p14 = brd.create('point', [14, function() {return binomial(20, 14, prob.Value());}], {name:''});
var p15 = brd.create('point', [15, function() {return binomial(20, 15, prob.Value());}], {name:''});
var p16 = brd.create('point', [16, function() {return binomial(20, 16, prob.Value());}], {name:''});
var p17 = brd.create('point', [17, function() {return binomial(20, 17, prob.Value());}], {name:''});
var p18 = brd.create('point', [18, function() {return binomial(20, 18, prob.Value());}], {name:''});
var p19 = brd.create('point', [19, function() {return binomial(20, 19, prob.Value());}], {name:''});
var p20 = brd.create('point', [20, function() {return binomial(20, 20, prob.Value());}], {name:''});


var f = brd.create('functiongraph',[function(x){ 
  var dist=0;
  for (n=1;  lt(n , 21); n++) {
    if (lt(x,n)) {
      return dist;
   } 
    dist=dist+binomial(20, n, prob.Value());
  }
 return dist; 
}]);

} catch(err) {

}

function binomial(n, k, p) {
var p1=1;
var p2=1;

var logf = [0, 0, 0.693147180559945,1.79175946922806,3.17805383034795,4.78749174278205,6.5792512120101,8.52516136106541,10.6046029027453,12.8018274800815,15.1044125730755,17.5023078458739,19.9872144956619,22.5521638531234,25.1912211827387,27.8992713838409,30.6718601060807,33.5050734501369,36.3954452080331,39.3398841871995,42.3356164607535,45.3801388984769,48.4711813518352,51.6066755677644,54.7847293981123,
58.0036052229805,61.261701761002,64.5575386270063,67.8897431371815,71.257038967168,74.6582363488302,78.0922235533153,81.5579594561151,85.0544670175815,88.5808275421977,92.1361756036871,95.7196945421432,99.3306124547874,102.968198614514,106.631760260643];

coeff= Math.exp(logf[n] - logf[n-k] - logf[k]);

    for (x=0; lt(x,k); x++) {
       coeff*=p;
    }
    for (x=0; lt(x,n-k); x++) {
       coeff*=(1-p);
    }
    return coeff;
}

</script>



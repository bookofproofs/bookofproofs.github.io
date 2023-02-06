layout: explanation
categories: branches,theoretical-physics, special-relativity
nodeid: bookofproofs$6299
orderid: 100
parentid: bookofproofs$6297
title: Einstein's Interpretation of the Time Dilation
description: EINSTEIN'S INTERPRETATION OF THE TIME DILATION &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: 
keywords: dilation,einstein,interpretation,time
contributors: bookofproofs


---


---

Imagine, Alice and Bob have two metronomes ticking at a constant rate of one second. We assume that the metronomes are perfectly constructed to measure the duration of a second. They are both traveling in two separate vehicles moving relatively to each other at a constant speed `\(v\)`. The [time dilation][bookofproofs$6297] was formulated by [Albert Einstein][bookofproofs$Einstein] (1879 - 1955) in the formula 
`\[t_A=t_B\frac 1{\sqrt{1-\frac {v^2}{c^2}}},\quad\quad (0\le v < c)\]`
where 
* `\(t_A\)` denotes the duration of one tick of the metronome as measured by Alice in her vehicle, which is one second `\(1s\)`,
* `\(t_B\)` denotes the duration of one tick of the metronome as measured by Bob in his vehicle, which, again, is one second `\(1s\)`,
* `\(v\)` denotes the constant speed, at which both vehicles are moving relatively to each other,
* `\(c\)` denotes the constant speed of light.

This formula can be interpreted as follows: If Bob decides to send Alice a light signal, whenever he hears his metronome ticking, the faster both vehicles move relatively to each other, the more will be the difference of the tick rate Alice hears according to her metronome as compared to the light signals reflecting the tick rate of the metronome of Bob.

For instance, if both vehicles do not move at all relatively to each other (which is the special case `\(v=0\)`), Alice won't observe any difference in both tick rates:

`\[t_A=t_B\frac 1{\sqrt{1-0}}=t_B.\]`

If the vehicles move at speeds, which we experience on a day-to-day basis (e.g. like cars, trains), it turns out that Alice won't realize any significant difference. For instance, at a speed of `\(300\,km/h\)`, Alice would have to wait about `\(820,000\)` years to realize that both metronomes differ by one second. 

The effect will, however, become noticeable by Alice, if the vehicles move at much higher speeds. E.g., if the speed corresponds to `\(60\)`% of the speed of light `\(c\)` (which equals to about `\(658\)` million `\(km/h\)`), the time dilation is

`\[t_A=t_B\frac 1{\sqrt{1-0.36}}=t_B\frac 1{\sqrt{0.64}}=t_B\frac 1{0.8}=t_B\cdot 1.25.\]`

In this case, Bob's time goes by the rate of `\(1.25\)` slower than this of Alice's. In other words, Alice would realize `\(5\)` ticks of her metronome, but only `\(4\)` ticks of Bob's metronome. 

The rate of time dilation is increasing very quickly, as the relative speed of both vehicles comes closer and closer to the speed of light `\(c\)`. For instance, at the speed of `\(0.9c\)`, the dime dilation rate is `\(2.29\)`, at `\(0.99c\)`, this rate is about `\(7\)`, at `\(0.999c\)`, the rate is already about `\(22\)`, etc. 

However, Einstein concluded that both vehicles would never move relatively to each other at the speed of light `\(v=c\)`. In this case, the Lorentz factor diverges to infinity
`\[\lim_{v\uparrow c}\frac 1{\sqrt{1-\frac {v^2}{c^2}}}=\infty.\]`
For `\(v=c\)`, the formula would loose any mathematical sense, since it is not possible to divide by zero[^1]. Albert Einstein and many authors interpreted this as a "rule of physics" that "nothing can travel faster than light".

[^1]: To see why it is not possible to divide by zero see a [separate article][bookofproofs$596].
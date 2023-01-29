layout: explanation
categories: branches,probability-theory-and-statistics
nodeid: bookofproofs$860
orderid: 100
parentid: bookofproofs$857
title: How to Interpret Events Which Are Constructed From Other Events Doing Set Operations?
description: HOW TO INTERPRET EVENTS WHICH ARE CONSTRUCTED FROM OTHER EVENTS DOING SET OPERATIONS? &#9733; master graduate maths &#10004; visit BookOfProofs now!
references: bookofproofs$856
keywords: are,constructed,doing,events,how,interpret,interpretation of,not,operations,other,set,which
contributors: bookofproofs

---


---

Since the [probability space][bookofproofs$857] `\(\Omega\)` and any event `\(A\subseteq \Omega\)` are defined as sets, all [operations applicable to sets][bookofproofs$552], (e.g. union `\(A\cup B\)`, intesection `\(A\cap B\)`, complement `\(\overline A\)`, etc.), are also applicable to events.

Therefore, it is notable that we can construct events from other events by combining them with set operations. The following table gives some answers and examples to the question, how these new events can be interpreted.


#### Event Intersection 


![venn1](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/examples/venn1.png?raw=true)

*Interpretation of* `\(A \cap B\)`: The event that both events `\(A\)` and `\(B\)` occur at once, e.g.:

> `\(A=\)` "It is raining.", 
`\(B=\)`  "Today is my birthday." 
`\(A \cap B=\)` "It is raining **AND** today is my birthday."

#### Empty Event Intersection 


![venn5](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/examples/venn5.png?raw=true)

*Interpretation of* `\(A \cap B=\emptyset\)`: The impossible event, i.e. that the mutually exclusive events `\(A\)` and `\(B\)` occur at once, e.g.:

> `\(A=\)` "It is raining.", 
`\(B=\)`  "The street is dry." 
`\(A \cap B=\)` "It is raining **AND** the street is dry."


#### Event Difference 


![venn2](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/examples/venn2.png?raw=true)

*Interpretation of* `\(A\setminus B\)`: The event, when exactly `\(A\)` occurs and `\(B\)` does not occur, e.g.:

> `\(A=\)` "It is raining.", 
`\(B=\)`  "The street is dry." 
`\(A \setminus B=\)` "It is raining **AND** the street is **NOT** dry."

#### Event Union


![venn3](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/examples/venn3.png?raw=true)

*Interpretation of* `\(A \cup B\)`: The event that `\(A\)` occurs or `\(B\)` occurs, or both of them at once occur, e.g.:

> `\(A=\)` "It is raining.", 
`\(B=\)`  "The street is dry." 
`\(A \setminus B=\)` "It is raining **OR** the street is dry  **OR** both)."


#### Complementary Event 


![venn4](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/examples/venn4.png?raw=true)

*Interpretation of* `\(\overline A\)`: The event that `\(A\)` does not occur, e.g.:

> `\(A=\)` "It is raining.", 
`\(\overline A=\)` "It is **NOT** raining."

#### Included Event


![venn6](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/examples/venn6.jpg?raw=true)

*Interpretation of* `\(A\subseteq B\)`: If the event `\(A\)` occurs then certainly also `\(B\)` occurs, e.g.:

> `\(A=\)` "It is raining.", 
`\(B=\)`  "The street is wet." 
`\(A \subseteq B=\)` "The street is wet **if** it is raining."

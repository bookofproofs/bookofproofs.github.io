# Layouts

Each page of <strong><span style='color:orange'>Bo</span><span style='color:lightblue'>P</span></strong> has a layout. 
The following layouts are possible: 

Layout | Meaning | Usage  
:----  | :----  | :----   
default|Default layout|Main pages of  <strong><span style='color:orange'>Bo</span><span style='color:lightblue'>P</span></strong>
root|Root node|First pages within each main category
branch|Branch node|First page of each mathematical branch
hidden|Hidden node|Stores the global list of references
index| |Dynamic index sites
part| |First page of a part
chapter| |First page of a chapter
section| |First page of a section
subsection| |First page of a subsection
axiom|Building block of mathematics|
definition|Building block of mathematics|
theorem|Building block of mathematics|
lemma|Building block of mathematics|
proposition|Building block of mathematics|
corollary|Building block of mathematics|
proof|Building block of mathematics|
algorithm| |Writing algorithms in python
application| |Application examples related to another node 
example| |Generic examples related to another node
explanation| |Explanation of another node
motivation| |Motivates a mathematical concept
problem| |Mathematical problem or riddle
solution| |Solution to the problem or riddle
epoch|Historical epoch|Lists chronologically the events related to mathematics
topic|Historical development of a topic|Unstructured article  

### "Common Thread" - the Structure of layouts 

<strong><span style='color:orange'>Bo</span><span style='color:lightblue'>P</span></strong> facilitates mathematical education. Contributors and authors can organize their posts from "easy" to "more difficult" mathematical concepts.
Unlike wiki pages in which each article is self-contained and widely independent from other articles,
the sites of <strong><span style='color:orange'>Bo</span><span style='color:lightblue'>P</span></strong> follow a "common thread". 


Visitors can navigate through all pages like they would in a book, turning its pages. 

Contributors determine this order of pages by defining a tree of nested pages with different layouts. In other words, 
all sites of <strong><span style='color:orange'>Bo</span><span style='color:lightblue'>P</span></strong> are organized into trees of nodes.
The combination of the above properties (`parentid`, `nodeid`) defines a parent-child relationship inside each tree.
The property `orderid` in the front matter defines the relative order of children of each parent.  

Technically speaking, the "common thread" (predecessor-successor) order of the pages is the same as the nodes of each tree, as they would be visited by a computer visiting them in a pre-order.

Currently, there are only three root nodes (i.e., with `layout: root`): 
* Branches: `nodeid: bookofproofs$0`, 
* History: `nodeid: bookofproofs$2`, and
* Index: `nodeid: bookofproofs$i`.

The current pre-order is visualized in the [tree-index published here][ti] 

[ti]:https://bookofproofs.github.io/index/tree-index.html

## Nesting layouts

When relating a node to its parent node by setting its `parentid` property in the front matter, there are allowed and not allowed combinations of layout combinations.
For instance:
* A node with the `section` layout might be the parent of a node with the `subsection` layout but not vice versa. 
* It only makes sense to provide a `proof` as a child of a `theorem`, but not of a `definition`, etc. 
* There might be a `corollary` to a `theorem` but not a `corollary` to an `explanation`.  
* etc.

The compiler will log any violations of such rules, e.g., like 
```
   Validating layout nesting
      Issues with ['definition->definition']
      (were added to ['bookofproofs$1068', 'bookofproofs$6213'])
```
These violations should be resolved before you make a pull request for your contributions.

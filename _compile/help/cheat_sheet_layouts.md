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

The layout property will influence the title of your page. For instance, the front matter

    layout: definition
    ...
    title: Order Of Natural Numbers 

would result in the following title of the published page: 

> "Definition: Order Of Natural Numbers"

Moreover, the layout will influence the building block, under which users will find your page in the published
[building blocks index][bbi]. 

[bbi]:https://bookofproofs.github.io/index/bb-index.html

## Nesting layouts

When relating a node to its parent node by setting its `parentid` property in the front matter (compare )

, there are allowed and not allowed combinations of layout combinations.
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

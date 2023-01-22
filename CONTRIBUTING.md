# How it works?

<strong><span style='color:orange'>Bo</span><span style='color:lightblue'>P</span></strong> uses markdown 
templates in `_sources` for each site published at https://bookofproofs.github.io/. The templates work similarly 
to JeKyll (if you are already familiar with it). 

However, we compile the markdown files into html using PYTHON scripts in the `_compile` folder. The reason why we do not use JeKill and 're-invent' the wheel is more flexibility to incorporate some features 
to improve user experience to read and/or contribute new mathematical content. Features improving the user-experience 
include, but are not limited to:

* [Mathjax][mj] 
* [JSXGraph][jx]
* [Sagecell][sc]
* Dynamic sites containing indices of the contents
* Dynamic RSS feeds
* Dynamic search with autocomplete

[mj]:https://www.mathjax.org
[jx]:https://jsxgraph.uni-bayreuth.de/wiki/index.php/Category:Examples
[sc]:https://sagecell.sagemath.org/

# Getting started

To contribute to the site, follow these generic steps:

1. Clone the repository. 
2. Change the following constant in the script `_compile/_templates/BopCompiler.py` to `True`:
```python
class BopCompiler:
    local = False
```
3. Add new or amend existing markdown files.
4. Run `_compile/_templates/main.py`. Before this step, you might be required to install some missing python packages using pip.
5. Control the result in your browser. If something is still not the way you want it, repeat steps 3-4.

Once you are ready with your editions: 

6. Change the constant in the script `_compile/_templates/BopCompiler.py` back to `False`.
7. Recompile (like in step 4).
8. Add to git any new files you added in the folder `_sources/` or its subfolders.
9. Commit and push to a new branch and make a change request.

# Using the templates
## Sections of the templates
### Overview (Example)
The templates usually consist of three (3) sections separated by `---`. A typical template looks like this:

```
layout: part
categories: branches,algebra
nodeid: bookofproofs$85
orderid: 1
parentid: bookofproofs$59
title: Algebraic Structures - Overview
description: ALGEBRAIC STRUCTURES OVERVIEW ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: 
keywords: algebraic structures overview
contributors: bookofproofs
---
<optional intro>
---
<your content>
```

In some cases you might need a 4th section separated from the other three by another `---`.

```
---
<optional script list> 
```

### Properties in Front Matter


The first section is the so-called *front matter*. Here you put a list of properties of your template. 
These properties tell the compiler to process your markdown file specifically. Some properties are optional, 
some mandatory, depending on the property `layout`. 

The following table explains which properties are where possible
and what they mean:

Property | Meaning | Possible values | Example 
:-----|:------ |:------ |:------ 
`layout`|Determines the type of a single <strong><span style='color:orange'>Bo</span><span style='color:lightblue'>P</span></strong> site|see below|`layout: theorem`
`categories`|Subject-related structure of the website|comma-separated list of categories|branches, algebra, galois-theory
`contributors`|Attribution to contributors of the site|comma-separated list of github user names (names of non-github contributors have to be marked with `@`|bookofproofs, @Fitzpatrick|
`description`|Content if the `description` attribute of the HTML `meta` tag of the site|| 
`keywords`|Comma-separated list of keywords for the become the `keywords` attribute of the HTML `meta` tag of the site||
`title`|Title of the site||
`nodeid`|A unique, filename-independent ID of the site|The name of the creator, followed by "$" and an alphanumeric identifier|bookofproofs@392|  
`url`|Link to a license (relevant only for the layout: `layout: license`) 
`parentid`|Reference to a parent `nodeid`|same as `nodeid`|`bookofproofs$0`
`orderid`|Relative order between the children nodes of the same `parentid`|Whole number|42
`references`|References (bibliography) of the site|Comma-separated list of `nodeid`|`bookofproofs$626,bookofproofs$628, bookofproofs$6419`
`issues`|Issues related to the site (kind of to-do list)|Comma-separated list|`missing-proof, missing-content`

### Layouts

Each node <strong><span style='color:orange'>Bo</span><span style='color:lightblue'>P</span></strong> has a layout. The following layouts are possible: 

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

<strong><span style='color:orange'>Bo</span><span style='color:lightblue'>P</span></strong> facilitates mathematical educations. Contributors and authors can organize their posts from "easy" to "more difficult" mathematical concepts.
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

### Nesting layouts

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

## (to be continued)
``` { .python linenos=true linenostart=42 hl_lines="1-2 10" }
# How it works?

<strong><span style='color:orange'>BookOf</span><span style='color:lightblue'>Proofs</span></strong> uses markdown 
templates in `_sources` for each site published at https://bookofproofs.github.io/. The templates work similar 
to JeKyll (if you are already familiar with it). 

However, we compile the markdown files into html using PYTHON scripts in the `_compile` folder. The reason why we do not use JeKill and 're-invent' the wheel is more flexibility to incorporate some features 
to improve user experience to read and/or contribute new mathematical contents. Features improving the user-experience 
include, but are not limited to:

* [Mathjax][mj] 
* [JSXGraph][jx]
* [Sagecell][sc]
* Dynamic sites containig indices of the contents
* Dynamic RSS feeds
* Dynamic search with autocomplete

[mj]:https://www.mathjax.org
[jx]:https://jsxgraph.uni-bayreuth.de/wiki/index.php/Category:Examples
[sc]:https://sagecell.sagemath.org/

# Getting started

In order to contribute to the site, follow these generic steps:

1. Clone the repository. 
2. Change the following constant in the script `_compile/_templates/BopCompiler.py` to `True`:
```python
class BopCompiler:
    local = False
```
3. Add new or amend existing markdown files.
4. Run `_compile/_templates/main.py`. Before this step, you might be required to install some missing python packages using pip.
5. Control the result in your browser. If something is still not the way you want it, repeat the steps 3-4.

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


The first section is the so called front-matter. Here you list properties of your template. 
These properties tell the compiler to process your markdown file specifically.

The second 


## (to be continued)
``` { .python linenos=true linenostart=42 hl_lines="1-2 10" }
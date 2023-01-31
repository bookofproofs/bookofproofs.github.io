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

# Further Help

Please check out our cheat sheets

1. [cheat_sheet_source_files.md][cssf]
1. [cheat_sheet_attributing][csa]
1. [cheat_sheet_layouts][csl]
1. [cheat_sheet_naming_identifying_ordering][csnio]
1. [cheat_sheet_categories][csc]
1. (more cheat sheets to come)

[cssf]:https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_compile/help/cheat_sheet_source_files.md
[csa]:https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_compile/help/cheat_sheet_attributing.md
[csl]:https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_compile/help/cheat_sheet_layouts.md
[csc]:https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_compile/help/cheat_sheet_categories.md
[csnio]:https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_compile/help/cheat_sheet_naming_identifying_ordering.md

``` { .python linenos=true linenostart=42 hl_lines="1-2 10" }
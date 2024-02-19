# How it works?

<strong><span style='color:orange'>Bo</span><span style='color:lightblue'>P</span></strong> uses markdown 
templates in `_sources` for each site published at https://bookofproofs.github.io/. The templates work similarly 
to JeKyll (if you are already familiar with it). 

However, we compile the markdown files into html using PYTHON scripts in the `_compile` folder. 
The reason why we do not use JeKyll and _'re-invent'_ the wheel is more flexibility. We incorporate some features 
improving user experience, e.g.:

* [Mathjax][mj] 
* [JSXGraph][jx]
* [Sagecell][sc]
* [markdown][mp] python library
* Dynamic indices and tables of contents
* Dynamic RSS feeds
* Dynamic search with autocomplete

[mj]:https://www.mathjax.org
[jx]:https://jsxgraph.uni-bayreuth.de/wiki/index.php/Category:Examples
[sc]:https://sagecell.sagemath.org/
[mp]:https://python-markdown.github.io/

# Getting started

To contribute to the site, follow these generic steps:

1. Clone the repository. 
   1. Optional: Change the constant in the script `_compile/BopCompiler.py` to `True`:
        ```python
        class BopCompiler:
            local = False
        ``` 
      Note: this is only necessary if you want to test hyperlinks locally.
1. Add new or amend existing markdown files.
1. Run `_compile/main.py`. Before this step, you might be required to install some missing python packages using pip.
1. Control the locally generated files in your browser. The root file is `docs/index.html. 
2. If something is still not the way you want it, repeat steps 2 to 4.

Once you are ready with your editions: 

6. Change the constant in the script `_compile/BopCompiler.py` back to `False` (if you changed it in 1.i) .
7. Recompile (like in step 3).
8. Add to git any new files you added in the folder `_sources/` or its subfolders _and(!)_ any new files that were auto-generated in `docs/`. 
9. Commit and push to a new branch and make a change request.

# Further Help

Please check out our cheat sheets

1. [cheat_sheet_source_files.md](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_compile/help/cheat_sheet_source_files.md)
2. [cheat_sheet_attributing](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_compile/help/cheat_sheet_attributing.md)
3. [cheat_sheet_layouts](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_compile/help/cheat_sheet_layouts.md)
4. [cheat_sheet_naming_identifying_ordering](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_compile/help/cheat_sheet_naming_identifying_ordering.md)
5. [cheat_sheet_categories](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_compile/help/cheat_sheet_categories.md)
6. [cheat_sheet_layout_epoch](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_compile/help/cheat_sheet_layout_epoch.md)
7. [cheat_sheet_layout_topic](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_compile/help/cheat_sheet_layout_topic.md)
8. [cheat_sheet_bibliography](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_compile/help/cheat_sheet_bibliography.md)
9. [cheat_sheet_layout_person](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_compile/help/cheat_sheet_layout_person.md)
10. (more cheat sheets to come)


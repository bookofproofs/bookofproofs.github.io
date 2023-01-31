# Naming, Identifying and Ordering Pages

## Naming

When you create a new markdown file in the `_sources` folder, you have to give it a unique name. 
Because the same name will be used for publishing in of the corresponding `html` file and to make the name
search-engine-friendly, only lower-case characters and hyphens are allowed.

If this convention is not met, the following error will occur:

    BopValidationError.BopValidationError: NAMING 01:
    Illegal characters found in filename ../_sources/branches/analysis/de-moivres-identity,-complex-powers-proof.md

Together with the categories defined in the front matter of the file, the file name will be used for the 
**permalink** of the published `html` page (see [cheat_sheet_categories][csc] for more info).

[csc]:https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_compile/help/cheat_sheet_categories.md

Because of its later permalink, all source files have to be uniquely named. Even if you try to put the same source file
into different subfolders in `_sources`, you will get the following error (example):

    BopValidationError.BopValidationError: NAMING 02:
    Duplicate filename in
    ../_sources/branches/geometry/differential-geometry.md and
    ../_sources/branches/geometry/differential-geometry/differential-geometry.md

## Identifying, Relating, Ordering

In addition to the later permalink, you can influence the order in which users can navigate from one page to another or
at which they will find the page in the "Table of Contents" of its parent page. 

You can accomplish this by setting these three properties in the front matter:

    nodeid: <github-usernam>$<alphanumeric-id>
    parentid: <github-usernam>$<alphanumeric-id>
    orderid: <whole-number>

The `nodeid` should consist of the Github username of the first contributor to the page (its creator), followed by a 
dollar sign `$`, followed by an alphanumeric identifier of the page. The prefixing Github username in the `nodeid`
ensures that every contributor has her _namespace_ of page identifiers in the `nodeid`.

The `parentid` is a reference to an existing `nodeid` of another page. This can be either a page created by yourself 
(i.e. prefixed with your Github username), or a page created by some other Github contributor.

The `orderid` is simply a whole number (usually in 100 steps like 100, 200, 300, etc.).

All three identifiers, `nodeid`, `parentid`, and `orderid` in a page influence the "Table of Contents" of 
(another) page whose `nodeid` equals the referenced `parentid`. 

### Example

The file `_sources/branches/analysis/convergence-criteria-for-infinite-series-involving-products.md` has the following identifiers:

    nodeid: bookofproofs$8360
    orderid: 1300
    parentid: bookofproofs$196

There are (among others) two other pages referring to the nodeid `bookofproofs$8360` as parentid:

1. the file `_sources/branches/analysis/abel-test.md` has the following identifiers:

    nodeid: bookofproofs$8365
    orderid: 100
    parentid: bookofproofs$8360

2. the file `_sources/branches/analysis/dirichlet-test.md`

    nodeid: bookofproofs$8367
    orderid: 200
    parentid: bookofproofs$8360

Because both these files refer to the same `parentid: bookofproofs$8360`, they will be automatically 
listed in the [published][example] (compiled) "Table of Contents" of the page `convergence-criteria-for-infinite-series-involving-products.md`.

[example]:https://bookofproofs.github.io/branches/analysis/convergence-criteria-for-infinite-series-involving-products.html

Because `orderid: 200` in `dirichlet-test.md` is greater than `orderid: 100` in `abel-test.md`, the latter 
will be listed prior in the compiled "Table of Contents".

### "Common Thread" and Navigation

All "Tables of Contents" determines a "common thread", in which visitors of 
<strong><span style='color:orange'>Bo</span><span style='color:lightblue'>P</span></strong> 
will navigate through your pages. It builds a tree with (currently) only three (3) root nodes: 
* Branches: `nodeid: bookofproofs$0`, 
* History: `nodeid: bookofproofs$2`, and
* Index: `nodeid: bookofproofs$i`.

There is a global "Table of Contents" visualizing the structure of these root nodes in the [tree-index published here][ti]. 

[ti]:https://bookofproofs.github.io/index/tree-index.html

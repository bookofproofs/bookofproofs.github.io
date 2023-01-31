# Naming, Identifying and Ordering Pages

## Naming

When you create a new markdown file in the `_sources` folder, you have to give it a unique name. 
Because the same name will be used for publishing in of the corresponding ` file and to make the name
search-engine-friendly, only lower-case characters and hyphens are allowed.

If this convention is not met, the following error will occur:

    BopValidationError.BopValidationError: NAMING 01:
    Illegal characters found in filename ../_sources/branches/analysis/de-moivres-identity,-complex-powers-proof.md

Together with the categories defined in the front matter of the file, the file name will be used for the 
permalink of the published `html` page (see [cheat_sheet_categories][csc] for more info).

[csc]:https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_compile/help/cheat_sheet_categories.md

Because of its later permalink, all source file have to be uniquely named. Even if try to put the same source file
into different subfolders in `_sources`, you will get the following error (example):

    BopValidationError.BopValidationError: NAMING 02:
    Duplicate filename in
    ../_sources/branches/geometry/differential-geometry.md and
    ../_sources/branches/geometry/differential-geometry/differential-geometry.md

## Identifying, Relating, Ordering

In addition to the later permalink, you can influence the order in which users can navigate from one page to another or
at which they will find the page in the table of contents of its parent page. 

This is accomplished by these three properties in the front matter

    nodeid: <github-usernam>$<alphanumeric-id>
    parentid: <github-usernam>$<alphanumeric-id>
    orderid: <whole-number>

The `nodeid` consists of the Github usernames of the first contributor to the page (its creator), followed by a 
dollar sign `$`, followed by an alphanumeric identifier of the page. The prefixing Github username in the `nodeid`
ensures that every contributor has her _namespace_ of page identifiers `nodeid`.

The `parentid` is a reference to an existing `nodeid` of another page. This can be both, a page created by yourself 
(i.e. prefixed with your Github username), and a page created by some other Github contributor.

The `orderid` is simply a whole number (usually in 100 steps like 100, 200, 300, etc.)

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
will be listed prior to the first in the compiled "Table of Contents".

### "Common Thread" - the Structure of Layouts 

All "Tables of Contents" like this create a "common thread" you can place your pages so that visitors of 
<strong><span style='color:orange'>Bo</span><span style='color:lightblue'>P</span></strong> 
can navigate through all pages like they would in a book, turning its pages. 

Technically speaking, the "common thread" (predecessor-successor) order of the pages is the same as the 
nodes of each tree, as they would be visited by a computer visiting them in a pre-order.

Currently, there are only three root nodes (i.e., with `layout: root`): 
* Branches: `nodeid: bookofproofs$0`, 
* History: `nodeid: bookofproofs$2`, and
* Index: `nodeid: bookofproofs$i`.

There is a global "Table of Contents" visualized in the [tree-index published here][ti]. 

[ti]:https://bookofproofs.github.io/index/tree-index.html

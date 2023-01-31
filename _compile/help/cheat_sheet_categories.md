# Categories

## Usage

Use the (mandatory) property 

    categories: 

in the front matter to influence the url of the resulting page. For instance, if your markdown file's name is `example.md` and 
its categories are comma-separated like 

    categories: branches,algebra,group-theory

the resulting **target file** will become  

    https://bookofproofs.github.io/branches/algebra/group-theory/example.html

It is important to know that the location of the **source file** `example.md` in the repository can be anywhere (!) inside 
the folder `_sources` or one of its subfolders. 
This location does not (!) influence the location of the target file, only the categories do. Nevertheless, the 
folder structure below `_sources` may be useful to sort all source files by subject.   

## Exceptions 

The compiler validates the categories of all markdown files and can produce the runtime errors with the
codes `CATEGORY 01` to `CATEGORY 04`, requiring your attention.

The front matter has to contain a category specification of the page. If not, the following error will occur (example):

    BopValidationError.BopValidationError: CATEGORY 01:
    Missing categories in ../_sources/branches/algebra/group-order.md

<hr>

When nesting pages using the parentid-nodeid relationship, the parent and the node need to have the same categories.
If this is not the case, the following error can occur (example).  

    BopValidationError.BopValidationError: CATEGORY 02:
    Categories '['branches', 'algebra']' of ../_sources/branches/algebra/algebraic-structure-algebra.md
    do not correspond to the categories ['branches', 'algebra', 'structures-overview']
    of its parent ../_sources/branches/algebra/structures-overview/structures-overview.md.

Just make the categories of both files identical to resolve this error.

<hr>

Categories must be lower-case, be alphanumeric and may contain the hyphen "-".


    BopValidationError.BopValidationError: CATEGORY 03:
    Malformed category 'group_theory' found in ../_sources/branches/algebra/algebraic-structure-algebra.md (must match '[a-z0-0\-]+')


<hr>

Every category needs an individual markdown file. 
In the example below, the category `structures-overview.md` was missing, before the category
`structures-overview` could be added to the file `magma-axioms.md`.


    BopValidationError.BopValidationError: CATEGORY 04:
    No markdown file found for the category 'structures-overview' found in ../_sources/branches/algebra/structures-overview/magma-axioms.md
    To start using this category, you must first add a new source file structures-overview.md to _sources.
    Also, give it the same categories as in ../_sources/branches/algebra/structures-overview/magma-axioms.md

<hr>

If the individual markdown file for the category has categories whose last one differs from its name,
the following error will occur:

    The file '../_sources/branches/algebra/algebra.md' is used as a category but has the categories 'branches'
    Make sure the file name 'algebra' is the last category in the front matter.

To resolve this error, just add the name of the file to its category list. 
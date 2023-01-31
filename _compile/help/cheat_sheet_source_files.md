# Markdown File Structure

All source files for the webpage hosted at https://bookofproofs.github.io/ can be found in the `_sources` folder 
and its subfolders.

These markdown files in `_sources` have all the same structure. They usually consist of three (3) sections
separated by `---`. A typical file looks like this:

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

## Properties in Front Matter - Overview

The first section is the so-called **front matter**. It contains a list of properties influencing the way your page 
will look like.  

The following table provides an overview of the available front matter properties.

Property | Meaning | Possible values | Example 
:-----|:------ |:------ |:------ 
`layout`|Determines the type of a single <strong><span style='color:orange'>Bo</span><span style='color:lightblue'>P</span></strong> site|see [cheat_sheet_layouts][csl]|`layout: theorem`
`categories`|Subject-related structure of the website|see [cheat_sheet_categories][csc]|`categories: branches, algebra, galois-theory`
`contributors`|Attribution to contributors of the site|see [cheat_sheet_attributing][csa]|`contributors: bookofproofs, @fitzpatrick`|
`description`|Content if the `description` attribute of the HTML `meta` tag of the site|| 
`keywords`|Comma-separated list of keywords for the become the `keywords` attribute of the HTML `meta` tag of the site||
`title`|Title of the site||
`nodeid`|A unique, filename-independent ID of the site|see [cheat_sheet_naming_identifying_ordering][csnio]|`nodeid: bookofproofs$392`|  
`url`|Link to a license (relevant only for the layout: `layout: license`) 
`parentid`|Reference to a parent `nodeid`|see [cheat_sheet_naming_identifying_ordering][csnio]|`parentid: bookofproofs$0`
`orderid`|Relative order between the children nodes of the same `parentid`|see [cheat_sheet_naming_identifying_ordering][csnio]|`orderid: 420`
`references`|References (bibliography) of the site|comma-separated list of `nodeid`|`references: bookofproofs$626,bookofproofs$628, bookofproofs$6419`
`issues`|Issues related to the site (kind of to-do list)|comma-separated list|`issues: broken-links`


[csl]:https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_compile/help/cheat_sheet_layouts.md
[csa]:https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_compile/help/cheat_sheet_attributing.md
[csc]:https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_compile/help/cheat_sheet_categories.md
[csnio]:https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_compile/help/cheat_sheet_naming_identifying_ordering.md
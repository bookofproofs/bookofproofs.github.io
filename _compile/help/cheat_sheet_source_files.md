# Markdown file structure

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

## Properties in Front Matter

The first section is the so-called **front matter**. Here you put a list of properties of your template. 
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

# Contributing to Persons

The `person` layout helps you to create brief fact sheets about 
living or passed persons with some significance for mathematics, physics, or computer science.

These following properties in the _front matter_ have special meaning and conventions to be met it this layout

* `title: <lastname>, <firstnames>` Lastname, followed by a comma-separated list of first names ( **mandatory**)
  * If there is no comma in the  `title` property, then the whole title will be treated as a last name.<br>
    This makes sense for some ancient names like `title: Euclid of Alexandria`.
  * If there are multiple commas in the `title` property, only the first name will be treated as the `<lastname>` variable.
    * `<lastname>` must be unique throughout all markdown files with this layout. 
      * To resolve persons with the last name, please meet the following convention: 
        1. Identify the person born later than the previous one. 
        2. Amend the lastname of the later person by adding `<lastname> (<running-number>)`.
           1. Rename accordingly any other persons born even later using a higher `<running-number>`.<br><br>
           Example: 
```
title: Bernoulli, Jacob
born: 1655
died: 1705
```

```
title: Bernoulli (2), Johann
born: 1667
died: 1748
```

* `born: <integer>` Year of birth (according to the western calendar, if negative then BC, **mandatory**).
* `died: <integer>` Year of death (according to the western calendar, if negative then BC, _optional_).
* tag
* `tags: <tag1,tag2,...>` Comma-separated list of tags (**mandatory**)
  * Use the `tags` property to attach additional information to persons.
  * This information can be used by the visitors of <strong><span style='color:orange'>BookOf</span><span style='color:lightblue'>Proofs</span></strong> (<strong><span style='color:orange'>Bo</span><span style='color:lightblue'>P</span></strong>) to search for specific persons by their tag.
  * Unlike the `categories` property, `tags` do not influence the __permalink__ under which person's site is published.
  * The tags have to be alphanumeric (including hyphens).
 

The above rules are subject to automatic validation during the compilation process. For instance, 

    BopValidationError.BopValidationError: PERSON 02:
    Duplicate lastname 'Ceva' found twice in
    ../_sources/history/17th-century/ceva-giovanni.md and 
    ../_sources/history/17th-century/ceva-tommaso.md
    Consider renaming 'Ceva' to 'Ceva (2)'.

indicates that there are two markdowns with two persons with the same lastname in the title. 
You have to fix such validation errors before committing your contribution and making a pull-request.

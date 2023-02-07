# Contributing to Epochs

Epochs are pages with the `epoch` layout. Their purpose is to provide a chronological view on the 
development of mathematics, physics, and computer science. 

    layout: epoch

It is usually not necessary to _create_ any new markdown files with this layout, since 
<strong><span style='color:orange'>BookOf</span><span style='color:lightblue'>Proofs</span></strong>
already covers the epochs from Prehistory to the 21st century. However, you can _improve_ the existing epochs.

## Structure of epochs

Each epoch markdown file is divided into two sections: 

1. The **Description** of the epoch contains a brief background information about the main historical developments that took place (world-wild) in the history during this epoch. 
These developments do not necessarily have to be related to mathematics, physics, and computer science.
2. The **Chronology** section contains a chronological list of events, usually sorted ascending by the year according to the western calendar 
<br><br>Note: By convention, we have to stick to only one calendar, but any other calendar system would do the trick.

## Editing Years

When you are missing a year, add it _chronologically_ and as a _heading 3 markdown_ (!) with respect to the existing years.
For instance, if in the epoch of the 17th century there were the years 1633 and 1635 already listed, but 1634 was missing,
you should add the following line:  

    ### 1636
    ... 
    
    ### 1637      <---- This is your new line
    
    ### 1638
    ...

Next, add an enumeration of events that took place in that year
(but, of course, only those you think are of relevance to mathematics, physics, or computer science).
By convention, you should always use markdown _bullet enumeration_ (!). For instance: 

```
### 1637
* [Descartes][bookofproofs$Descartes] publishes "La Géometrie".
   * Continuing the work of [François Viète][bookofproofs$Viete], Descartes solves geometrical problems using algebraic means. 
   * In this epochal work, he also abolishes the dogma that lasted in mathematics for millennia, prohibiting mathematicians from calculating with lengths and volumes at once
     (which, they thought, was impossible because of the danger to mix up incompatible geometrical concepts).
* ...
* ...
* <yet another event>
```
It is important to use the markdown of _bullet enumeration_ to keep the convention in all 
chronology sections of <strong><span style='color:orange'>BookOf</span><span style='color:lightblue'>Proofs</span></strong> 
and to keep the event description short and concise. 

## Topics related to the epoch.

If you need more text to describe the event, feel free to create a
separate page dedicated to this event, in which you use the `topic` layout instead (see [cheat_sheet_layout_topic](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_compile/help/cheat_sheet_layout_topic.md)). 
Also, make sure that the epoch's `nodeid` corresponds to the `parentid` of the topic. This will make the topic be listed
in the able of Contents of the epoch. 

## Famous Personalities

The markdown file of each `epoch` is has the `nodeid` corresponding to the `parentid` of persons who were born
in the epoch. They are automatically listed in the Table of Contents of the epoch. 

For using the `person` layout, see [cheat_sheet_layout_person](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_compile/help/cheat_sheet_layout_person.md). 
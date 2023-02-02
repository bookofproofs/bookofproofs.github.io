# Referencing to Bibliography

Unless you are simply correcting typos or improving the language used in some pages, _you should always_ make bibliographic 
references to your new content.

There is a standard way to add bibliography to pages in <strong><span style='color:orange'>Bo</span><span style='color:lightblue'>P</span></strong>:

    references: bookofproofs$6909, bookofproofs$8285

The property `references` accepts a comma-separated list of identifiers. These identifiers refer to lines in the hidden markdown file 
locate at [_sources/_references/references.md](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_references/references.md).

If your bibliography is not listed here, just add new lines to `_sources/_references/references.md`, giving it your identifiers.

## Example

Imagine, you write a mathematical text and want to refer to one of your books titled "Complex Analysis", by Serge Lang, published in 1999 in its Forth Edition.

1. Go to [_sources/_references/references.md](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_references/references.md)
2. Add three colums to the table of references. Your line will probably look like this:<br><br>
`bookofproofs$6925 | <your-github-userid>$<some-identifier> | **Lang, Serge**: "Complex Analysis", Springer, 1999, Forth Edition`
<br><br> to the existing table. 
3. Add the same identifier as in your second column in your markdown:<br>  
`references: <your-github-userid>$<some-identifier>`<br>

In most cases, you should use `bookofproofs$6925` in the first column. This is the so-called _license identifier_ and influences the references section 
in which your reference will appear in on the page with your published content.

The licence `bookofproofs$6925` corresponds to the reference section "Bibliography". You can find this and other reference sections, in which your reference can appear 
in the folder [_sources/_licenses](https://github.com/bookofproofs/bookofproofs.github.io/tree/main/_sources/_licenses). 




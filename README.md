# bookofproofs.github.io

This repository was created to enable collaborating on the <strong><span style='color:orange'>BookOf</span><span style='color:lightblue'>Proofs</span></strong> (<strong><span style='color:orange'>Bo</span><span style='color:lightblue'>P</span></strong>) site.
Originally hosted at https://www.bookofproofs.org, it is currently migrating to https://bookofproofs.github.io/. 

<strong><span style='color:orange'>Bo</span><span style='color:lightblue'>P</span></strong> derives the results of mathematics, physics, and computer sciences using the axiomatic method. If you are passionate about mathematics, theoretical physics, or (theoretical) computer science, we warmly welcome you to contribute to this site. 

The site is public, non-profit, and dedicated to sharing known mathematical theories with interested internet users.

# How is this repository structured?

The public website https://bookofproofs.github.io/ is deployed using [Github Pages][gp] from this repository's `doc` subfolder.
All other folders are auxiliary:
* In the `_sources` folder, you will find the sources of the webpages in a markdown format.  
* In the `_compile` folder, you will find Python scripts needed to compile the markdown format to HTML and write it into the `doc` subfolder. Before submitting a pull request, you will need these scripts to test your contributions locally.

# How can I collaborate?

Note: As long as we are still migrating from the old site, you can contribute to the already migrated branches of mathematics.
Check the subfolders of `_sources/branches` and `_sources/history` to see, which branches of mathematics are already migrated. 

We will remove this note after the migration is complete.  

Please check out our [CONTRIBUTING.md][cmd] for more detailed information.

[cmd]:./CONTRIBUTING.md
[gp]:https://docs.github.com/en/pages

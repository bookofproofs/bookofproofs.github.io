layout: algorithm
categories: branches,theoretical-computer-science, basic-algorithms
nodeid: bookofproofs$625
orderid: 50
parentid: bookofproofs$155
title: Sequential Search
description: SEQUENTIAL SEARCH &#9733; bring your math skills to the graduate level &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: 
keywords: search,sequential
contributors: bookofproofs

---
Let `\(n=|keys|\)`. The sequential search (using a dictionary data structure) requires:

> `\(n+1=\mathcal O(n)\)` (worst case) and

> `\(\frac{n+1}2=\mathcal  O(n)\)` (average case)

comparison operations.

---

def seqSearch(searchitem, dictionary):
    found = False # help variable found
    for k, v in dictionary.items():
        if v == searchitem:
            found = True
            break

    if found:
        return k
    else:
        return False


# Usage
dictionary = {1: "Zara", 2: "Tess", 3: "Bott", 4: "Dial"}
print(seqSearch("Bott", dictionary))
1. will output
1. will output

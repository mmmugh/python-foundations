## Practice: a lost property register

The station's lost property office keeps a register: what is being held, and
how many of each. It is a dictionary, item name to count.

```python
{"umbrella": 3, "phone": 1, "scarf": 2}
```

Things arrive and things get claimed, so the register changes all day. You are
going to write the functions behind the counter.

Everything here uses Chapters 1 to 9: dictionaries, `get()`, `values()`,
`items()`, `del`, sets, and `&` and `|`.

As in Chapter 7, none of these functions should change the register they are
handed — they return a new one. An office where looking something up can
quietly alter the records is not an office anyone can trust.

An item held zero times is not held. When the last one is claimed, its entry
comes out of the register rather than sitting there as a zero.

### Steps

1. Write `count_of(register, item)` returning how many are held, and `0` for something that was never handed in. `get()` does this in one line without raising.
2. Write `total_items(register)` returning how many objects are in the office altogether — 6 for the register above, not 3.
3. Write `add_item(register, item)` returning a new register with one more of that item, whether or not it was already there.
4. Write `remove_item(register, item)` returning a new register with one fewer. When the last one goes, drop the entry entirely with `del`. Claiming something that is not held changes nothing.
5. Write `sorted_items(register)` returning the item names in alphabetical order. Looping over a dictionary gives you its keys.
6. Write `busiest(register)` returning the name of the item there are most of. Assume no ties.
7. Write `in_both(left, right)`, given two lists of item names, returning a sorted list of the names in both. Turn them into sets and use `&`.
8. Write `register_from(found)`, given a list of item names as they were handed in, returning the register that counts them.

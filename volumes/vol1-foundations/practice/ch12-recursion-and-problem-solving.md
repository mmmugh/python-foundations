## Practice: adding up a folder tree

"How big is this folder?" is a question with no bottom to it. A folder holds
files, and it holds folders, and those hold folders. You cannot write a loop
that goes deep enough, because you do not know how deep it goes — which is
exactly the shape recursion is for.

A folder is a dictionary:

```python
{"name": "docs", "files": [100, 250], "folders": []}
```

A name, the sizes of the files directly inside it, and the folders directly
inside it, each one the same shape again. A folder with nothing in it has two
empty lists, and that is the base case for nearly everything here.

The tree to test with:

```
root            files 10, 20
  docs          files 100
  images        files 300, 40
    raw         files 1000
```

Everything here uses Chapters 1 to 12. Each function needs to answer for the
folder it is given by asking the same question of the folders inside it.

### Steps

1. Write `total_size(folder)` returning every byte at or below it — 1470 for `root`, and 0 for an empty folder. Add up its own files, then add what each folder inside reports.
2. Write `file_count(folder)` returning how many files there are altogether, all the way down. Six for `root`.
3. Write `depth(folder)` returning how many levels deep the tree goes. A folder with no folders inside is depth 1, so `root` is 3.
4. Write `folder_names(folder)` returning every folder name, the folder itself first, then each subtree in order: `root`, `docs`, `images`, `raw`.
5. Write `largest_file(folder)` returning the size of the biggest file anywhere below, or `None` when there are no files at all. The biggest one is three levels down, so this cannot only look at its own files.
6. Write `find_folder(folder, name)` returning the folder dictionary with that name, searching the whole tree, or `None` if there is no such folder.
7. Write `all_sizes(folder)` returning a flat list of every file size, in the same order as step 4 visits the folders.
8. Write `size_report(folder)` returning one line per folder, reading `docs: 100`, with each folder's own total from step 1, in the same order again.

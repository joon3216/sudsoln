
# `sudsoln`

## Coming up: `sudsoln` ver 0.0.5

* Add `Appearance` object, a concept used in `.solve_by_pairs()` method of `Sudoku` object.
* Eliminate `numpy` dependencies by adding `Array` object
* Fix typo in `to_sudoku()`: it is `(str, {objects}, int)`, not `(str, int, {objects})`.
* Make `Sudoku.elements` type-independent; i.e. it can accept not only a set of strings, but also a set of integers
* Write more solving features
* Write unittests of `Sudoku` object for simpler maintenance and automatic testing
	+ Test `.__init__()` with more examples in unittest
	+ Test `.solve_logically()` with more sudoku questions in unittest

## `sudsoln` ver 0.0.4

* Added unittests: `tests_candidate.py`
* Updated `.__repr__()` in `Candidate` object.
* Updated `Sudoku` object so that it now accepts a list of lists.

## `sudsoln` ver 0.0.3

* Added: `from .candidates import *` in `sudoku.py`


## `sudsoln` ver 0.0.2

* Edited: dependency in `setup.py`


## `sudsoln` ver 0.0.1

* Created a package.
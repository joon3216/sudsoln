
# `sudsoln`

## Coming up: ver 0.0.9

* Add `Appearance` object, a concept used in `.solve_by_pairs()` method of `Sudoku` object. This is basically an "inverse" of Candidate: for every element in elements, it gives you the number of appearances in each key of Candidate. 
* Eliminate `numpy` dependencies by adding `Array` object
* Write more solving features
* Write unittests on `Sudoku` object for simpler maintenance and automatic testing
	+ Test `.__init__()` with more examples in unittest
* Write unittests on `Appearance` object after it is defined.


## ver 0.0.8

* Deleted `from sudsoln.candidate import *` in `__init__.py`; unnecessary. 
* Deleted `solvers.py` in `sudsoln/tmp` directory; redundant.
* Made `Sudoku.elements` type-independent, i.e. i.e. it now accepts not only a set of strings, but also a set of integers, as well as a mixture of both
* Wrote a test on `.solve_logically()` with questions in `questions.py`


## ver 0.0.7

* Edited `tests.py`: instead of using `import sudsoln.candidate as candidate`, it is now `import candidate`


## ver 0.0.6

* Packaging failed; edited `__init__.py` in `sudsoln` directory.


## ver 0.0.5

* `__version__` variable directly defined in `__init__.py`, and `version.py` deleted.
* Added one unit test on Sudoku class
* Edited: from `from .candidate import *` to `import candidate` in `sudoku.py`
* Fixed typo in `to_sudoku()`: `(str, int, {objects})` => `(str, {objects}, str)`, and default has been defined for `elements` argument
* Moved `.py` scripts that are not currently a part of package: `array.py`, `questions.py`, `solvers.py`, `tests_candidate.py`, and `tests_sudoku.py`. These are currently located in `tmp` directory.
* Unified all tests into `tests.py`



## ver 0.0.4

* Added unittests: `tests_candidate.py`
* Updated `.__repr__()` in `Candidate` object.
* Updated `Sudoku` object so that it now accepts a list of lists.

## ver 0.0.3

* Added: `from .candidates import *` in `sudoku.py`


## ver 0.0.2

* Edited: dependency in `setup.py`


## ver 0.0.1

* Created a package.

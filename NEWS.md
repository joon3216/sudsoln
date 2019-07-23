
# `sudsoln`

## Coming up: ver >= 0.0.12

* Add `Appearance` object, a concept used in `.solve_by_pairs()` method of `Sudoku` object. This is basically an "inverse" of `Candidate`: for every element in `elements`, it gives you the number of appearances in each key of `Candidate`. 
* Create `sudsoln/data` directory to store sudoku questions
* Eliminate `numpy` dependencies by adding `Array` object
* Make `Sudoku` accept strings as well... but should I?
* Write more solving features
* Write unittests on:
	+ `Appearance` object after it is defined.
	+ `Array` object after it is defined.

## Working on: ver 0.0.11 (changes made after the current version)

* Added `Array` object, an array that is ALWAYS 2-dimensional.
* Added two tests in `tests.py`: `test_init_detect_typo_elements_none()` and `test_init_detect_typo_elements_specific()`.
* Changed the name of `array.py` to `sarray.py`
* Edited `test_init_detect_answer()` to test two features: answer-form detection and empty-specification irrelevance.

## ver 0.0.10 (current version)

* Added `change_empty(array, old, new)` in `sudoku.py`.
* Erased `from sudsoln.candidate import *` and `from sudsoln.questions import *` in `__init__.py` because I think they should be accessed as submodules.
* Made `Sudoku` to guess `self.elements` whenever it is not specified (i.e. `None`); you don't need to specify it every time you initialize `Sudoku` puzzle unless error messages specifically ask you to do so.
	+ Updated `tests.py` accordingly: added `test_init_detect_answer()`, `test_init_elements_error()`, and `test_init_empty_error()`.
* Wrote `import doctest; doctest.testmod()` in `candidate.py`


## ver 0.0.9

* Added `formatting.py` for a formatting of `questions.py`
* Added `test_solve_forcefully()` in `tests.py`
* Added `seed` and `quietly` arguments to `.solve()` and `.solve_forcefully()`
* Changed the numberings of `a_sta410_*` in `questions.py`, and added `q_sta410_testing` for unittest
* Removed `numpy.random` dependency from `.solve_forcefully()`
* Removed `sudsoln/tmp` directory and moved all the `.py` scripts out of it. `appearance.py` and `array.py` is now in `sudsoln` directory
* Rewrote `__init__.py`:
	+ Added: `from sudsoln.candidate import *`; realized having this is more convenient
	+ Added: `from sudsoln.questions import *`; the same reason
* Wrote `import doctest; doctest.testmod()` in `sudoku.py`


## ver 0.0.8

* Added `python_requres=">=3"` in `setup.py`
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

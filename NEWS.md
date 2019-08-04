
# `sudsoln`

## Coming up: ver >= 0.0.20

* Create `sudsoln/data` directory to store sudoku questions
* Eliminate duplicate codes in `.solve_by_*_pairs()`
* Write more solving features:
	+ Currently working on `.solve_by_hidden_pairs()` and its `by` argument
	+ Next: work on `.solve_by_pointing_pairs()` to handle `by` argument properly.
* Write unittests on `Appearance`.

## ver 0.0.19 (working on)

* to be continued

## ver 0.0.18 (current version)

* `Candidate.refine()` now accepts either `condition = ['contains', 1]` or `condition = ['contains', 2]` only; `['both', 2]` has been completely deprecated from `Candidate.refine()` (but NOT from `Appearance.sieve()`) since `['contains', 2]` is a more versatile condition that also works with `by = row` and `by = col` in `.solve_by_hidden_pairs()`.
* Changed the name of method: `.solve_by_pairs()` -> `.solve_by_pointing_pairs()`
* Checked that `start` argument is working properly on both `.solve_by_hidden_pairs()` and `.solve_by_pointing_pairs()`.
* The behaviour of `Appearance.sieve()` when `deep = True` has changed; if `deep = True`, then the method will check all the second elements of the value lists of `Appearance` so that 1. they are all the same AND 2. all has length `condition[1]`. If not, then the respective keys that passed `condition` are furthur removed from `Appearance`. Docstring has been added to explain this behaviour.


## ver 0.0.17

* `.solve_by_hidden_pairs()` yields an 'answer' that cannot be transformed into the answer form; needs revision.
	+ `Candidate.refine()` body modified so that it works only if `len(replacing_candids) == 2 and len(ent_to_replace) == 2` 
* Packaging again to see if `.solve_by_hidden_pairs()` now works properly.


## ver 0.0.16

* Added `by` and `start` arguments to `.solve_by_pairs()` of `Sudoku`
* Added `condition` and `deep` arguments to `.sieve()` method of `Appearance`.
* Added `sieve`, `condition`, and `deep` arguments to `.refine` method of `Candidate`
* Added `.keys()` and `.values()` method to `Appearance`
* Cancelled a plan to make `Sudoku` accept strings; it seems unnecessary because `to_sudoku()` function already does the job of transforming sudoku strings into `Sudoku`. Moreover, simplifying the type of `array` argument in `Sudoku()` seems important.
* Edited `__repr__()` of `Candidate`; dictionary will be displayed as if it is passed to `pprint.pprint()`
* Packaging done to check `.solve_by_hidden_pairs()`


## ver 0.0.15

* Packaging still failing in Python <= 3.6; moved `Appearance` and `Union` under `Candidate` and retried
* Removed `import appearance` and `import union` in `tests.py` as these objects are now moved to `candidate.py`



## ver 0.0.14

* Packaging failed in Python ver <= 3.6; modified `__init__.py` and retried.

## ver 0.0.13

* Added `.appearances()` and `.unions()` methods to `Candidate` object.
* Added `Appearance` and `Union` object that is used in `.solve_by_pairs()` method of `Sudoku` puzzle. They're written in `appearance.py` and `union.py` respectively.
* Adjusted `Candidate` object to have `elements` argument; `n` argument is completely deprecated and is computed via `elements`. All affected objects --- `Appearance`, `Union`, and `Sudoku` --- are accustomed to adapt this change.
* Rewrote the entire docstring examples of `Candidate` and `Sudoku` to pass doctest.
* Rewrote the test cases in `tests.py` to adapt the change in `Candidate`.


## ver 0.0.12

* Commented out `install_requires=['numpy']` in `setup.py`

## ver 0.0.11

* Added `Array` object, an array that is ALWAYS 2-dimensional:
	+ supported attributes: `.show`, `.nrow`, `.ncol`, `.shape`, `.size`
	+ supported methods: `.__eq__()`, `.__getitem__()`, `.__setitem__()`, `.__repr__()`, `.copy()`, `.flatten()`, `.itemset()`, `.reshape()`
* Added two tests in `tests.py`: `test_init_detect_typo_elements_none()` and `test_init_detect_typo_elements_specific()`.
* Added `TestArray(unittest.TestCase)` in `tests.py`.
* Changed the name of `array.py` to `sarray.py`
* Edited `test_init_detect_answer()` to test two features: answer-form detection and empty-specification irrelevance.
* Made `sudoku.py` completely numpy-free

## ver 0.0.10

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

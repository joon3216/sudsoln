
<!-- README.md is generated from README.Rmd. Please edit that file -->

# `sudsoln`

<!-- badges: start -->

[![Build
Status](https://travis-ci.org/joon3216/sudsoln.svg?branch=master)](https://travis-ci.org/joon3216/sudsoln)
[![codecov](https://codecov.io/gh/joon3216/sudsoln/branch/master/graph/badge.svg)](https://codecov.io/gh/joon3216/sudsoln)
<!-- badges: end -->

A `n ** 2`-by-`n ** 2` sudoku solver.

## Installation

To install, type:

``` bash
pip install sudsoln
```

To update, type:

``` bash
pip install sudsoln --upgrade
```

## A very brief introduction to `sudsoln`

``` python
import sudsoln as ss
eg = '6.5..7..1.1..2..5......6..33.2.......4.....8.......9.52..9......6..1..2.5..3..7.6'
eg = ss.to_sudoku(eg)
eg
#> Sudoku(
#>     6    .    5    |    .    .    7    |    .    .    1
#>     .    1    .    |    .    2    .    |    .    5    .
#>     .    .    .    |    .    .    6    |    .    .    3
#> -------------------+-------------------+-------------------
#>     3    .    2    |    .    .    .    |    .    .    .
#>     .    4    .    |    .    .    .    |    .    8    .
#>     .    .    .    |    .    .    .    |    9    .    5
#> -------------------+-------------------+-------------------
#>     2    .    .    |    9    .    .    |    .    .    .
#>     .    6    .    |    .    1    .    |    .    2    .
#>     5    .    .    |    3    .    .    |    7    .    6
#> n: 3
#> elements: 1, 2, 3, 4, 5, 6, 7, 8, 9
#> empty: .
#> )
eg.solve()
#> ('0:00:00.086731', 0)
eg
#> Sudoku(
#>     6    3    5    |    8    9    7    |    2    4    1
#>     8    1    9    |    4    2    3    |    6    5    7
#>     7    2    4    |    1    5    6    |    8    9    3
#> -------------------+-------------------+-------------------
#>     3    5    2    |    6    8    9    |    1    7    4
#>     9    4    6    |    5    7    1    |    3    8    2
#>     1    8    7    |    2    3    4    |    9    6    5
#> -------------------+-------------------+-------------------
#>     2    7    1    |    9    6    5    |    4    3    8
#>     4    6    3    |    7    1    8    |    5    2    9
#>     5    9    8    |    3    4    2    |    7    1    6
#> n: 3
#> elements: 1, 2, 3, 4, 5, 6, 7, 8, 9
#> empty: .
#> )
eg.is_valid_answer()
#> True
```

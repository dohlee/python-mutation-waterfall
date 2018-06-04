========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |requires|
        | |codecov|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|

.. |docs| image:: https://readthedocs.org/projects/python-mutation-waterfall/badge/?style=flat
    :target: https://readthedocs.org/projects/python-mutation-waterfall
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/dohlee/python-mutation-waterfall.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/dohlee/python-mutation-waterfall

.. |requires| image:: https://requires.io/github/dohlee/python-mutation-waterfall/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/dohlee/python-mutation-waterfall/requirements/?branch=master

.. |codecov| image:: https://codecov.io/github/dohlee/python-mutation-waterfall/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/dohlee/python-mutation-waterfall

.. |version| image:: https://img.shields.io/pypi/v/mutation-waterfall.svg
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/mutation-waterfall

.. |commits-since| image:: https://img.shields.io/github/commits-since/dohlee/python-mutation-waterfall/v0.1.1.svg
    :alt: Commits since latest release
    :target: https://github.com/dohlee/python-mutation-waterfall/compare/v0.1.1...master

.. |wheel| image:: https://img.shields.io/pypi/wheel/mutation-waterfall.svg
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/mutation-waterfall

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/mutation-waterfall.svg
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/mutation-waterfall

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/mutation-waterfall.svg
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/mutation-waterfall


.. end-badges

Python library for visualizing mutation landscape as waterfall diagram.

* Free software: MIT license

Installation
============

::

    pip install mutation-waterfall

Documentation
=============

https://python-mutation-waterfall.readthedocs.io/

Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox

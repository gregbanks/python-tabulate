===============
python-tabulate
===============

Pretty-print tabular data in Python.

The main use cases of the library are:

* printing small tables without hassle: just one function call,
  formatting is guided by the data itself

* authoring tabular data for lightweight plain-text markup: multiple
  output formats suitable for further editing or transformation

* readable presentation of mixed textual and numeric data: smart
  column alignment, configurable number formatting, alignment by a
  decimal point


Installation
------------

::

    pip install tabulate


Build status
------------

.. image:: https://drone.io/bitbucket.org/astanin/python-tabulate/status.png
   :alt: Build status
   :target: https://drone.io/bitbucket.org/astanin/python-tabulate/latest


Usage
-----

The module provides just one function, ``tabulate``, which takes a
list of lists or another tabular data type as the first argument,
and outputs a nicely formatted plain-text table::

    >>> from tabulate import tabulate

    >>> table = [["Sun",696000,1989100000],["Earth",6371,5973.6],
    ...          ["Moon",1737,73.5],["Mars",3390,641.85]]
    >>> print tabulate(table)
    -----  ------  -------------
    Sun    696000     1.9891e+09
    Earth    6371  5973.6
    Moon     1737    73.5
    Mars     3390   641.85
    -----  ------  -------------

The following tabular data types are supported:

* list of lists or another iterable of iterables
* list or another iterable of dicts (keys as columns)
* dict of iterables (keys as columns)
* two-dimensional NumPy array
* NumPy record arrays (names as columns)
* pandas.DataFrame

Examples in this file use Python2. Tabulate supports Python3 too.


Headers
~~~~~~~

The second optional argument named ``headers`` defines a list of
column headers to be used::

    >>> print tabulate(table, headers=["Planet","R (km)", "mass (x 10^29 kg)"])
    Planet      R (km)    mass (x 10^29 kg)
    --------  --------  -------------------
    Sun         696000           1.9891e+09
    Earth         6371        5973.6
    Moon          1737          73.5
    Mars          3390         641.85

If ``headers="firstrow"``, then the first row of data is used::

    >>> print tabulate([["Name","Age"],["Alice",24],["Bob",19]],
    ...                headers="firstrow")
    Name      Age
    ------  -----
    Alice      24
    Bob        19

When the data is a list of dict, ``headers="firstrow"`` can also be 
used to assign different column names to each corresponding dict key:

        >>> print tabulate([{"name": "Name", "age": "Age"}, 
                            {"name": "Alice", "age": 24},
                            {"name": "Bob", "age": 19}],
        ...                headers="firstrow")
    Name      Age
    ------  -----
    Alice      24
    Bob        19

Furthermore with a list of dict, you can also specify ``headers`` as 
a dict (similar to the example above), or as a list of keys. Either way,
the specified keys can be a subset of all the keys present across the 
dataset:

        >>> print tabulate([{"foo": 1, "bar": 2},
                            {"foo": 3, "bar": 4, "baz": 5}],
        ...                headers=["bar","foo"])
    bar    foo
    -----  -----
        2      1
        4      3


If ``headers="keys"``, then the keys of a dictionary/dataframe, or
column indices are used. It also works for NumPy record arrays and
lists of dictionaries or named tuples::

    >>> print tabulate({"Name": ["Alice", "Bob"],
    ...                 "Age": [24, 19]}, headers="keys")
      Age  Name
    -----  ------
       24  Alice
       19  Bob


Table format
~~~~~~~~~~~~

There is more than one way to format a table in plain text.
The third optional argument named ``tablefmt`` defines
how the table is formatted.

Supported table formats are:

- "plain"
- "simple"
- "grid"
- "pipe"
- "orgtbl"
- "rst"
- "mediawiki"
- "latex"

``plain`` tables do not use any pseudo-graphics to draw lines::

    >>> table = [["spam",42],["eggs",451],["bacon",0]]
    >>> headers = ["item", "qty"]
    >>> print tabulate(table, headers, tablefmt="plain")
    item      qty
    spam       42
    eggs      451
    bacon       0

``simple`` is the default format (the default may change in future
versions).  It corresponds to ``simple_tables`` in `Pandoc Markdown
extensions`_::

    >>> print tabulate(table, headers, tablefmt="simple")
    item      qty
    ------  -----
    spam       42
    eggs      451
    bacon       0

``grid`` is like tables formatted by Emacs' `table.el`_
package.  It corresponds to ``grid_tables`` in Pandoc Markdown
extensions::

    >>> print tabulate(table, headers, tablefmt="grid")
    +--------+-------+
    | item   |   qty |
    +========+=======+
    | spam   |    42 |
    +--------+-------+
    | eggs   |   451 |
    +--------+-------+
    | bacon  |     0 |
    +--------+-------+

``pipe`` follows the conventions of `PHP Markdown Extra`_ extension.  It
corresponds to ``pipe_tables`` in Pandoc. This format uses colons to
indicate column alignment::

    >>> print tabulate(table, headers, tablefmt="pipe")
    | item   |   qty |
    |:-------|------:|
    | spam   |    42 |
    | eggs   |   451 |
    | bacon  |     0 |

``orgtbl`` follows the conventions of Emacs `org-mode`_, and is editable
also in the minor `orgtbl-mode`. Hence its name::

    >>> print tabulate(table, headers, tablefmt="orgtbl")
    | item   |   qty |
    |--------+-------|
    | spam   |    42 |
    | eggs   |   451 |
    | bacon  |     0 |

``rst`` formats data like a simple table of the `reStructuredText`_ format::

    >>> print tabulate(table, headers, tablefmt="rst")
    ======  =====
    item      qty
    ======  =====
    spam       42
    eggs      451
    bacon       0
    ======  =====

``mediawiki`` format produces a table markup used in `Wikipedia`_ and on
other MediaWiki-based sites::

    >>> print tabulate(table, headers, tablefmt="mediawiki")
    {| class="wikitable" style="text-align: left;"
    |+ <!-- caption -->
    |-
    ! item   !! align="right"|   qty
    |-
    | spam   || align="right"|    42
    |-
    | eggs   || align="right"|   451
    |-
    | bacon  || align="right"|     0
    |}


``latex`` format creates a ``tabular`` environment for LaTeX markup::

    >>> print tabulate(table, headers, tablefmt="latex")
    \begin{tabular}{lr}
    \hline
     item   &   qty \\
    \hline
     spam   &    42 \\
     eggs   &   451 \\
     bacon  &     0 \\
    \hline
    \end{tabular}



.. _Pandoc Markdown extensions: http://johnmacfarlane.net/pandoc/README.html#tables
.. _PHP Markdown Extra: http://michelf.ca/projects/php-markdown/extra/#table
.. _table.el: http://table.sourceforge.net/
.. _org-mode: http://orgmode.org/manual/Tables.html
.. _reStructuredText: http://docutils.sourceforge.net/docs/user/rst/quickref.html#tables
.. _Wikipedia: http://www.mediawiki.org/wiki/Help:Tables


Column alignment
~~~~~~~~~~~~~~~~

``tabulate`` is smart about column alignment. It detects columns which
contain only numbers, and aligns them by a decimal point (or flushes
them to the right if they appear to be integers). Text columns are
flushed to the left.

You can override the default alignment with ``numalign`` and
``stralign`` named arguments. Possible column alignments are:
``right``, ``center``, ``left``, ``decimal`` (only for numbers), and
``None`` (to disable alignment).

Aligning by a decimal point works best when you need to compare
numbers at a glance::

    >>> print tabulate([[1.2345],[123.45],[12.345],[12345],[1234.5]])
    ----------
        1.2345
      123.45
       12.345
    12345
     1234.5
    ----------

Compare this with a more common right alignment::

    >>> print tabulate([[1.2345],[123.45],[12.345],[12345],[1234.5]], numalign="right")
    ------
    1.2345
    123.45
    12.345
     12345
    1234.5
    ------

For ``tabulate``, anything which can be parsed as a number is a
number. Even numbers represented as strings are aligned properly. This
feature comes in handy when reading a mixed table of text and numbers
from a file:

::

    >>> import csv ; from StringIO import StringIO
    >>> table = list(csv.reader(StringIO("spam, 42\neggs, 451\n")))
    >>> table
    [['spam', ' 42'], ['eggs', ' 451']]
    >>> print tabulate(table)
    ----  ----
    spam    42
    eggs   451
    ----  ----



Number formatting
~~~~~~~~~~~~~~~~~

``tabulate`` allows to define custom number formatting applied to all
columns of decimal numbers. Use ``floatfmt`` named argument::


    >>> print tabulate([["pi",3.141593],["e",2.718282]], floatfmt=".4f")
    --  ------
    pi  3.1416
    e   2.7183
    --  ------


Performance considerations
--------------------------

Such features as decimal point alignment and trying to parse everything
as a number imply that ``tabulate``:

* has to "guess" how to print a particular tabular data type
* needs to keep the entire table in-memory
* has to "transpose" the table twice
* does much more work than it may appear

It may not be suitable for serializing really big tables (but who's
going to do that, anyway?) or printing tables in performance sensitive
applications. ``tabulate`` is about two orders of magnitude slower
than simply joining lists of values with a tab, coma or other
separator.

In the same time ``tabulate`` is comparable to other table
pretty-printers. Given a 10x10 table (a list of lists) of mixed text
and numeric data, ``tabulate`` appears to be slower than
``asciitable``, and faster than ``PrettyTable`` and ``texttable``

::

    ===========================  ==========  ===========
    Table formatter                time, μs    rel. time
    ===========================  ==========  ===========
    join with tabs and newlines        22.6          1.0
    csv to StringIO                    31.6          1.4
    asciitable (0.8.0)                777.6         34.4
    tabulate (0.7.2)                 1374.9         60.9
    PrettyTable (0.7.2)              3640.3        161.2
    texttable (0.8.1)                3901.3        172.8
    ===========================  ==========  ===========


Version history
---------------

- 0.7.3: Iterables of dictionaries.
- 0.7.2: Python 3.2 Support.
- 0.7.1: Bug fixes. ``tsv`` format. Column alignment can be disabled.
- 0.7: ``latex`` tables. Printing lists of named tuples and NumPy
  record arrays. Fix printing date and time values. Python <= 2.6.4 is supported.
- 0.6: ``mediawiki`` tables, bug fixes.
- 0.5.1: Fix README.rst formatting. Optimize (performance similar to 0.4.4).
- 0.5: ANSI color sequences. Printing dicts of iterables and Pandas' dataframes.
- 0.4.4: Python 2.6 support.
- 0.4.3: Bug fix, None as a missing value.
- 0.4.2: Fix manifest file.
- 0.4.1: Update license and documentation.
- 0.4: Unicode support, Python3 support, ``rst`` tables.
- 0.3: Initial PyPI release. Table formats: ``simple``, ``plain``,
  ``grid``, ``pipe``, and ``orgtbl``.


Contributors
------------

Sergey Astanin, Pau Tallada Crespí, Erwin Marsi, Mik Kocikowski, Bill Ryder, Zach Dwiel.

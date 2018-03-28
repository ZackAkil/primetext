primetext
=========
python package for indexing text datasets for fast word frequency analysis

algorithm explanation
=========
https://www.codeproject.com/Tips/1137359/Text-Indexing-with-Prime-Factors

https://github.com/ZackAkil/text-indexing-using-prime-factors/blob/master/text%20indexing%20using%20prime%20factors.ipynb

Usage
=====

.. code-block:: python

  from primetext import primetext

  data = ["black cat on mat",
  "black hat for you",
  "cat sat on you"]

  # initiate primetext
  pt = primetext.primetext()

  # indexing data
  pt.index(data)

  # finding words 
  recordsWithCat = pt.find(['cat'])
  # returns boolean vector : [True,False,True]

  recordsWithCatAndSat = pt.find(['cat','sat'])
  # returns boolean vector : [False,False,True]

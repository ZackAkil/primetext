primetext
=========
python package for indexing text datasets for fast word frequency analysis

Usage
=====

.. code:: python
	:linenos:
	#from primetext import primetext

	data = ["black cat on mat",
	"black hat for you",
	"cat sat on you"]

	# initiate primetext
	pt = primetext()

	# indexing data
	pt.index(data)

	# finding words 
	recordsWithCat = pt.find(['cat'])
	# returns boolean vector : [True,False,True]

	recordsWithCatAndSat = pt.find(['cat','sat'])
	# returns boolean vector : [False,False,True]

import sys
import itertools as it
import numpy as np

 
class primetext:
    
    indexedDictionary = dict()
    indexedRecords = []
 
    cleanedRecords = []
    cleanedDictionary = []

    def primeInterator(self):
        D = { 9: 3, 25: 5 }
        yield 2
        yield 3
        yield 5
        MASK= 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0,
        MODULOS= frozenset( (1, 7, 11, 13, 17, 19, 23, 29) )

        for q in it.compress(
                it.islice(it.count(7), 0, None, 2),
                it.cycle(MASK)):
            p = D.pop(q, None)
            if p is None:
                D[q*q] = q
                yield q
            else:
                x = q + 2*p
                while x in D or (x%30) not in MODULOS:
                    x += 2*p
                D[x] = p

    def generatePrimeNumbers(self, count):
        output = []
        i = 0
        for prime in self.primeInterator():
            i += 1
            if i > count:
                break
            output.append(prime)
        return output

    def index(self, records):
        self.cleanedRecords = records
        self.assembleDictionary()
        self.indexDictionary()
        self.indexComments()

    def assembleDictionary(self):
        uniqueWords = []
        recordsChecked = 0
        for text in self.cleanedRecords:
            recordsChecked += 1
            sys.stdout.write("\rRecords checked : %i" % recordsChecked)
            for word in text.split(' '):
                if word not in uniqueWords:
                    uniqueWords.append(word)
        sys.stdout.write("\n")
        sys.stdout.flush()
        self.cleanedDictionary = uniqueWords  
        
    def indexDictionary(self):
        fitPrime = np.array(self.generatePrimeNumbers(len(self.cleanedDictionary)))
        self.indexedDictionary = dict(np.c_[self.cleanedDictionary,fitPrime])
        print('Indexed dictionary')

    def indexComments(self):
        output = []
        for comment in self.cleanedRecords:
            prod = 1
            words = comment.split(' ')
            for word in words:
                if word in self.indexedDictionary:
                    prod *= int(self.indexedDictionary[word])
            output.append(prod)
        self.indexedRecords = output
        print('Indexed comments')


    def convertWordsToProduct(self,words):
        output = 1
        for word in words:
            if word in self.indexedDictionary:
                output *= int(self.indexedDictionary[word])
        return output

    def searchByPrimeFact(self,searchProduct):
        return  (np.mod(self.indexedRecords, searchProduct) == 0)

    def find(self, words):
        prod = self.convertWordsToProduct(words)
        if prod == 1:
            return False
        return self.searchByPrimeFact(prod)
        
    def findInRecords(self, words):
        data = np.asarray(self.cleanedRecords)
        return data[self.find(words)]
        
    def countInRecords(self, words):
        return self.find(words).sum()
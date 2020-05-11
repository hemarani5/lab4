# -*- coding: utf-8 -*-
from string import punctuation, whitespace
text = 'pg45164.txt'
fin = open("pg45164.txt")
start = []
def projectbook():
     for line in fin:
         for item in line.split():
             start.append(item)
     return main
     fin.close()        

def nospace():
    withoutspace = ''
    for char in text:
        if ((char in punctuation) or (char in whitespace)):
            pass
        else:
            withoutspace += char.lower()
    return withoutspace        
print("the book has words")
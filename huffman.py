#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 13:43:35 2023

@author: umutmurat
"""
from operator import itemgetter
import sys
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Error -> No File")
        sys.exit(1)

    input_file = sys.argv[1]

with open(sys.argv[1], 'r') as file:
        a = file.readline()
        
        
class Node(object):
    def __init__(self ,left=None,right=None):
        self.left = left
        self.right = right
    
    def children(self):
        return (self.left, self.right)

    def nodes(self):
        return (self.left, self.right)

    def __str__(self):
        return '%s   %s' % (self.left, self.right)
        
        
def hufmannTree(node, left =True , binary = ''):
    if type(node) is str:
        return {node : binary}
    (l,r) = node.children()
    d = dict()
    d.update(hufmannTree(l,True,binary + '0'))
    d.update(hufmannTree(r,False,binary+'1'))
    return d;

frequency = {}
for c in a:
    if c in frequency:
        frequency[c] += 1
    else:
        frequency[c] = 1
        
frequency = sorted(frequency.items(), key = lambda x : x[1],reverse=True)

     
nodes = frequency

while len(nodes) > 1:
    (key1, c1) = nodes[-1]
    (key2, c2) = nodes[-2]
    nodes = nodes[:-2]
    node = Node(key1, key2)
    nodes.append((node, c1 + c2))
    nodes = sorted(nodes, key=lambda x: x[1], reverse=True)

hufmann = hufmannTree(nodes[0][0])


def encode(mapping,inputStr):
    encodedStr = ""
    for char in inputStr:
        encodedStr += mapping[char]
    return encodedStr
encoded = encode(hufmann, a)


def decode(mapping,inputStr):
    reverseMapping = {v: k for k, v in mapping.items()}
    decodedStr  =""
    code =""
    for bit in inputStr:
        code +=bit
        if code in reverseMapping:
            decodedStr += reverseMapping[code]
            code=""
    return decodedStr

decoded = decode(hufmann, encoded)


def CalcRatio(mapping,freq):
        B1=len(a)*8
        B0 = 0 
        size = len(freq)
        for i,j in freq:
            B0=B0+(len(i*j)*j)
        B0+=len(freq)
        return B1/B0
compRatio=CalcRatio(hufmann, frequency)
print("ENCODED : " + encoded +"\n" + "COMP RATIO : " + str(compRatio) +"\n"+ "DECODED : " +decoded)
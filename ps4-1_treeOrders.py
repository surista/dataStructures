#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S. Urista
Oct 2020
"""

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

*above code*

threading.Thread(target=main).start()
class Tree:
   def read(self):
       self.n = int(sys.stdin.readline())
       self.key = [0 for i in range(self.n)]
       self.left = [0 for i in range(self.n)]
       self.right = [0 for i in range(self.n)]
       for i in range(self.n):
          [a, b, c] = map(int, sys.stdin.readline().split())
          self.key[i] = a
          self.left[i] = b
          self.right[i] = c
          return self.n

    def isBinarySearchTree(self,index=0):
        leftIndex=self.left[index]
        rightIndex=self.right[index]
        key=self.key[index]
        if leftIndex==-1 and rightIndex==-1:
            return key,key,True

        if leftIndex!=-1:
            left=self.isBinarySearchTree(self.left[index])
            leftMin=left[0]
            leftMax=left[1]
            leftbool=left[2]

        if rightIndex!=-1:
            right=self.isBinarySearchTree(self.right[index])
            rightMin=right[0]
            rightMax=right[1]
            rightbool=right[2]

        if leftIndex==-1:
            return min(key,rightMin), rightMax, key<=rightMin and rightbool

        elif rightIndex==-1:
            return leftMin, max(key,leftMax), key>=leftMax and leftbool

        else:
            return min(key,leftMin), max(key,rightMax), key>leftMax and key<rightMin and leftbool and rightbool
def main():
    tree = Tree()
    n=tree.read()
    if n==0 or tree.isBinarySearchTree()[2]:
        print("CORRECT")
    else:
        print("INCORRECT")
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S. Urista
Oct 2020
Module documentation goes here
"""

# python3


def build_heap(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    swaps = []
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] > data[j]:
                swaps.append((i, j))
                data[i], data[j] = data[j], data[i]
    return swaps


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


# if __name__ == "__main__":
#     main()


lst = [40, 60, 10, 20, 50, 30]
for x, y in enumerate(lst):
    print(x, 'parent:',int((x-1)/2))
    print(x, 'left child:',int(x*2+1))
    print(x, 'right child:',int(x*2 + 2))


class minHeap:
    def getParent(self, i):
        return int((i-1)/2)

    def get_leftChild(self,i):
        return int(2*i)

    def get_rightChild(self,i):
        return int(2*i+1)
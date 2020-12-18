#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 12:54:59 2020

@author: jwoo
"""


#MergeSort

#The idea is to halve the original list, sort each half individually, then
#merge them.

#[12, 10, 2, 20, 1, 2, 50, 20]

#[12, 10, 2, 20]      [1, 2, 50, 20]

#[2, 10, 12, 20]      [1, 2, 20, 50]

#      [1, 2, 2, 10, 12, 20, 20, 50]

def merge(L1, L2):
    '''Return the sorted version of L1 + L2
    L1, L2 are sorted lists of ints
    '''
    #We are going to keep track of our position in both lists.
    #Then we append the smaller value.
    i1, i2 = 0, 0
    sorted = []
    
    while i1 < len(L1) and i2 < len(L2):
        if L1[i1] < L2[i2]:
            sorted.append(L1[i1])
            i1 += 1
        else:
            sorted.append(L2[i2])
            i2 += 1
    
    sorted.extend(L1[i1:])
    sorted.extend(L2[i2:])
    
    return sorted
#merge appends len(L1) + len(L2) elements to res
#so it runs in len(L1) + len(L2) iterations complexit:
#O(len(L1) + len(L2))
        

def merge_sort(L):
    
    if len(L) <= 1:
        return L[:]
    
    mid = len(L)//2
    sorted_half1 = merge_sort(L[:mid])
    sorted_half2 = merge_sort(L[mid:])
    return merge(sorted_half1, sorted_half2)

#TIME COMPLEXITY
#[1] [1] [1] [1] [1] [1] ...
#.......................
#    [n/4]                          [n/4]       #4 * k * n/4 = k*n seconds
#           [n/2]          [n/2]                #k*(n/2) + k*(n/2) = k*n seconds
#                   [n]                         #k*n seconds

#therefore, total runtime: (log2(n) + 1) * kn seconds
#complexity O(nlog(n))

#How many total calls do we have?
#1 + 2 + 4 + 8 + ... + n
#1 + 2 + 4 + 8 + ... + 2^(log2(n))
#geometric sum
#(2^(log2(n) + 1) - 1)/(2-1)
#2^log2(n) = n
#O(n) calls
#this is not quite so simple because merging doesn't take the same
#amount of time per call

def merge_sort_2(L):
    '''This time, we are using mid = 1
    So we append 1 element each time
    INSERTION SORT
    '''
    
    if len(L) <= 1:
        return L[:]
    
    #This time, we set mid to 1
    mid = 1
    sorted_half1 = merge_sort(L[:mid])
    sorted_half2 = merge_sort(L[mid:])
    return merge(sorted_half1, sorted_half2)

#                   [1]     k
#                  ...
#         [1]   [n-2]       
#   [1]     [n-1]           k*(n-1)
#       [n]                 k*n

#Total time k*(n + (n-1) + (n-2) + ... + 1)

#python sort and sorted algorithms use TimSort
#mergesort for large lists and insertion sort for small lists
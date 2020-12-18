#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 22:10:41 2020

@author: jwoo
"""
alphabet = "abcdef"
        
#print all strings of length n over alphabet alphabet
def print_all(alphabet, n, start_str = ""):
    '''Print all strings over alphabet alphabet of length n
    pre-pend the string start_str to every str'''
    if n == 0:
        print(start_str)
        return
    
    for letter in alphabet:
        #We do all combinations of each possible arrangement. Starting
        #with A. Since we do n-1 each time, we ensure that we eventually
        #reach the desired length.
        print_all(alphabet, n - 1, start_str + letter)
    
def all_combinations(alphabet, n, start_str = ""):
    '''Return a list of all strings over the alphabet alphabet, of length
    n, with start_str pre-pended
    '''
    if n == 0:
        return [start_str]
    
    combinations = []
    
    for letter in alphabet:
        '''This time, this loop returns a list of strings. 
        We want to store ALL of them.
        '''
        combinations.extend(all_combinations(alphabet, n-1, start_str + letter))
        #Although the base case already returns a list, you have to make
        #sure that you return a list in the recursive call too.
        return combinations
    
######################################################
    
#get a list of all the subsets of a list L
#L = [1, 2, 3]
#subsets = [[], [1], [2], [3], [1,2], [1,3] [2,3] [1,2,3]]
    
def get_all_subsets(L):
    '''We want to determine all subsets (combinations) that can be formed
    from a list L
    '''
    if len(L) == 0:
        return [[]]
    
    #The total subsets consists of all subsets that start with L[0]
    #and all those that don't.
    #all the subsets that contain L[0]
    #all the subsets that don't contain L[0]
    
    #We first get the subsets that do not start with L[0]
    all0 = get_all_subsets(L[1:])
    res = []
    
    #here, we get all subsets that start with L[0] by appending L[0]
    #to the start of all subsets that dont' start with L[0]
    for subset in all0:
        res.append([L[0]] + subset)
    #finally, we add the original subsets that didn't start with L[0]
    res.extend(all0)
    return res
        

    []
     |
    [3] -> [[], [3]]
     |
    [2,3] -> [[2], [2,3], [], [3]]
     |
    [1,2,3] -> [[1,2], [1,2,3], [1], [1,3], [2], [2,3], [], [3]]
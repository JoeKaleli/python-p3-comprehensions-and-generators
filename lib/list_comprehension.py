#!/usr/bin/env python3

def return_evens(num_list):
    evens = []
    for n in num_list: 
        if n % 2 == 0:
         evens.append(n)
    return evens

def make_exclamation(sentence_list):
    sentence = []
    for n in sentence_list:
       sentence.append(n + '!')
    return sentence
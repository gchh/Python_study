# -*- coding: utf-8 -*-
"""
Created on Sat Nov 22 09:57:06 2014

@author: Liyu Fu
"""
'''Step one:New Dictionary'''
dict1={}
for i in range(100):
    sentence = raw_input()
    word_list = sentence.split()
    for word in word_list:
        if word not in dict1:
            dict1[word] = set() #new word
        dict1[word].add(i+1) #update for dictionary
    
'''Step two:Print Index'''
answer_list = sorted(dict1.iteritems(),key=lambda d:d[0])#Sort by keyword of dictionary.
for word in answer_list:
    l = list(word[1])
    l.sort()
    print word[0]+': '+', '.join(map(str,l)) #Print Index

def print_answer(answer_set): #Output search results
    empty_set = set()									
    if empty_set == answer_set: #answer_set is empty
        print 'None'
    else:
        answer_list=list(answer_set)
        answer_list.sort()
        print ', '.join(map(str,answer_list)) #Print answer of Query
        
'''Step three:Retrieval'''       
while True:
    Query = raw_input() 
    if Query == '': break #Exit condition
    answer_set = set()         
    if 'OR:' in Query: #OR-Retrieval
        Query = Query[3:]
        Q_word_list = Query.split()
        for word in Q_word_list:
            if (word != '')and(word in dict1):
                answer_set = dict1[word]|answer_set #set or
        print_answer(answer_set)
    else: #AND-Retrieval
        if 'AND:' in Query:Query = Query[4:]
        Q_word_list = Query.split()
        if Q_word_list!=[]:
            for i in range(1,101):answer_set.add(i)          
            for word in Q_word_list:
                if (word != ''):
                    if word in dict1:
                        answer_set = dict1[word]&answer_set #set and
                    else:answer_set = set() #wrong word
            print_answer(answer_set)                         
        else:print 'None'

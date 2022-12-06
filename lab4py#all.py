# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 08:49:53 2022

@author: MaKaNaK
"""

with open('E:\\data.txt','r') as file:
    max_ =0 
    lines = file.read().splitlines()
    for sen in lines:
        wds =sen.split()
        for c in wds:
            if len(c) > max_ :
                max_ = len(c)
                
    print(max_)


words=[]
with open('E:\\data.txt','r') as file:
    lines = file.read().splitlines()
    for sen in lines: 
        word = sen.split()
        words = words +word 
        
for e in words:
  print(f'frequency : {e} is {words.count(e)}')        
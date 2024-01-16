# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 15:45:41 2023

@author: USER
"""

#21點
cards=list()
import random
def newPoke():
    cards.clear()
    for i in range(4):
        for x in range(1,14):
            cards.append(x)
newPoke()
print(cards)
print()
def washPoke():
    for i in range(200):
        first=random.randint(0,len(cards)-1)
        end=random.randint(0,len(cards)-1)
        cards[first],cards[end]=cards[end],cards[first]
washPoke()
print(cards)
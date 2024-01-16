# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 10:10:07 2023

@author: USER
"""

from GameSword import SwordMan
from GameAdviser import Adviser
import random

def Fight(role1,role2):
    print(role1.getName(),end='')
    role1.fight()
    blood = random.randint(0,20)   
    print(role2.getName(),'損失',blood,'血量')
    role2.changeHp(blood)
    

if __name__ =='__main__':
    roles=list()
    for i in range(2):
        role=int(input('劍士按1,軍師按2:'))
        name=input('輸入姓名:')
        if role == 1:
            r=SwordMan(name,300,100)
            roles.append(r)
        else:
            r=Adviser(name,200,500)
            roles.append(r)
            
    while roles[0].getHp()>0 and roles[1].getHp()>0:
        ran = random.randint(1,100)
        if ran%2 == 0:
           Fight(roles[0],roles[1])
        else:
           Fight(roles[1],roles[0])
            
    print()
    print()
    if roles[0].getHp()>0:
        print(roles[0].getName(),'Win')
    else:
        print(roles[1].getName(),'Win')
            
            
            
            
            
            
            
            

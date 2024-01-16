# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 09:59:23 2023

@author: USER
"""

from GameRole import Role
class Adviser(Role):
    
    def fight(self):
        print('搖扇攻擊')
        
    def skill(self):
        print('三十六計...撤')
        
    def cure(self):
        print('進行大補血')
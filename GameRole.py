# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 09:31:29 2023

@author: USER
"""

class Role:
    
    def __init__(self,name,hp,mp):
        self.__name=name
        self.__hp=hp
        self.__mp=mp
    
    def fight(self):
        print('角色攻擊')
        
    def getName(self):
        return self.__name
    
    def getHp(self):
        return self.__hp
    
    def setName(self,name):
        self.__name = name
        
    def setHp(self,hp):
        self.__hp=hp
        
    def setMp(self,mp):
        self.__mp=mp
        
    def changeHp(self,hp):
        self.__hp -= hp
        
        
        
        
        
        
        
        
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 17:19:02 2019

@author: LKK
"""

#will build 3 different databases
#each database has 10,0000 tuples
#A tuple has d attributes of type double and one bulk atrrtibute with garbage characters to ensure that each tuple is 100 bytes long.
#The valus of the d doubles of a tuple are generated randomly in the rage of 0,1
import numpy as np
import random
import string
import time
from sys import getsizeof

def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

class record :
    bulk = ''
    att = []
    def __init__(self,d) :
        self.bulk = randomString(100) 
        self.att = np.random.uniform(0,1,(1,d))
        
#indep
def build_indep () :
    indep_database = []
    for i in range(0,100000) :
        indep_database.append(record(2))
    return indep_database  

def dominate (record, target) :
    for att in record :
        pass
    
def BNL_basic (database) :
    start_time = time.time()
    operating_setting = np.zeros.((database[0].att.shape),dtype='i2') ## 0 for min 1 for max 2 for distinct, basically for min
    w_size = 1024 // getsizeof(database[0])
    window = np.array((1,w_size), dtype='o')
    temp = []
    skylines = []
    while not database :
        for record in database :
            if not window :
                window.append(record)
                del record
                continue
            for target in window :
                dominate (record, target)
            
    
    
    
    
    
    cost_time = start_time - time.time()
    
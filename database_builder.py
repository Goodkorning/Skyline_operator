# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 17:19:02 2019

@author: LKK
"""

#will build 3 different databases
#each database has 10,0000 tuples
#A tuple has d attributes of type double and one bulk attribute with garbage characters to ensure that each tuple is 100 bytes long.
#The valus of the d doubles of a tuple are generated randomly in the rage of 0,1
import numpy as np
import random
import string
import time
import copy
from sys import getsizeof

def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

class record :
    bulk = ''
    att = []
    def __init__(self,d) :
        self.bulk = randomString(10) 
        self.att = np.random.uniform(0,1,(1,d))
        
#indep
def build_indep () :
    indep_database = []
    for i in range(0,20) :
        indep_database.append(record(2))
    return indep_database  

def dominate (record1, record2) :
    result = record1.att - record2.att       
    if np.all(result>=0) :
        return 1 #record dominate target
    if np.all(result< 0) :
        return 2 #target dominate record
    else :
        return 0    #incomparable
    
def BNL_basic (origin_database) :
    start_time = time.time()
    database = copy.deepcopy(origin_database)
    #operating_setting = np.zeros.((database[0].att.shape),dtype='i2') ## 0 for min 1 for max 2 for distinct, basically for min
    #w_size = 1024 // getsizeof(database[0])
    w_size = 3
    window = []
    temp = []
    skylines = []
    
    while database :
        for record in list(database) :
            if not window :
                window.append(record)
                database.remove(record)
                continue                
            record_dominated = False
            for target in list(window) :
                if dominate(record, target) == 2 :
                    database.remove(record)
                    record_dominated = True
                    break
                elif dominate(record, target) == 1 :
                    window.remove(target)
                    continue
                elif dominate(record, target) == 0 :
                    continue
            if record_dominated :
                continue
            if len(window) < w_size :               
                window.append(record)
            else :
                temp.append(record)
            database.remove(record)            
        skylines = skylines + window
        database = temp
    cost_time = time.time() - start_time
    return [cost_time, skylines]
    
    
database = build_indep ()
for att in database :
    print(att.att)
BNL_basic (database)
    
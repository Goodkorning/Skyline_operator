# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 16:12:58 2019

@author: LKK
"""
import numpy as np
from sys import getsizeof
import time
import copy

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
    w_size = 1024 // getsizeof(database[0])
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
        temp.clear()
    cost_time = time.time() - start_time
    return [cost_time, skylines]
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

    
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
import seaborn as sns


#function to convert data entry in weight to integer
def convert_lbs_to_int(pounds):
    if type(pounds) == str:
        if pounds.endswith('lbs'):
            return int(pounds[:-3])
    elif np.isnan(pounds):
        return

    
#splitting the bust size entry
def separate_band_and_cup(bust_size):
    if type(bust_size) == str:
        return bust_size[:2]+','+bust_size[2:]
    elif np.isnan(bust_size):
        return np.NaN, np.NaN

    
#converting string heights to integer
def convert_feetinches_to_inches(distance):
    if type(distance) == str:
        inches = 0
        for i, ft in enumerate(distance):
            if ft=='f' or ft=='\'':
                inches += 12*int(distance[:i])
            if ft=='i' or ft=='\"':
                inches += int(distance[i-2:i].strip())
        return inches
    elif np.isnan(distance):
        return np.NaN

#converting string band entry to integer    
def convert_to_int(band):
    if type(band)==str:
        return int(band)
    elif band==np.NaN:
        pass

#replace NaN values for either hips or waist to yield moderate risk body proportion
def hip_waist_ratio(data):
    lst = []
    for x in data:
        y = list(x)
        if math.isnan(y[0]) == True and math.isnan(y[1]) == False:
            y[0] = round(y[1]*.85,0)
            lst.append(y)
            
        elif math.isnan(y[1]) == True and math.isnan(y[0]) == False:
            y[1] = round(y[0]/.85,0)
            lst.append(y)

        else:
            lst.append(y)
    return lst


#bootstrap resampling
np.random.seed(1234)
def bootstrap( data,m, n,):
    result = []
    for i in range( n):
        xs = np.random.choice(data, m, replace = True)
        m1 = np.mean( xs)
        result.append( m1)
    return result
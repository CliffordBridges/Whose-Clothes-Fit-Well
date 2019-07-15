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
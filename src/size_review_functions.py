import math
import numpy as np


def convert_lbs_to_int(pounds):
    """
    Converts weight entry from a string ending in 'lbs' to an int
    
    Parameters
    ----------
    pounds: str
        string likely ending in 'lbs' 
    """    
    if type(pounds) == str:
        if pounds.endswith('lbs'):
            return int(pounds[:-3])
    elif np.isnan(pounds):
        return

    
def separate_band_and_cup(bust_size):
    """
    Splits the int and string (band and cup)
    
    Parameters
    ----------
    bust_size: str
        likely a 2 digit integer followed by some nunber of letters
    """
    if type(bust_size) == str:
        return bust_size[:2]+','+bust_size[2:]
    elif np.isnan(bust_size):
        return np.NaN, np.NaN

    
#converting string heights to integer
def convert_feetinches_to_inches(distance):
    """
    Converts height as string with feet and inches to just inches
    
    Parameters
    ----------
    distance: str
        likely an integer, single quote, space, integer, double quote
    """
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

def convert_to_int(band):
    """
    Converts band size to int
    
    Parameters
    ----------
    band: str
        band size in inches
    """
    if type(band)==str:
        return int(band)
    elif band==np.NaN:
        pass

def hip_waist_ratio(data):
    """
    If exactly one measurement for hips or waist is NaN, 
    replaces NaN value so the resulting hip-waist ratio is 0.85

    Parameters
    ----------
    data: list
        list of ordered pairs (waist, hip)
    
    Returns
    -------
    lst: list
        list of "ordered" lists
    """
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


def bootstrap(data, m, n,):
    """
    Bootstrap function
    
    Parameters
    ----------
    data: 1-D array-like or int
        If an ndarray, a random sample is generated from its elements.
        If an int, the random sample is generated as if a were np.arange(a)
        
    m: int
        Sample size from data to be selected (with replacement)
        
    n: int
        Number of samples to choose and take mean
    """
    np.random.seed(1234)
    result = []
    for i in range(n):
    xs = np.random.choice(data, m, replace = True)
        m1 = np.mean(xs)
        result.append(m1)
    return result
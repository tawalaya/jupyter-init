#! /usr/bin/env python3

import pandas as pd
import numpy as np

def load(store_cache_file=False,cache_file=None):
    if not store_cache_file and cache_file:
        return pd.load(cache_file)
    else:
        #TODO load your data into a DataFrame
        result = pd.DataFrame() #replace with your data
        
        if store_cache_file and cache_file:
            result.to_csv(cache_file)
        
        return result
    
    
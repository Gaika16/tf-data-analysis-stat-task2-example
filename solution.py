import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 1119567869 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
     x = x / 100
    
    alpha = 1 - p
    loc = x.mean()
    scale = np.sqrt(np.var(x)) / np.sqrt(len(x))
    chi2_left = chi2.ppf(alpha / 2, df=len(x)-1)
    chi2_right = chi2.ppf(1 - alpha / 2, df=len(x)-1)
    return np.sqrt(((len(x)-1) * np.var(x)) / chi2_right), \
           np.sqrt(((len(x)-1) * np.var(x)) / chi2_left)

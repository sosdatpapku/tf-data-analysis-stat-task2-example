import pandas as pd
import numpy as np

from scipy.stats import norm, chi2


chat_id = 1188007817 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    n = len(x)
    alpha = 1 - p
    s2 = np.sum((x-np.mean(x))**2)/(n-1)
    q1 = chi2.ppf(alpha/2, n-1)
    q2 = chi2.ppf(1-alpha/2, n-1)
    ci = np.sqrt((n-1)*s2/q1), np.sqrt((n-1)*s2/q2)
    return ci

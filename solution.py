import pandas as pd
import numpy as np

from scipy.stats import norm, chi2


chat_id = 1188007817 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    R_squared = sum([d**2 for d in distances])
    S_squared = R_squared / (2*n)
    alpha = 1 - p

# доверительный интервал для sigma^2
    df = n-1
    chi2_lower = chi2.ppf(alpha/2, df)
    chi2_upper = chi2.ppf(1-alpha/2, df)
    sigma_squared_interval = [(df*S_squared)/chi2_upper, (df*S_squared)/chi2_lower]

# доверительный интервал для sigma
    sigma_interval = [np.sqrt(s) for s in sigma_squared_interval]
    return sigma_interval 

import pandas as pd
import numpy as np
from scipy.stats import mannwhitneyu
# import scipy.stats as sps


chat_id = 341395919 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
#     p_value = sps.permutation_test((x, y), lambda x, y, axis: np.mean(x, axis=axis) - np.mean(y, axis=axis), 
#              vectorized=True, 
#              n_resamples=500,
#              alternative='greater').pvalue 
#     alpha = 0.05
#     return p_value < alpha # Ваш ответ, True или False
    pval = mannwhitneyu(x, y, alternative="less").pvalue
    return pval < 0.05

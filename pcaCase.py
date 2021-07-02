from sklearn.decomposition import PCA
from sklearn.decomposition import TruncatedSVD 
from numpy.linalg import inv, eig, svd
from sklearn.manifold import TSNE
from sklearn.decomposition import KernelPCA
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas import read_csv, set_option
from pandas.plotting import scatter_matrix
import seaborn as sns
from sklearn.preprocessing import StandardScaler

dataset = read_csv('dji.csv', index_col=0)
print(dataset.shape)
import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np 

df = pd.read_csv('../tables/mtcars.csv')

df_plot = (
    df
    .rename({'Unnamed: 0': 'name'}, axis=1)
    .set_index('name')
    .assign(mpg_sorted = lambda x: sorted(x['mpg']), 
            disp_sorted = lambda x: sorted(x['disp']))
)

plt.plot(df_plot['mpg_sorted'], df_plot['disp_sorted'], linewidth=3, marker = 's', color='red', alpha=0.5, markeredgecolor='red', markerfacecolor = 'green', markersize = 10, linestyle='None')

plt.show()
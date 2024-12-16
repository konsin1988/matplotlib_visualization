import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np 

df = pd.read_csv('../tables/mtcars.csv')

df_plot = (
    df
    .rename({'Unnamed: 0': 'name'}, axis=1)
    .set_index('name')
    .assign(mpg_sorted = lambda x: sorted(x['mpg']), 
            disp_sorted = lambda x: sorted(x['disp']),
            qsec_sorted= lambda x: sorted(x['qsec']),
            disp_sorted_2 = lambda x: sorted(x['disp']))
    
)

# plt.figure(figsize=(15,10))
plt.plot(df_plot['mpg_sorted'], df_plot['disp_sorted'], label='mpg_sorted')
plt.plot(df_plot['qsec_sorted'], df_plot['disp_sorted_2'],
         linewidth = 6, label='qsed_sorted'
         )
plt.legend(fontsize=20, loc='lower right', bbox_to_anchor = (1, 0), borderaxespad = 2)

plt.style.use('Solarize_Light2')


plt.show()

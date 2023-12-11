import pandas as pd
import numpy as np


df3 = pd.read_csv("../datasets/dataset-3.csv")

def calculate_distance_matrix(df):
    r_df=pd.pivot_table(df,values="distance",index="id_start",
                        columns="id_end",fill_value=0).cumsum(axis=1)

    n = r_df.shape[0]
    for i in range(n):
        for j in range(i+1, n):
            r_df.iloc[j, i] = r_df.iloc[i, j]


    return r_df.head()

print(calculate_distance_matrix(df3))

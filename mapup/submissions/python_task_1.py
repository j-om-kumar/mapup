import pandas as pd
import numpy as np


df = pd.read_csv("../datasets/dataset-1.csv")
df2 = pd.read_csv("../datasets/dataset-2.csv")

def generate_car_matrix(df):

    matrix=pd.pivot(df,values="car",index="id_1",columns="id_2")
    ## TASK-Q1.PNG HAS THE ANSWER FOR BUS
    # matrix=pd.pivot(df,values="bus",index="id_1",columns="id_2")

    np.fill_diagonal(matrix.values,0)

    return matrix.head()


# print(generate_car_matrix(df))

def get_type_count(df):
    car=df["car"]
    def conditions(car):
        if  car <=15:
            return "low"
        elif  car >15 and car <=25:
            return "medium"
        else:
            return "high"
    df['car_type'] = df['car'].apply(conditions)
    df.tail()

    counts=df["car_type"].value_counts().to_dict()

    return counts
    
# print(get_type_count(df))
def get_bus_indexes(df):

    mean=df["bus"].mean()

    indices=df[df["bus"]>(2*mean)].index

    indices.to_list().sort()

    return indices

# print(get_bus_indexes(df))

def filter_routes(df):
    avg=df.groupby("route")["truck"].mean()

    routes=avg[avg>7]

    return(routes.to_list())

# print(filter_routes(df))

def multiply_matrix(df):
    matrix=pd.pivot(df,values="bus",index="id_1",columns="id_2")
    np.fill_diagonal(matrix.values,0)

    modified_matrix = matrix.where(matrix <= 20, matrix * 0.75).where(matrix > 20, matrix * 1.25)

    modified_matrix=modified_matrix.round(1)
    return modified_matrix.head()

    ## FOR CAR
    # matrix=pd.pivot(df,values="bus",index="id_1",columns="id_2")
    # np.fill_diagonal(matrix.values,0)

    # modified_matrix = matrix.where(matrix <= 20, matrix * 0.75).where(matrix > 20, matrix * 1.25)

    # modified_matrix=modified_matrix.round(1)
    # return modified_matrix.head()

# print(multiply_matrix(df))

def check_timestamp_completeness(df): 

    df['start_timestamp'] = pd.to_datetime(df['startDay'] + ' ' + df['startTime'])


    df['end_timestamp'] = pd.to_datetime(df['endDay'] + ' ' + df['endTime'])

    return df

print(check_timestamp_completeness(df2))


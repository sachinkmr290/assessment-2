import pandas as pd
import numpy as np

def calculate_dist_mat(df):
    dist = {}
    for _, row in df.iterrows():
        id_start, id_end, distance = row['id_start'], row['id_end'], row['distance']
        dist[(id_start, id_end)] = distance
        dist[(id_end, id_start)] = distance  
    ids = df['id_start'].unique()
    dist_mat = pd.DataFrame(index=ids, columns=ids)
    for (id_start, id_end), distance in dist.items():
        dist_mat.loc[id_start, id_end] = distance

    dist_mat.fillna(0, inplace=True)

    for k in ids:
        for i in ids:
            for j in ids:
                dist_mat.loc[i, j] = min(dist_mat.loc[i, j], dist_mat.loc[i, k] + dist_mat.loc[k, j])

    return dist_mat

df = pd.read_csv(r"C:\Users\sachi\Downloads\MapUp-DA-Assessment-2024-main\MapUp-DA-Assessment-2024-main\datasets\dataset-2.csv")
print(df.columns)
dist_mat = calculate_dist_mat(df)
# print(dist_mat)

def unroll_distance_matrix(distance_matrix):
    unrolled_data = []

    for i, row in distance_matrix.iterrows():
        for j, distance in row.items():
            if i != j:
                unrolled_data.append([i, j, distance])

    return pd.DataFrame(unrolled_data, columns=['id_start', 'id_end', 'distance'])

distance_mat = pd.read_csv(r"C:\Users\sachi\Downloads\MapUp-DA-Assessment-2024-main\MapUp-DA-Assessment-2024-main\datasets\dataset-2.csv")
unrolled_df = unroll_distance_matrix(distance_mat)
# print(unrolled_df)

def calculate_toll_rate(df, rate_coefficients):
    result_df = df.copy()

    for vehicle_type, rate_coefficient in rate_coefficients.items():
        result_df[vehicle_type] = result_df['distance'] * rate_coefficient

    return result_df
rate_coefficients = {
    "moto": 0.8,
    "car": 1.2,
    "rv": 1.5,
    "bus": 2.2,
    "truck": 3.6
}
distance_mat = pd.read_excel(r"C:\Users\sachi\Downloads\MapUp-DA-Assessment-2024-main\MapUp-DA-Assessment-2024-main\excel-assessment.xlsm", sheet_name='Dataset')
result_df = calculate_toll_rate(unrolled_df, rate_coefficients)
print(result_df)

import pandas as pd
from datetime import datetime, timedelta

def calculate_time_based_toll_rates(df):
    df['start_day'] = df.index._data.astype(str)
    # df['start_time'] = pd.to_datetime(df['start_time'])
    df['start_time'] = df.index
    df['end_day'] = (df.index._data + timedelta(days=1)).astype(str)
    df['end_time'] = datetime.time(23, 59, 59)
    weekday_time_ranges = [(datetime.time(0), datetime.time(10)), (datetime.time(10), datetime.time(18)), (datetime.time(18), datetime.time(23, 59, 59))]
    weekday_discount_factors = [0.8, 1.2, 0.8]
    weekend_discount_factor = 0.7
    def apply_discount_factor(row):
        if row['start_day'].weekday() < 5:
            for start_time, end_time, discount_factor in zip(weekday_time_ranges, weekday_discount_factors):
                if start_time <= row['start_time'] < end_time:
                    return discount_factor
        else:
            return weekend_discount_factor
    df['discount_factor'] = df.apply(apply_discount_factor, axis=1)
    for vehicle_type in ['moto', 'car', 'rv', 'bus', 'truck']:
        df[vehicle_type + '_time_based'] = df[vehicle_type] * df['discount_factor']
    return df

df1 = pd.read_excel(r"C:\Users\sachi\Downloads\MapUp-DA-Assessment-2024-main\MapUp-DA-Assessment-2024-main\excel-assessment.xlsm", sheet_name='Dataset')
result_df1 = calculate_time_based_toll_rates(df1)
print(result_df1)
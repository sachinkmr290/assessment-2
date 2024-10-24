def reverse_by_num(arr,n):
    start =0
    end = n-1
    while end < len(arr):
        arr[start:end+1] = reversed(arr[start:end+1])
        start +=n
        end+=n
    if start < len(arr):
        arr[start:] = reversed(arr[start:])
    return(arr)
arr = [1,2,3,4,5,6,7,8]
n=3
print(reverse_by_num(arr,n))

def lst_dict(s):
    res={}
    for i in s:
        length = len(i)
        if length not in res:
            res[length]=[]
        res[length].append(i)
    return(dict(sorted(res.items())))
string = ["apple", "bat", "car", "elephant", "dog", "bear"]
output= lst_dict(string)
print(output)

def flat_func(nested_dict):
    flattened_dict = {}

    def flat_rec(nested_dict, prefix=""):
        for key, value in nested_dict.items():
            if isinstance(value, dict):
                flat_rec(value, prefix + key + ".")
            elif isinstance(value, list):
                for i, item in enumerate(value):
                    if isinstance(item, dict):
                        flat_rec(item, prefix + key + f"[{i}].")
                    else:
                        flattened_dict[prefix + key + f"[{i}]"] = item
            else:
                flattened_dict[prefix + key] = value

    flat_rec(nested_dict)
    return flattened_dict
input = {
    "road": {
        "name": "Highway 1",
        "length": 350,
        "sections": [
            {
                "id": 1,
                "condition": {
                    "pavement": "good",
                    "traffic": "moderate"
                }
            }
        ]
    }
}
out_dict = flat_func(input)
print(out_dict)


def perm(nums):
    result = []
    used = [False] * len(nums)

    def check_func(permutation):
        if len(permutation) == len(nums):
            result.append(permutation.copy())
            return

        for i in range(len(nums)):
            if not used[i]:
                used[i] = True
                permutation.append(nums[i])
                check_func(permutation)
                permutation.pop()
                used[i] = False

    check_func([])
    return result

nums = [1, 1, 2]
permutations = perm(nums)
print(permutations)


import re

def date_func(text):
    date_patterns = [
        r"\d{2}-\d{2}-\d{4}", 
        r"\d{2}/\d{2}/\d{4}", 
        r"\d{4}\.\d{2}\.\d{2}" 
    ]

    dates = []
    for pattern in date_patterns:
        dates.extend(re.findall(pattern, text))

    return dates

text = "I was born on 23-08-1994, my friend on 08/23/1994, and another one on 1994.08.23."
dates = date_func(text)
print(dates)

def maat_func(matrix):
    n = len(matrix)
    rot_matrix = [[matrix[j][i] for j in range(n)] for i in range(n - 1, -1, -1)]
    # trans_matrix = [[sum(row) - rot_matrix[i][j] for j in range(n)] for i, row in enumerate(rot_matrix)]

    return rot_matrix,
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rot_mat = maat_func(matrix)
print(rot_mat)

import pandas as pd
from datetime import datetime, timedelta

def check_time_func(df):
    df['startDay'] = '2024-10-24 ' + df['startDay']
    df['start_timestamp'] = pd.to_datetime(df['startDay'] + ' ' + df['startTime'], format='%Y-%m-%d %A %H:%M:%S')
    df['end_timestamp'] = pd.to_datetime(df['endDay'] + ' ' + df['endTime'])
    df['duration'] = df['end_timestamp'] - df['start_timestamp']
    df['duration_correct'] = df['duration'] == timedelta(days=1)
    df['day_span_correct'] = df['end_timestamp'].dt.dayofweek - df['start_timestamp'].dt.dayofweek >= 6
    return df['duration_correct'] & df['day_span_correct']

data = pd.read_csv(r"C:\Users\sachi\Downloads\MapUp-DA-Assessment-2024-main\MapUp-DA-Assessment-2024-main\datasets\dataset-1.csv")
op = check_time_func(data)
print(op)
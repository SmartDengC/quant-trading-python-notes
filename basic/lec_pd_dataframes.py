import pandas as pd

dates = ['2020-01-02','2020-01-03','2020-01-06','2020-01-07','2020-01-08','2020-01-09',
         '2020-01-10','2020-01-13','2020-01-14','2020-01-15']

# Close prices
prices = [7.1600,7.1900,7.0000,7.1000,6.8600,6.9500,7.0000,7.0200,7.1100,7.0400]


def learn_pandas_series():
    bday = [i for i in range(len(dates))]

    ser1 = pd.Series(data=prices, index=dates)
    ser2 = pd.Series(data=bday, index=dates)

    df1 = pd.DataFrame({'clone': ser1, 'bday': ser2})

    print(df1)


def learn_pandas_dataframe_sort():
    ser = pd.Series(data=[1,3,2], index=['a', 'c', 'b'])
    # 判断索引是否有序
    print(ser.is_monotonic_increasing)
    sorted_ser = ser.sort_index()
    print(sorted_ser)

    x = sorted_ser['a': 'b']
    print(x)

    y = sorted_ser['b': 'z']
    print(y)


learn_pandas_dataframe_sort()


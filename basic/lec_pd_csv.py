# 看到章节：3.4.7 Python 和 Pandas 中的日期
import pandas as pd


def read_csv():
    df = pd.read_csv('../input_csv/qan_prc_2020.csv')
    print(df.loc[:, 'close'])
    print(df.info)
    df.set_index('date', inplace=True)
    print(df)
    print(df.loc['1/2/2020'])

    # df.to_csv('../output_csv/qan_prc_2020.csv')
    ser = df.loc[:, 'close']
    print(ser.name)


read_csv()
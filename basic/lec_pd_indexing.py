import pandas as pd

# ----------------------------------------------------------------------------
#   The dates and prices lists
# ----------------------------------------------------------------------------
dates = [
  '2020-01-02',
  '2020-01-03',
  '2020-01-06',
  '2020-01-07',
  '2020-01-08',
  '2020-01-09',
  '2020-01-10',
  '2020-01-13',
  '2020-01-14',
  '2020-01-15',
  ]

prices = [
  7.1600,
  7.1900,
  7.0000,
  7.1000,
  6.8600,
  6.9500,
  7.0000,
  7.0200,
  7.1100,
  7.0400,
  ]

# Trading day counter
bday = [
  1,
  2,
  3,
  4,
  5,
  6,
  7,
  8,
  9,
  10]


def learn_pandas_series():
  ser = pd.Series(data=prices, index=dates)
  print(ser)

  df = pd.DataFrame(data={'Close': ser, 'Trading Day': bday}, index=dates)
  print(df)

  x = df.loc['2020-01-13']
  print(x)

  new_ser = ser.copy()
  new_ser.loc['2020-01-02'] = 7.22

  print(new_ser)

  print(new_ser.loc[['2020-01-02', '2020-01-10']])
  print(new_ser.loc['2020-01-02': '2020-01-10'])


def learn_pandas_dataframe():
  ser = pd.Series(data=prices, index=dates)
  df = pd.DataFrame(data={'Close': ser, 'Trading Day': bday}, index=dates)
  # print(df)

  print(df.loc['2020-01-02', :])
  print(df.loc[:, 'Close'])

learn_pandas_dataframe()
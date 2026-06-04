# http://tushare.org/
# http://tushare.org/trading.html#id2
# https://tushare.pro/weborder/#/user/privilege

# https://tushare.pro/document/2

import tushare as ts

# 设置你的token
token_str = ''
ts.set_token(token_str)

# 选择你感兴趣的股票
stock_code = '603019'

# 获取历史数据
# 本接口即将停止更新，请尽快使用Pro版接口：https://tushare.pro/document/2
df = ts.get_hist_data(stock_code)

# 计算5天和20天的移动平均线
df['MA5'] = df['close'].rolling(window=5).mean()
df['MA20'] = df['close'].rolling(window=20).mean()

# 找到5天移动平均线从下方穿越20天移动平均线的点
buy_signals = (df['MA5'] > df['MA20']) & (df['MA5'].shift(1) < df['MA20'].shift(1))

# 如果存在买入信号，打印买入
if buy_signals.any():
    print(f"Buy signal for {stock_code} on dates {buy_signals[buy_signals == True].index}")


change = 3.79
coins = [2, 1, 0.50, 0.20, 0.10, 0.05, 0.02, 0.01]

for coin in coins:
    number_of_coins = int(change / coin)
    remainder = round(change % coin, 2)  # round to avoid floating point issues

    print(str(coin) + ': ' + str(number_of_coins))
    change = remainder



'''
2     3.79  1 coin   remainder 1.79
1     1.79  1 coin   remainder 0.79
0.50  0.79  1 coin   remainder 0.29
0.20  0.29  1 coin   remainder 0.09
0.10
0.05  0.09  1 coin   remainder 0.04
0.02  0.04  2 coin   remainder
'''

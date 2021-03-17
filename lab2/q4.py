# Hung Yiu Pan
# 1155108381
# CSCI1040 Lab2 Q4

def max_profit(prices):
    #TODO: return the maximum profit
    max = 0
    for i in range(len(prices)-1):
        for j in range(i+1,len(prices)):
            if(prices[j] - prices[i] > max):
                max = prices[j] - prices[i]
    return max



AAPL = [12.5, 20.3, 23.2, 1.5, 2.6, 5.3, 7.5, 10.9]
GOOG = [1.8, 3.2, 8.0, 7.5, 1.0, 5.3, 12.8, 0.9]
print(max_profit(AAPL))
print(max_profit(GOOG))
def max_profit(prices):
    return sum([prices[i+1]-prices[i] for i in range(len(prices)-1) if prices[i]<prices[i+1]])


if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    print(max_profit(prices))

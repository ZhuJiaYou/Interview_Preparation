def max_stock_profit(prices):
    profits = 0
    buy = float('inf')
    for price in prices:
        profits = max(profits, price-buy)
        buy = min(buy, price)
    return profits


if __name__ == '__main__':
    prices = [9, 11, 8, 5, 7, 12, 16, 14]
    print(max_stock_profit(prices))

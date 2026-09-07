prices = list(map(int, input().split()))

if len(prices) < 2:
    print(0)

else:
    min_price = prices[0]
    profit = float('-inf')
    for p in prices[1:]:
        profit = max(profit, p-min_price)
        min_price = min(p, min_price)

    print(profit)
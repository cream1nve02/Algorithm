from collections import deque

prices = [1, 2, 3, 2, 3]

def get_price_not_fall_period(prices):
    result = [] # 결과 저장 array
    prices_queue = deque(prices)

    while prices_queue: # prices_queue가 비어있지 않을 동안 반복
        price_not_fall_period = 0
        current_price = prices_queue.popleft()
        for next_price in prices_queue:
            if current_price <= next_price:
                price_not_fall_period += 1
            else:
                price_not_fall_period += 1
                break
        result.append(price_not_fall_period)
    return result

print(get_price_not_fall_period(prices))


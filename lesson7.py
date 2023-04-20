# def max_digit(number: int) -> int:
#     return int(max(f'{number}'))
#
#
# print(max_digit(384))

# def coins_count(amount: int, coins: tuple[int] = None) -> int:
#     if coins is None:
#         coins = (25, 10, 5, 1)
#     else:
#         coins = sorted(coins, reverse=True)
#     count = 0
#     for coin in coins:
#         count += amount // coin
#         amount -= (amount // coin) * coin
#     return count
#
#
# print(coins_count(49))

# numbers = [1, 2, 3, 4, 4, 3, 2, 1]
# def unique_numbers(numbers: list) -> bool:
#     for i in range(len(numbers) - 1):
#         if numbers[i] == numbers[i+1]:
#              return False
#     return True

data = {'a': 3, 'b': 1, 'c': 2}
data = sorted(data.items())
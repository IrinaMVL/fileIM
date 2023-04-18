# a = 5
# result = bin(a)
# print(result)

def decimal_to_binary(decimal: int) -> str:
    binary: str = ''
    while decimal > 1:
        binary = f'{decimal % 2}' + binary
        decimal //= 2
    binary = f'{decimal}' + binary
    return binary

def binary_to_decimal(binary: str) -> int:
    binary =
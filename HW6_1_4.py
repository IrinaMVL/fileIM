# text = [1, 2, 3, 'a', 'b', 'c', {'age': 32}]
# def filter_str(element):
#     for element in text:
#         if isinstance(text, str):
#             return True
#         else:
#             return False
#
#
# filter1 = filter(filter_str, text)
# print(filter1)

text = [1, 2, 3, 'a', 'b', 'c', {'age': 32}]
res = list(map(lambda x: x == str, text))
print(res)
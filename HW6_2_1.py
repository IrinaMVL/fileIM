list = [1, 5, 23, 6, 47, 84, 4, 9, 11]
res = [i for i in list if not i%2]
res1 = [i for i in list if i%2]
print(res + res1)
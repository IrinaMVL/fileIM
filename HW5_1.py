N = 5
M = 13
K = 100
while N:
    if not K % M:
        print(K)
        N -= 1
        K += M
    else:
        K += 1
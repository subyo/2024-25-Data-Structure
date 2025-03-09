def recSumFirstN(n):
    if n == 0:
        return 0
    return recSumFirstN(n-1) + n
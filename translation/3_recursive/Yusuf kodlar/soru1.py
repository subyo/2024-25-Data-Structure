def intpow(x, n):
    # Temel durum: n 0 ise 1 döndür
    if n == 0:
        return 1
    # Özyineleme durumu: x ^ n = x * x ^ (n-1)
    else:
        return x * intpow(x, n - 1)

print(intpow(2, 3))

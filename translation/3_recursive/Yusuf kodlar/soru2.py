def factorial(n):
    """
    Özyinelemeli olarak faktöriyel hesaplayan fonksiyon.

    Temel Durum: n 0 ise 1'i döndür.
    Özyineleme Durumu: n * (n-1)'in faktöriyelini hesapla.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def main():
    # Kullanıcıdan bir tamsayı al
    user_input = int(input("Bir tamsayı girin: "))

    # Faktöriyelini hesapla
    result = factorial(user_input)

    # Sonucu ekrana yazdır
    print(f"{user_input}'in faktöriyeli: {result}")

# Ana programı çağır
if __name__ == "__main__":
    main()

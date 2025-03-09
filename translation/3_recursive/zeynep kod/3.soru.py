def metin_uzunlugu_hesapla(metin, index=0):
    # Base case: metin boşsa uzunluk 0'dır
    if not metin:
        return 0
    
    # Recursive case: bir karakteri geç ve geri kalan metni kontrol et
    return 1 + metin_uzunlugu_hesapla(metin[1:], index + 1)

def main():
    # Kullanıcıdan metin girişi al
    girilen_metin = input("Bir metin girin: ")

    # Uzunluğu hesapla
    uzunluk = metin_uzunlugu_hesapla(girilen_metin)

    # Sonucu ekrana yazdır
    print("Girilen metnin uzunluğu:", uzunluk)

if __name__ == "__main__":
    main()

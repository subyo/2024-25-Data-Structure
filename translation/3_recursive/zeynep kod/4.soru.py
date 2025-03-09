def yerDegistir(text):
    # Metnin uzunluğunu kontrol et
    if len(text) <= 1:
        return text

    # İkişerli gruplar halinde metni döndür
    return text[1] + text[0] + yerDegistir(text[2:])

# Test durumları
test_metinler = ["abcdefgh", "12345678", "abc", "x", ""]

for metin in test_metinler:
    sonuc = yerDegistir(metin)
    print(f"Orijinal: {metin}, Yer Değiştirilmiş: {sonuc}")

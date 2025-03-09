def merge(dizi, baslangic, orta, bitis):

    """
    Verilen dizinin iki alt dizisini birleştirir.

    Parametreler:
        dizi: Birleştirilecek dizi.
        baslangic: Birinci alt dizinin başlangıç indisi.
        orta: İki alt dizinin ayırma indisi.
        bitis: İkinci alt dizinin bitiş indisi.

    Dönüş Değeri:
        Birleştirilmiş dizi.
    """

    sol = []
    sag = []

    # Sol alt diziyi kopyala
    for i in range(baslangic, orta):
        sol.append(dizi[i])

    # Sağ alt diziyi kopyala
    for i in range(orta, bitis):
        sag.append(dizi[i])

    i = 0
    j = 0
    k = baslangic

    # Sol ve sağ alt dizileri karşılaştır ve birleştir
    while i < len(sol) and j < len(sag):
        if sol[i] < sag[j]:
            dizi[k] = sol[i]
            i += 1
        else:
            dizi[k] = sag[j]
            j += 1
        k += 1

    # Kalan sol elemanları kopyala
    while i < len(sol):
        dizi[k] = sol[i]
        i += 1
        k += 1

    # Kalan sağ elemanları kopyala
    while j < len(sag):
        dizi[k] = sag[j]
        j += 1
        k += 1

    return dizi


def siralama(dizi, baslangic, bitis):

    """
    Verilen diziyi özyineli olarak birleştirme sıralaması ile sıralar.

    Parametreler:
        dizi: Sıralanacak dizi.
        baslangic: Sıralama işleminin başlangıç indisi.
        bitis: Sıralama işleminin bitiş indisi.

    Dönüş Değeri:
        Sıralanmış dizi.
    """

    if baslangic >= bitis - 1:
        return

    orta = (baslangic + bitis) // 2

    # Alt dizileri sırala
    siralama(dizi, baslangic, orta)
    siralama(dizi, orta, bitis)

    # Alt dizileri birleştir
    merge(dizi, baslangic, orta, bitis)


def birlestirme_siralama(dizi):

    """
    Verilen diziyi birleştirme sıralaması ile sıralar.

    Parametreler:
        dizi: Sıralanacak dizi.

    Dönüş Değeri:
        Sıralanmış dizi.
    """

    siralama(dizi, 0, len(dizi))

    return dizi
dizi = [5, 2, 4, 6, 1, 3]

birlestirme_siralama(dizi)

print(dizi)
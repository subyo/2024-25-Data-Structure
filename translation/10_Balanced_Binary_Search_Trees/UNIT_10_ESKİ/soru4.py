class AVLNode:
    def __init__(self, deger):
        self.deger = deger
        self.sol_cocuk = None
        self.sag_cocuk = None
        self.yukseklik = 1

class AVLAgaci:
    def __init__(self):
        self.kok = None

    def yukseklik(self, dugum):
        if not dugum:
            return 0
        return dugum.yukseklik

    def denge(self, dugum):
        if not dugum:
            return 0
        return self.yukseklik(dugum.sol_cocuk) - self.yukseklik(dugum.sag_cocuk)

    def saga_don(self, y):
        x = y.sol_cocuk
        T2 = x.sag_cocuk

        x.sag_cocuk = y
        y.sol_cocuk = T2

        y.yukseklik = 1 + max(self.yukseklik(y.sol_cocuk), self.yukseklik(y.sag_cocuk))
        x.yukseklik = 1 + max(self.yukseklik(x.sol_cocuk), self.yukseklik(x.sag_cocuk))

        return x

    def sola_don(self, x):
        y = x.sag_cocuk
        T2 = y.sol_cocuk

        y.sol_cocuk = x
        x.sag_cocuk = T2

        x.yukseklik = 1 + max(self.yukseklik(x.sol_cocuk), self.yukseklik(x.sag_cocuk))
        y.yukseklik = 1 + max(self.yukseklik(y.sol_cocuk), self.yukseklik(y.sag_cocuk))

        return y

    def ekle(self, dugum, deger):
        if not dugum:
            print(f"{deger} değeri AVL ağacına ekleniyor.")
            return AVLNode(deger)
        
        if deger < dugum.deger:
            dugum.sol_cocuk = self.ekle(dugum.sol_cocuk, deger)
        else:
            dugum.sag_cocuk = self.ekle(dugum.sag_cocuk, deger)

        dugum.yukseklik = 1 + max(self.yukseklik(dugum.sol_cocuk), self.yukseklik(dugum.sag_cocuk))

        denge = self.denge(dugum)

        # Sol Sol Durumu
        if denge > 1 and deger < dugum.sol_cocuk.deger:
            print(f"{dugum.deger} düğümü için sağa dönme işlemi yapılıyor. ({self.denge(dugum)})")
            return self.saga_don(dugum)

        # Sağ Sağ Durumu
        if denge < -1 and deger > dugum.sag_cocuk.deger:
            print(f"{dugum.deger} düğümü için sola dönme işlemi yapılıyor. ({self.denge(dugum)})")
            return self.sola_don(dugum)

        # Sol Sağ Durumu
        if denge > 1 and deger > dugum.sol_cocuk.deger:
            print(f"{dugum.deger} düğümü için sola dönme, sonra {dugum.deger} için sağa dönme işlemi yapılıyor. ({self.denge(dugum)})")
            dugum.sol_cocuk = self.sola_don(dugum.sol_cocuk)
            return self.saga_don(dugum)

        # Sağ Sol Durumu
        if denge < -1 and deger < dugum.sag_cocuk.deger:
            print(f"{dugum.deger} düğümü için sağa dönme, sonra {dugum.deger} için sola dönme işlemi yapılıyor. ({self.denge(dugum)})")
            dugum.sag_cocuk = self.saga_don(dugum.sag_cocuk)
            return self.sola_don(dugum)

        return dugum

    def anahtar_ekle(self, deger):
        self.kok = self.ekle(self.kok, deger)

    def min_deger_dugum(self, dugum):
        if dugum is None or dugum.sol_cocuk is None:
            return dugum
        return self.min_deger_dugum(dugum.sol_cocuk)

    def sil(self, dugum, deger):
        if not dugum:
            return dugum

        if deger < dugum.deger:
            dugum.sol_cocuk = self.sil(dugum.sol_cocuk, deger)
        elif deger > dugum.deger:
            dugum.sag_cocuk = self.sil(dugum.sag_cocuk, deger)
        else:
            if dugum.sol_cocuk is None:
                temp = dugum.sag_cocuk
                dugum = None
                return temp
            elif dugum.sag_cocuk is None:
                temp = dugum.sol_cocuk
                dugum = None
                return temp

            temp = self.min_deger_dugum(dugum.sag_cocuk)
            dugum.deger = temp.deger
            dugum.sag_cocuk = self.sil(dugum.sag_cocuk, temp.deger)

        if dugum is None:
            return dugum

        dugum.yukseklik = 1 + max(self.yukseklik(dugum.sol_cocuk), self.yukseklik(dugum.sag_cocuk))

        denge = self.denge(dugum)

        # Sol Sol Durumu
        if denge > 1 and self.denge(dugum.sol_cocuk) >= 0:
            return self.saga_don(dugum)

        # Sol Sağ Durumu
        if denge > 1 and self.denge(dugum.sol_cocuk) < 0:
            dugum.sol_cocuk = self.sola_don(dugum.sol_cocuk)
            return self.saga_don(dugum)

        # Sağ Sağ Durumu
        if denge < -1 and self.denge(dugum.sag_cocuk) <= 0:
            return self.sola_don(dugum)

        # Sağ Sol Durumu
        if denge < -1 and self.denge(dugum.sag_cocuk) > 0:
            dugum.sag_cocuk = self.saga_don(dugum.sag_cocuk)
            return self.sola_don(dugum)

        return dugum

    def anahtar_sil(self, deger):
        self.kok = self.sil(self.kok, deger)

    def sira_sag_sol_dolas(self, dugum):
        if dugum:
            self.sira_sag_sol_dolas(dugum.sol_cocuk)
            print(dugum.deger, end=" ")
            self.sira_sag_sol_dolas(dugum.sag_cocuk)

def avl_agaci_testi():
    avl = AVLAgaci()
    degerler = [9, 5, 10, 0, 6, 11, -1, 1, 2]

    for deger in degerler:
        avl.anahtar_ekle(deger)

    print("\nAVL Ağacının Sıra Sağ Sol Dolaşımı:")
    avl.sira_sag_sol_dolas(avl.kok)
    print("\n")

    silinecek_degerler = [10, 5, 9] 
    for deger in silinecek_degerler:
        print(f"\n{deger} değerini siliyoruz:")
        avl.anahtar_sil(deger)
        print("Silme işleminden sonra AVL Ağacının Sıra Sağ Sol Dolaşımı:")
        avl.sira_sag_sol_dolas(avl.kok)
        print("\n")

if __name__ == "__main__":
    avl_agaci_testi()

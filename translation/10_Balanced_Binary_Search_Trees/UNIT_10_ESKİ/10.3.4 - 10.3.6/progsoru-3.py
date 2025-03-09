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
    
######################## ANLAŞILABİLİRLİK #####################################
    print("\n\nBu kısım kodun anlaşılabilirliği için eklenmiştir.")
    print("İlk olarak 9 değeri ağaca eklenir. Bu değer ağacın kökü olur.")
    print("Ardından 5 değeri eklenir. Bu, 9'un soluna eklenir.")
    print("10 değeri eklenir. Bu, 9'un sağına eklenir.")
    print("0 değeri eklenir. Bu, 5'in soluna eklenir.")
    print("6 değeri eklenir. Bu, 5'in sağına eklenir.")
    print("11 değeri eklenir. Bu, 10'un sağına eklenir.")
    print("-1 değeri eklenir. Bu, 0'ın soluna eklenir.")
    print("1 değeri eklenir. Bu, 0'ın sağına eklenir.")
    print("2 değeri eklenir. Bu, 1'in sağına eklenir.")
    print("Son eklenen düğüm, AVL ağacının denge kriterlerini ihlal ettiği için bir dönme işlemi gerçekleştirilmiştir. Bu dönme işlemi, ağacın denge durumunu yeniden sağlamak için yapılmıştır. Sonuç olarak, ağaçta belirli bir düzgünleştirme işlemi uygulanmış ve ağaç, dengelenmiş bir yapıya kavuşmuştur.")
    
    print("\n Himmet Can Umutlu")
    
if __name__ == "__main__":
    avl_agaci_testi()

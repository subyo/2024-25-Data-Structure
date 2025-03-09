import datetime
import random
import time

def main():
    # Sonuçları içeren bir XML dosyası yazın
    dosya = open("ListAccessTiming.xml", "w")

    dosya.write('<?xml version="1.0" encoding="UTF-8" standalone="no" ?>\n')
    dosya.write('<Plot title="Ortalama Liste Eleman Erişim Zamanı">\n')

    # Boyutları 1000 ila 200000 olan listeleri test edin.
    xmin = 1000
    xmax = 200000

    # xList'te liste boyutlarını ve yList'te o boyuttaki ortalama erişim süresini kaydedin,  
    # 1000 alıntı için.
    xList = []
    yList = []

    for x in range(xmin, xmax + 1, 1000):
        xList.append(x)

        prod = 0

        # Boyutu x olan tüm 0'lardan oluşan bir liste oluşturun
        lst = [0] * x

        # Çöp toplama/bellek tahsisi tamamlansın
        # veya en azından durulsun
        time.sleep(1)

        # 1000 test alıntısından önceki zaman
        starttime = datetime.datetime.now()

        for v in range(1000):
            # Liste içinde rastgele bir konum bulun ve bir değeri alın.
            # Gerçekten alındığından emin olmak için o değerle sahte bir işlem yapın.
            index = random.randint(0, x - 1)
            val = lst[index]
            prod = prod * val

        # 1000 test alıntısından sonraki zaman
        endtime = datetime.datetime.now()

        # Başlangıç ve bitiş arasındaki fark.
        deltaT = endtime - starttime

        # Ortalama erişim zamanı için 1000'e bölün, ancak mikrosaniye cinsinden   
        # çarpmak için 1000000 ile çarpın.
        accessTime = deltaT.total_seconds() * 1000

        yList.append(accessTime)

    dosya.write(' <Axes>\n')
    dosya.write(' <XAxis min="' + str(xmin) + '" max="' + str(xmax) + '">Liste Boyutu</XAxis>\n')
    dosya.write(' <YAxis min="' + str(min(yList)) + '" max="' + str(60) + '">Mikrosaniye</YAxis>\n')
    dosya.write(' </Axes>\n')

    dosya.write(' <Sequence title="Liste Boyutuna Göre Ortalama Erişim Zamanı" color="red">\n')

    for i in range(len(xList)):
        dosya.write(' <DataPoint x="' + str(xList[i]) + '" y="' + str(yList[i]) + '"/>\n')

    dosya.write(' </Sequence>\n')

    # Bu bölüm, bir listenin içindeki 100 rastgele konuma erişimi test eder
    # 200.000 öğe ile, tüm konumların yaklaşık olarak aynı miktarda zamanda erişilebileceğini görmek için.
    xList = lst
    yList = [0] * 200000

    time.sleep(2)

    for i in range(100):
        starttime = datetime.datetime.now()
        index = random.randint(0, 200000 - 1)
        xList[index] = xList[index] + 1
        endtime = datetime.datetime.now()
        deltaT = endtime - starttime
        yList[index] = yList[index] + deltaT.total_seconds() * 1000000

    dosya.write(' <Sequence title="Erişim Zamanı Dağılımı" color="blue">\n')

    for i in range(len(xList)):
        if xList[i] > 0:
            dosya.write(' <DataPoint x="' + str(i) + '" y="' + str(yList[i] / xList[i]) + '"/>\n')

    dosya.write('</Sequence>\n')
    dosya.write('</Plot>\n')
    dosya.close()

if __name__ == "__main__":
    main()

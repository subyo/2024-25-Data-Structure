# Bu, turtle grafik modülünü içe aktarır.
import turtle

# Ana fonksiyon, programın ana kodunun yazıldığı yerdir.
def main():
    # Bu satır, kullanıcıdan bir giriş satırı okur.
    filename = input("Lütfen çizim dosyasının adını girin: ")

    try:
        # Çizim yapmak için bir Turtle Grafik penceresi oluşturun.
        t = turtle.Turtle()
        # Ekran programın sonunda kullanılır.
        screen = t.getscreen()

        # Bir sonraki satır, dosyayı "r" veya okuma için açar. "w" onu yazma için açardı.
        # "y" dosyayı yazmak için açar ve "a" dosyayı eklemek için açar (yani sonuna eklemek için).
        # Bu programda sadece dosyayı okumakla ilgileniyoruz.
        file = open(filename, "r")

        # Aşağıdaki for döngüsü, dosyanın satırlarını tek tek okur
        # ve döngünün gövdesini dosyanın her satırı için bir kez çalıştırır.
        for line in file:

            # strip yöntemi, satırın sonundaki yeni satır karakterini
            # ve satırın başında veya sonunda olabilecek boşlukları kaldırır.
            text = line.strip()

            # Aşağıdaki satır, metin değişkenini parçalarına ayırır.
            # Örneğin eğer metin bunu içeriyorsa"goto, 10, 20, 1, black" sonra
            # Komut listesi bu şekilde olacaktır ["goto", "10", "20", "1", "black"] sonra
            # Metni ayır.
            commandList = text.split(",")

            # çizim komutunu al
            command = commandList[0]
            if command == "goto":
                # float(commandList[1]) ifadesi,
                # commandList[1]'de bulunan dizeden bir float nesnesi oluşturur.
                # Benzer şekilde, int nesneleri için de tür dönüşümü yapabilirsiniz.
                try:
                    x = float(commandList[1])
                    y = float(commandList[2])
                    width = float(commandList[3])
                    color = commandList[4].strip()
                    t.width(width)
                    t.pencolor(color)
                    t.goto(x, y)
                except ValueError:
                    print("Hata: 'goto' komutu için sayısal değerler bekleniyor. Satır:", line.strip())
                except IndexError:
                    print("Hata: 'goto' komutu için eksik parametreler. Satır:", line.strip())

            elif command == "circle":
                try:
                    radius = float(commandList[1])
                    width = float(commandList[2])
                    color = commandList[3].strip()
                    t.width(width)
                    t.pencolor(color)
                    t.circle(radius) # Yazım hatası düzeltildi: cirle -> circle
                except ValueError:
                    print("Hata: 'circle' komutu için sayısal değerler bekleniyor. Satır:", line.strip())
                except IndexError:
                    print("Hata: 'circle' komutu için eksik parametreler. Satır:", line.strip())

            elif command == "beginfill":
                try:
                    color = commandList[1].strip()
                    t.fillcolor(color)
                    t.begin_fill()
                except IndexError:
                    print("Hata: 'beginfill' komutu için eksik parametreler. Satır:", line.strip())

            elif command == "endfill":
                t.end_fill() # Fazla virgül kaldırıldı

            elif command == "penup":
                t.penup()

            elif command == "pendown":
                t.pendown()

            else:
                print("Dosyada bilinmeyen komut bulundu:", command)
        # dosyayı kapat
        file.close()

        # çizimi yapmak için kullandığımız turtle'ı gizleyin.
        t.hideturtle() # Daha açıklayıcı isim: ht() -> hideturtle()

        # Bu, programın turtle grafik penceresini fare tıklanana kadar açık tutmasına neden olur.
        screen.exitonclick()
        print("Program Çalışması Tamamlandı.")

    except FileNotFoundError:
        print(f"Hata: Dosya bulunamadı: {filename}")
    except Exception as e:
        print(f"Beklenmeyen bir hata oluştu: {e}")

# Bu kod, her şeyin başlatılması için ana fonksiyonu çağırır.
if __name__ == "__main__": # Yazım hatası düzeltildi: _name_ -> __name__, _main_ -> __main__
    main()
import turtle

# Sabitler
HUMAN = -1
COMPUTER = 1
BOARD_SIZE = 3  # Oyun tahtasının boyutu

class Dummy:
    """
    Henüz bir hamle yapılmamış hücreleri temsil eden sınıf.
    """
    def __init__(self):
        pass

    def eval(self):
        return 0  # Henüz bir hamle yoksa 0 döndür

    def goto(self, x, y):
        pass  # Dummy nesnesi hareket etmez

class X(turtle.RawTurtle):  # RawTurtle'dan miras alıyoruz
    """
    'X' işaretini temsil eden sınıf.
    """
    def __init__(self, canvas):
        super().__init__(canvas)  # RawTurtle'ın init metodunu çağır
        self.hideturtle()  # Turtle'ı gizle
        # 'X' şeklini tanımla
        x_shape = ((-40, -36), (-40, -44), (0, -4), (40, -44), (40, -36),
                   (4, 0), (40, 36), (40, 44), (0, 4), (-40, 44),
                   (-40, 36), (-4, 0), (-40, -36))
        canvas.register_shape("X", x_shape)  # Şekli kaydet
        self.shape("X")  # Şekli ayarla
        self.penup()  # Çizgi çizme
        self.speed(0)  # En hızlı hız

    def eval(self):
        return COMPUTER  # Bu hücre bilgisayarın hamlesi

    def goto(self, x, y):  # X'i belirtilen konuma taşı
        self.setposition(x, y)
        self.showturtle()  # Turtle'ı göster

class O(turtle.RawTurtle):  # RawTurtle'dan miras alıyoruz
    """
    'O' işaretini temsil eden sınıf.
    """
    def __init__(self, canvas):
        super().__init__(canvas)  # RawTurtle'ın init metodunu çağır
        self.hideturtle()  # Turtle'ı gizle
        canvas.register_shape("circle", ((-10, -10), (-10, 10), (10, 10), (10, -10)))
        self.shape("circle")  # Şekli ayarla
        self.penup()  # Çizgi çizme
        self.speed(0)  # En hızlı hız

    def eval(self):
        return HUMAN  # Bu hücre insanın hamlesi

    def goto(self, x, y):  # O'yu belirtilen konuma taşı
        self.setposition(x, y)
        self.showturtle()  # Turtle'ı göster

# Örnek Kullanım:
if __name__ == '__main__':
    screen = turtle.Screen()  # Ekran oluştur
    screen.setup(width=600, height=600)  # Ekran boyutunu ayarla
    screen.title("Tic-Tac-Toe")  # Pencere başlığı

    board = [[Dummy() for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]  # Başlangıçta boş tahta

    # X ve O nesnelerini oluştur
    x_turtle = X(screen)
    o_turtle = O(screen)

    # Örneğin, tahtanın ortasına bir X yerleştirelim
    x_turtle.goto(0, 0)  # Tahtanın ortasına git

    # Örneğin, başka bir konuma bir O yerleştirelim
    o_turtle.goto(100, 100)

    screen.mainloop()  # Pencereyi açık tut
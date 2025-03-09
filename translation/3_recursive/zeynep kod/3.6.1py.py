import turtle

def drawSpiral(t, length, color, colorBase):
 # renk, değişen 24 bitlik bir değerdir 
 #her seferinde güzel bir renk efekti için
 if length == 0:
   return

# eski renk modulo 2ˆ24'e 2ˆ10 ekleyin
# modulo 2ˆ24 rengin değişmesini önler
#çok büyüyor.
 newcolor = (int(color[1:],16) + 2**10)%(2**24)

 # renk tabanı tamsayı değerini bul
 base = int(colorBase[1:],16)

  # şimdi yeni renk tabandan azsa
   # 2ˆ24 temel modülünü ekleyin. 
 if newcolor < base:
  newcolor = (newcolor + base)%(2**24)

 # yeni rengin dönüşümden sonraki onaltılık dize olmasına izin verin.
 newcolor = hex(newcolor)[2:]

  # önüne bir pound işareti ve sıfırlar ekleyin, böylece
   # 6 karakter uzunluğunda artı pound işaretidir.
  # uygun renk dizisi. 
 newcolor = "#"+("0"*(6-len(newcolor)))+newcolor

 t.color(newcolor)
 t.forward(length)
 t.left(90)

 drawSpiral(t, length-1, newcolor, colorBase)

def main():
 t = turtle.Turtle()
 screen = t.getscreen()
 t.speed(100)
 t.penup()
 t.goto(-100,-100)
 t.pendown()

 drawSpiral(t, 200, "#000000", "#ff00ff")

 screen.exitonclick()

if __name__ == "__main__":
 main()

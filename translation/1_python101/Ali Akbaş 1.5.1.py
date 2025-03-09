class Dog:
    # Bu, sınıfın kurucu metodudur. Bir Dog nesnesi oluşturulduğunda çağrılır.
    # "self" adlı referans Python tarafından otomatik olarak oluşturulur ve
    # yeni oluşturulan nesnenin alanını işaret eder. Python bunu bizim için
    # otomatik olarak yapar ancak "self" parametresini __init__ metodunun
    # (yani kurucunun) ilk parametresi olarak eklememiz gerekir.
    def __init__(self, name, month, day, year, speakText):
        self.name = name
        self.month = month
        self.day = day
        self.year = year
        self.speakText = speakText
        
    # Bu, nesnede saklanan speakText değerini döndüren bir erişim metodudur.
    # Dikkat ederseniz "self" bir parametredir. Her metodun ilk parametresi
    # "self"tir. "self" parametresi, mevcut nesneyi temsil eden bir referanstır.
    # Metod çağrıldığında, mevcut nesne noktanın (yani . operatörünün) sol
    # tarafında görünür.
    def speak(self):
        return self.speakText
    
    # Bu, ismi almak için kullanılan bir erişim metodudur.
    def getName(self):
        return self.name
    
    # Bu, doğum günü bilgisini kullanarak tarihi bir string olarak döndüren
    # başka bir erişim metodudur.
    def birthDate(self):
        return str(self.month) + "/" + str(self.day) + "/" + str(self.year)
    
    # Bu, Dog nesnesinin speakText değerini değiştiren bir değiştirme metodudur.
    def changeBark(self,bark):
        self.speakText = bark
        
    # Yeni bir yavru köpek oluştururken doğum gününü bilmiyoruz.
    # İlk köpeğin doğum gününe bir yıl ekleyerek belirleyelim.
    # speakText değeri, her iki köpeğin metninin birleştirilmesiyle oluşacaktır.
    # "self" parametresi, + operatörünün sol tarafındaki nesneyi temsil eder.
    # "otherDog" parametresi ise operatörün sağ tarafındaki köpeği temsil eder.
    def __add__(self,otherDog):
        return Dog("Puppy of " + self.name + " and " + otherDog.name, \
                   self.month, self.day, self.year + 1, \
                   self.speakText + otherDog.speakText)
  
def main():      
    boyDog = Dog("Mesa", 5, 15, 2004, "WOOOOF")
    girlDog = Dog("Sequoia", 5, 6, 2004, "barkbark")
    print(boyDog.speak())
    print(girlDog.speak())
    print(boyDog.birthDate())
    print(girlDog.birthDate())
    boyDog.changeBark("woofywoofy")
    print(boyDog.speak())
    puppy = boyDog + girlDog
    print(puppy.speak())
    print(puppy.getName())
    print(puppy.birthDate())
    
if __name__ == "__main__":
    main()
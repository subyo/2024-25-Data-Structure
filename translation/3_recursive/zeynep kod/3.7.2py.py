def revList(lst):
 # İşte temel durum
 if lst == []:
  return []

 # Bu fonksiyonun geri kalanı özyinelemeli durumdur.
 # Bu işe yarıyor çünkü onu daha küçük bir şeye çağırdık.
 # Lst[1:], lst'teki ilk öğe dışındaki tüm öğelerin bir dilimidir.
 restrev = revList(lst[1:])
 first = lst[0:1]

 # Şimdi parçaları bir araya getir.
 result = restrev + first

 return result


def main():
  print(revList([1,2,3,4]))

if __name__ == "__main__":
   main()


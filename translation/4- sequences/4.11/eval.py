def main():
    expr = input("Lütfen bir infix ifadesi girin: ")
    result = eval(expr)
    print("Sonuç",expr,"=",result)
    
if __name__ == "__main__":
    main()
    
# Bu Python kodu, kullanıcıdan bir “infix” matematiksel ifade alır ve bu ifadeyi değerlendirerek sonucunu hesaplar. 
# eval fonksiyonu, verilen ifadeyi bir Python ifadesi olarak değerlendirir ve çalıştırır. 
# Bu kod parçası, basit matematiksel işlemleri hesaplamak için kullanılabilir.
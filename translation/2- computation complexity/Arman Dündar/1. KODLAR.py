def find_value(my_list, value):
    for i in range(len(my_list)):
        if my_list[i] == value:
            return i
    return -1

my_list = [1, 2, 3, 4, 5]
value = int(input("Sayı giriniz: "))
index = find_value(my_list, value)

if index == -1:
    print("Değer listede bulunamadı.")
else:
    print(f'{value} sayısı {index}. indeksde bulundu')


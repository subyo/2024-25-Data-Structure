def revList2(lst):

 def revListHelper(index):
  if index == -1:
   return []

  restrev = revListHelper(index-1)
  first = [lst[index]]

  # Şimdi parçaları bir araya getirin.
  result = first + restrev

  return result

 # bu tek satırlık koddur.
 # revList2 fonksiyonu
 return revListHelper(len(lst)-1)


def main():
 print(revList2([1,2,3,4]))

if __name__ == "__main__":
 main()
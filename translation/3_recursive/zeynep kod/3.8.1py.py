def reverse(seq):
  SeqType = type(seq)
  emptySeq = SeqType()
 
  if seq == emptySeq:
   return emptySeq

  restrev = reverse(seq[1:])
  first = seq[0:1]

 # Şimdi parçaları bir araya getirin.
  result = restrev + first

  return result


def main():
  print(reverse([1,2,3,4]))
  print(reverse("hello"))
if __name__ == "__main__":
  main()
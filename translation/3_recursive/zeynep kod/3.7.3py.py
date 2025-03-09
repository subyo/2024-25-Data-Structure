def revString(s):
   if s == "":
     return ""

   restrev = revString(s[1:])
   first = s[0:1]
   # Şimdi parçaları bir araya getirin.
   result = restrev + first

   return result


def main():
  print(revString("hello"))

if __name__ == "__main__":
  main()
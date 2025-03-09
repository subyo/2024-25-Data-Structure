def __siftDownFromTo (self,fromIndex,lastIndex):
       '''fromIndex is the index of an element in the heap.
       Pre:data{fromIndex..lastIndex} satisfies the heap condition,
       except perhaps for the element data [fromIndex].
       Post: That element is sifted down as far as necessery to
       maintain the heap structure for data[fromIndex..lastIndex].'''
       
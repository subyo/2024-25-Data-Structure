def select(seq, start):
    minIndex = start

    for j in range(start+1, len(seq)):
        if seq[minIndex] > seq[j]:
            minIndex = j

    return minIndex

def selSort(seq):
    for i in range(len(seq)-1):
        minIndex = select(seq, i)
        tmp = seq[i]
        seq[i] = seq[minIndex]
        seq[minIndex] = tmp

seq = [5, 8, 2, 6, 9, 1, 0, 7]

selSort(seq)

print(seq)

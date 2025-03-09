def select(seq, start):
    minIndex = start

    for j in range(start+1, len(seq)):
        if seq[minIndex] > seq[j]:
            minIndex = j

    return minIndex

seq = [5, 8, 2, 6, 9, 1, 0, 7]
start = 0

print(select(seq, start))


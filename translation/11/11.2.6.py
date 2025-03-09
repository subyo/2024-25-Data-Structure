#11.2.6
def readRecord(file,recNum,recSize):
    file.seek(recNum*recSize)
    record = file.read(recSize)
    return record
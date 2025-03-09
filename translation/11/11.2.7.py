#11.2.7
import os


def main():
    attribTypeCols = ["int","char20","char60","int","int","int","int"]
    feedCols = ["int","int","int","char50","datetime","float","float","int","char50","int"]
    feedAttributeCols = ["int","int","float"]

    feedAttributeTable = open("FeedAttribute.tbl","r")

    if os.path.isfile("Feed.idx"):
        indexFile = open("Feed.idx","r")
        feedTableRecLength = int(indexFile.readline())
        feedIndex = eval(indexFile.readline())
    else:
        feedIndex = BTree(3)
        feedTable = open("Feed.tbl","r")
        offset = 0
        for record in feedTable:
            feedID = readField(record,feedCols,0)
            anItem = Item(feedID,offset)
            feedIndex.insert(anItem)
            offset+=1
            feedTableRecLength = len(record)

        print("Feed Table Index Created") 
        indexFile = open("Feed.idx","w")
        indexFile.write(str(feedTableRecLength)+"\n")
        indexFile.write(repr(feedIndex)+"\n")
        indexFile.close()

    if os.path.isfile("FeedAttribType.idx"):
        indexFile = open("FeedAttribType.idx","r")
        attribTypeTableRecLength = int(indexFile.readline())
        attribTypeIndex = eval(indexFile.readline())
    else:
        attribTypeIndex = BTree(3)
        attribTable = open("FeedAttribType.tbl","r")
        offset = 0
        for record in attribTable:
            feedAttribTypeID = readField(record,attribTypeCols,0)
            anItem = Item(feedAttribTypeID,offset)
            attribTypeIndex.insert(anItem)
            offset+=1
            attribTypeTableRecLength = len(record)

        print("Attrib Type Table Index Created")
        indexFile = open("FeedAttribType.idx","w")
        indexFile.write(str(attribTypeTableRecLength)+"\n")
        indexFile.write(repr(attribTypeIndex)+"\n")
        indexFile.close()

    feedTable = open("Feed.tbl","rb")
    feedAttribTypeTable = open("FeedAttribType.tbl", "rb")
    before = datetime.datetime.now()
    for record in feedAttributeTable:

        feedID = readField(record,feedAttributeCols,0)
        feedAttribTypeID = readField(record,feedAttributeCols,1)
        value = readField(record,feedAttributeCols,2)

        lookupItem = Item(feedID,None)
        item = feedIndex.retrieve(lookupItem)
        offset = item.getValue()
        feedRecord = readRecord(feedTable,offset,feedTableRecLength)
        feedNum = readField(feedRecord,feedCols,2)
        feedName = readField(feedRecord,feedCols,3)

        lookupItem = Item(feedAttribTypeID,None)
        item = attribTypeIndex.retrieve(lookupItem)
        offset = item.getValue()
        feedAttribTypeRecord = readRecord(feedAttribTypeTable,offset,attribTypeTableRecLength)
        feedAttribTypeName = readField(feedAttribTypeRecord,attribTypeCols,1)

        print(feedNum,feedName,feedAttribTypeName,value)
    after = datetime.datetime.now()
    deltaT = after - before
    milliseconds = deltaT.total_seconds() * 1000
    print("Time for the query with indexing was",milliseconds,"milliseconds.")    
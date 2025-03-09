 #11.2.5
import datetime
def readField(record,colTypes,fieldNum):

 offset = 0
 for i in range(fieldNum):
     colType = colTypes[i]

     if colType == "int":
        offset+=10
     elif colType[:4] == "char":
        size = int(colType[4:])
        offset += size
     elif colType == "float":
          offset+=20
     ...
 return eval

def main():
    attribTypeCols = ["int","char20","char60","int","int","int","int"]
    feedCols = ["int","int","int","char50","datetime","float","float","int","char50","int"]
    feedAttributeCols = ["int","int","float"]
    before = datetime.datetime.now()
    feedAttributeTable = open("FeedAttribute.tbl","r")
    for record in feedAttributeTable:
        feedID = readField(record,feedAttributeCols,0)
        feedAttribTypeID = readField(record,feedAttributeCols,1)
        value = readField(record,feedAttributeCols,2)
        feedTable = open("Feed.tbl","r")
        feedFeedID = -1
        while feedFeedID != feedID:
            feedRecord = feedTable.readline()
            feedFeedID = readField(feedRecord,feedCols,0)
        feedNum = readField(feedRecord,feedCols,2)
        feedName = readField(feedRecord,feedCols,3)
        feedAttribTypeTable = open("FeedAttribType.tbl", "r")
        feedAttribTypeIDID = -1
        while feedAttribTypeIDID != feedAttribTypeID:
            feedAttribTypeRecord = feedAttribTypeTable.readline()
            feedAttribTypeIDID = readField(feedAttribTypeRecord,attribTypeCols,0)
        feedAttribTypeName = readField(feedAttribTypeRecord,attribTypeCols,1)
        print(feedNum,feedName,feedAttribTypeName,value)
    after = datetime.datetime.now()
    deltaT = after - before
    milliseconds = deltaT.total_seconds() * 1000
    print("Time for the query without indexing was",milliseconds,"milliseconds.")
 
if __name__ == "__main__":
    main()
import titanicFileConfig

lineNum=0

def titanicStrSpit(dataStr):
    dataList = []
    tmpStr = dataStr
    for i in titanicFileConfig.splitList:
        dataList.append(tmpStr[0:tmpStr.index(i)])
        tmpStr = tmpStr[tmpStr.index(i)+len(i):]
    return dataList

with open(titanicFileConfig.inputFileName, "r" ) as file:
    for line in file:
        if lineNum == 0:
            print(line)
        else:
            tmpDataList = titanicStrSpit(line)
            tmpDataList[titanicFileConfig.indexOfSexCol] = tmpDataList[titanicFileConfig.indexOfSexCol].replace("female","F")
            tmpDataList[titanicFileConfig.indexOfSexCol] = tmpDataList[titanicFileConfig.indexOfSexCol].replace("male","M")
            tmpDataList.append(int(tmpDataList[titanicFileConfig.indexOfSibSpCol])+int(tmpDataList[titanicFileConfig.indexOfParchCol]))
            
            print(tmpDataList)

        lineNum+=1



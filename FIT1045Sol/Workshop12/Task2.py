def getAnswers():
    fileName = input('Enter Answer File: ')
    infile = open(fileName + '.txt','r')
    contents = infile.readlines()
    infile.close()

    ans = []

    for i in range(len(contents)):
        lineStr = contents[i].rstrip('\n')
        ans.append(lineStr)

    return ans

answers = getAnswers()
print(answers)

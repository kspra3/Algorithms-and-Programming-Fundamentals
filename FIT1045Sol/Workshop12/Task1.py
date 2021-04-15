def getQuestions():
    fileName = input('Enter Question File: ')
    infile = open(fileName + '.txt','r')
    contents = infile.readlines()
    infile.close()

    q = []

    for i in range(len(contents)):
        lineStr = contents[i].rstrip('\n')
        lineArr1 = lineStr.split(':',1)
        lineArr2 = lineArr1[1].split(',')
        q.append([lineArr1[0]])
        q[i].extend(lineArr2)

    return q


questions = getQuestions()
print(questions)

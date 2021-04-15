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

def startQuiz():
    questions = getQuestions()
    answers = getAnswers()
    correct = 0

    infile = open('revision.txt','w')
    
    for i in range (len(questions)):
        print ('-' * 40)
        for j in range (len(questions[i])):
            print(questions[i][j])
            
        input_answer = input('Answer is: ')
        if input_answer == answers[i]:
            correct += 1
            print('Correct')
        else:
            print('Correct answer is',answers[i])
            
            for j in range (len(questions[i])):
                infile.write(questions[i][j])
                infile.write('\n')
            infile.write('Correct answer is ' + answers[i])
            infile.write('\n\n')

    infile.close()
      
    print('-' * 40)
    print('Total correct answers:',correct)

startQuiz()

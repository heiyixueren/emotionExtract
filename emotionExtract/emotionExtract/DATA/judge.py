import os
if __name__ == '__main__':
    filePath = os.path.join(os.path.dirname(__file__),'result1.txt')
    file = open(filePath,'r')
    text = file.read()
    file.close()
    text = text.split('\n')
    testResult = []
    for each in text:
        each = float(each)
        testResult.append(each)
    filePath = os.path.join(os.path.dirname(__file__),'200.txt')
    file = open(filePath,'r')
    text = file.read()
    file.close()
    text = text.split('\r')
    result = []
    for each in text:
        each = each.split('    ')
        result.append(float(each[0]))
    
    #get the accuracy of the text
    acNum = 0
    size = len(testResult)
    region = 0.4
    difSet = []
    for i in range(0,size):
        tmp = 0
        if testResult[i] > region:
            tmp = 1
        elif testResult[i]<-1*region:
            tmp = -1
        
        if abs(tmp - result[i])<0.00001 or tmp==0:
            acNum += 1
        else:
            difSet.append(i+1)
    print acNum
    print difSet
        
            
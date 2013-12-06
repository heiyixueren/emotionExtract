
file1 = open("twitterTestData.txt")
text1 = file1.read()
text1 = text1.split("\n")

file2 = open("tms.result")
text2 = file2.read()
text2 = text2.split("\n")

result = open("result.txt","w")
size = len(text1)
for i in range(0,size-1):
    eachText1 = (text1[i].split("\t"))[1]
    #print text2[i]
    eachText2 = (text2[i].split("\t"))[0]
    result.write(eachText2+"\t"+eachText1+"\n")

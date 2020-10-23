import socket, glob, os
finalOutput = ".txt files in /home/data: \n"

#Output variables
allWordsCount = 0
mostWords = 0
mostWordsFile = ""
ip = ""

#Temp Variabl;es
tempWordLength = 0

##Get Files from /home/data
inPath = os.path.expanduser("/home/data")
os.chdir(inPath)
for file in glob.glob("*.txt"):
	finalOutput+=(file +"\n")
	#Count number of words in file, save that number if largest and save filename
	fileObj = open(file, "r")
	tempWordLength = len(fileObj.read().split())
	allWordsCount += tempWordLength
	if(tempWordLength>mostWords):
		mostWords=tempWordLength
		mostWordsFile=file
		
finalOutput+=("\n\nCount of all words per file: "+str(allWordsCount))
finalOutput+=("\n\nFile with most words was "+mostWordsFile+" with "+str(mostWords)+" words\n")

##Get IP
ip = socket.gethostbyname(socket.gethostname())
finalOutput+="Ip: "+ip+"\n"

##Write output
if not os.path.exists("/home/output"):
	os.makedirs("/home/output")
output = open("/home/output/result.txt","a")
output.write(finalOutput)
output.close()

#print output to terminal
print(finalOutput)

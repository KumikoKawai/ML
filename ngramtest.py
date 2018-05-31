import urllib.request
import re
import string
import operator
import csv

def cleanText(input):
    input = re.sub('\n+', " ", input).lower() # change line &Transcoding mark change to Empty case
    input = re.sub('\[[0-9]*\]', "", input) # Removal of similarity [1] ferential quotation mark
    input = re.sub(' +', " ", input) #change two or more empty cases to one empty case
    #input = bytes(input)#.encode('utf-8') # contents change to utf-8 formal
    #input = input.decode("ascii", "ignore")
    return input

def cleanInput(input):
    input = cleanText(input)
    cleanInput = []
    input = input.split(' ') # split with empty case, return result

    for item in input:
        item = item.strip(string.punctuation) # string.punctuation gain all sign

        if len(item) > 0 or (item.lower() == 'a' or item.lower() == 'i'): #find Lonely
            cleanInput.append(item)
    return cleanInput

def getNgrams(input, n):
    input = cleanInput(input)

    output = {} # Structure dictionary
    for i in range(len(input)-n+1):
        ngramTemp = " ".join(input[i:i+n])#.encode('utf-8')
        if ngramTemp not in output: # calculate code frequency
            output[ngramTemp] = 0 
        output[ngramTemp] += 1
    return output

def createListCSV(fileName="", dataList=[]):
    with open(fileName, "w",newline='') as csvFile:
        csvWriter = csv.writer(csvFile,delimiter=',')
        for data in dataList:
            csvWriter.writerow(data)
            csvFile.close


#url = 'http://pythonscraping.com/files/inaugurationSpeech.txt'
#data = urllib.request.urlopen(url).read()
data = open("/Users/yuhanliu/Downloads/test1127/under2changetosignal.txt").read()
#data = data.decode('utf-8')
rams = getNgrams(data, 4)
sortedNGrams = sorted(rams.items(), key = operator.itemgetter(1), reverse=True) #=True An interjection

#print(sortedNGrams)
#file = open('/Users/yuhanliu/Downloads/ngram-result.txt', 'w') # write file
#file.write(str(sortedNGrams));  
#file.close() 

#open file，add a

createListCSV('/Users/yuhanliu/Downloads/under2-4-gramtest.csv', sortedNGrams)
#out = open('/Users/yuhanliu/Downloads/ngramtest.csv','a', newline='')

#csv_write = csv.writer(out,dialect='excel')
#write contents
#sv_write.writerow(str(sortedNGrams))

print ("write over")

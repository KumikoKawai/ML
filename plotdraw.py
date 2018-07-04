from numpy import array
from numpy.random import normal
import matplotlib.pyplot as plt
import re
lenths=[]
datas=[]
prequen=[]
gram=[]
indexcsv=[]
frequency=[]
def get_data():
    n=0
    readfile=open("/Users/yuhanliu/Downloads/test0118/ngram/0118dont2-4-gramtestnew.csv")
    lines=readfile.readlines()
    for line in lines:
 #       line=line.strip()
        lenths.append(line)
        n+=1
    #print (n)
   # lenths1 = np.array(lenths)  # 将list数组转化成array数组便于查看数据结构
 #   lenths_header = np.array(birth_header)
    
 #   print(birth_header.shape)
    return(n)
lens=get_data()
for num in range(0,lens):
    datas=str(lenths).split(',')
    prequen.append(datas[2*num+1])
    gram.append(datas[2*num])
    indexcsv.append(num)
for n in range(0,lens):
    s=re.sub("\D", "", prequen[n])
    prequen[n]=int(s);
    m=re.sub('[^a-zA-Z]','',gram[n])
    gram[n]=m;
    
for i in range(0,lens):
    f=prequen[i]/sum(prequen);
    frequency.append(f)
 
 
 
#print(sum(prequen))
#print (lens)
#print(lenths)  # 利用.shape查看结构。
#print(prequen)
#print(gram)
#print(indexcsv)
#print(frequency)
      
      
#name_list = ['lambda=0', 'lambda=0.05', 'lambda=0.1', 'lambda=0.5']
name_list=gram
#num_list = [52.4, 57.8, 59.1, 54.6]
num_list=frequency
rects=plt.bar(range(len(num_list)), num_list, color='rgby')
# X轴标题
#index=[0,1,2,3]
index=indexcsv
index=[float(c) for c in index]
plt.ylim(ymax=1, ymin=0)
plt.xticks(index, name_list)
plt.ylabel("Frequency(%)") #X轴标签
for rect in rects:
    height = rect.get_height()
 #   plt.text(rect.get_x() + rect.get_width() / 2, height, str(height)+'%', ha='center', va='bottom')
    plt.text(rect.get_x() + rect.get_width() / 2, height, float(height), ha='center', va='bottom')
plt.show()

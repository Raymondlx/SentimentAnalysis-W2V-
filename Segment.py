__author__ = 'raymond'
# coding:utf-8
'''
import re #去除字符串中的所有标点信息
def eniminate():

temp = "想做/ 兼_职/学生_/ 的 、加,我Q：  1 5.  8 0. ！！？？  8 6 。0.  2。 3     有,惊,喜,哦"
temp = temp.decode("utf8")
string = re.sub("[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）：]+".decode("utf8"), "".decode("utf8"),temp)
print string
'''

''' 去除文档中的标点，并将文档分句
import re
M  = 30

def  splitSentence(FilePath = './test1.txt'):
    f = open(FilePath, 'r')
    f1 = open('temp_split.txt', 'w')
    results=[]
    for line in f.readlines():
       # line = line.strip().decode('utf-8', 'ignore')       #去除每行首尾可能出现的空格，并转为Unicode进行处理
        r=line.strip()#[11:]#.split('。')r
        #temp = re.split('。|\?|？|[...]|“”|~|!|！|；|;|：|：|→|\n|[0-9]+|-|:|()|（）|', str(r))
        temp = re.split('。|\?|？|[...]|“”|~|!|！|；|;|：|：|→|\n|()|（）|', str(r)) #去除除了，之后的句子,并换行
        sentences=[]
        for element in temp:
            if element:
                f1.write(element.strip())
                f1.write('\n')
                sentences.append(element)
        results.append(sentences)

    f.close()
    f1.close()
    return 'temp_split.txt'

def main():
    results=splitSentence()
    print results

if __name__ == "__main__":
    main()
'''

'''读取小文本的结巴分词
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import jieba
import jieba.posseg as pseg
import time
def Segment():

   t1=time.time()
   f=open("./wiki.zh.text.jian","r") #读取文本
   string=f.read().decode("utf-8")
   words = pseg.cut(string) #进行分词
   result=""  #记录最终结果的变量
   for w in words:
      result+= str(w.word)+"\t"#"/"+str(w.flag) #加词性标注
      print result
   f = open("./wiki.zh.text.jian.seg", "w")  # 将结果保存到另一个文档中
   f.write(result.encode("utf-8"))
   f.close()
   t2=time.time()
   print("分词及词性标注完成，耗时："+str(t2-t1)+"秒。") #反馈结果

def main():
    results= Segment()
    print results

if __name__ == '__main__':
    main()
'''
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import jieba
import jieba.posseg as pseg
import time
def Segment():

   t1=time.time()
   result = ""  # 记录最终结果的变量
   f = open("./wiki.zh.text.jian.seg", "a")  # 将结果保存到另一个文档中
   for line in open('./wiki.zh.text.jian'): #通过逐行读取文件，解决时间效率问题
      string = line.decode("utf-8")
      words = pseg.cut(line)

      for w in  words:
         result += str(w.word) + "\t"  # "/"+str(w.flag) #加词性标注
         f.write(result.encode("utf-8"))
         print result
         result = ""    #读完一行后清空buffer

   f.close()
   t2=time.time()
   print("分词及词性标注完成，耗时："+str(t2-t1)+"秒。") #反馈结果

def main():
    results= Segment()
    print results

if __name__ == '__main__':
    main()
#分词及词性标注完成，耗时：45056.4293699秒。文件大小1G
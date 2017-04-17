__author__ = 'raymond'
# coding:utf-8
import time
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def Split(): #统计词数
    t1 = time.time()
    count1 = 0
    count2 = 0
    count3 = 0

    for line in open('./SVM/negative.utf8'):
        count1+= str(line[0]).count('1' and '2')
    print count1

    for line in open('./SVM/positive.utf8'):  # 通过逐行读取文件，解决时间效率问题
        count2 += str(line[0]).count('4' and '5')
    print count2


    for line in open('./SVM/cut_word_all.txt'):  # 通过逐行读取文件，解决时间效率问题
        count3 += str(line[0]).count('1'and '2'and '3'and'4'and'5')
    print count3

def SplitforTrain(): #分割文本作为训练集
    f = open('./SVM/negative')
    f1 = open('./SVM/negative_train_10000','a')
    f2 = open('./SVM/positive')
    f3 = open('./SVM/positive_train_10000','a')

    count = 0
    count2 = 0
    count3 = 0
    while True:

            eachline = f.readline()
            string = eachline.decode('utf-8')
            count2+= str(eachline).count('1',0,1)
            count3+= str(eachline).count('2',0,1)
            count = count2 + count3
            f1.write(string.encode('utf-8'))
            if count == 10000:
                break
            if not eachline :break

    f.close()

    count1 = 0
    count4 = 0
    count5 = 0
    while True:

        eachline = f2.readline()
        string = eachline.decode('utf-8')
        count4 += str(eachline).count('4', 0, 1)
        count5 += str(eachline).count('5', 0, 1)
        count1 = count4 + count5
        f3.write(string.encode('utf-8'))
        if count1 == 10000:
            break
        if not eachline: break

    print count
    print count1
    f2.close()

def SplitforTest():
    f = open('./SVM/negative')
    f1 = open('./SVM/negative_test_5000', 'a')
    f2 = open('./SVM/positive')
    f3 = open('./SVM/positive_test_5000','a')

    count = 0
    while True:

        eachline = f.readline()
        string = eachline.decode('utf-8')
        count += str(eachline).count('1' and '2', 0, 1)
        if count > 20000 and count <=25000:
            f1.write(string.encode('utf-8'))
        if not eachline: break

    f.close()
    count1 = 0
    while True:

        eachline = f2.readline()
        string = eachline.decode('utf-8')
        count1 += str(eachline).count('4' and '5', 0, 1)
        if count1 > 20000 and count1 <=25000:
            f3.write(string.encode('utf-8'))
        if not eachline: break
    f2.close()

def Replace():
    f1 = open('./SVM/negative','a')
    for line in open('./SVM/negative.utf8'):
        a =str(line).replace('\\', '\t') # 替换掉其中的\便于word2vec工作
        string = a.decode('utf-8')
        f1.write(string.encode('utf-8'))

    f2 = open('./SVM/positive', 'a')
    for line in open('./SVM/positive.utf8'):
        a = str(line).replace('\\', '\t')  # 替换掉其中的\便于word2vec工作
        string = a.decode('utf-8')
        f2.write(string.encode('utf-8'))
    f1.close()
    f2.close()
def main ():
     split= SplitforTrain()
   #  split2= SplitforTest()
   # result = Split()
   # replace = Replace()
if __name__ == '__main__':
    main()
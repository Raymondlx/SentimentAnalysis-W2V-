# coding: utf-8

from sklearn.cross_validation import train_test_split
from gensim.models.word2vec import Word2Vec
from sklearn.preprocessing import scale
from sklearn import metrics
from sklearn.linear_model import SGDClassifier
import numpy as np

def loadinfor():
    # load from local
    with open('./Test1','r') as infile:
        test1 = infile.readlines()

    with open('./Test2','r') as infile:
        test2 = infile.readlines()

    return test1, test2

def numpyProcess(pos,neg):

    number_pos = 5
    number_neg = 5
    # use 1 and 0 to build the array
    y = np.concatenate((np.ones(number_pos),np.zeros(number_neg)))
    # use tran_split to randomly select Train and Test
    x_train, x_test, y_train, y_test = train_test_split(np.concatenate((pos, neg)), y, test_size=0.5)
    return x_train, x_test, y_train, y_test

def cleanText(corpus):

    corpus = [z.lower().replace('\n','').split() for z in corpus]
    return corpus

def builVocab(dim,x_train):

    w2v = Word2Vec(size=dim, min_count=1)# test
    w2v.build_vocab(x_train)
    return w2v

def buildWordVector(w2v,text,size):
    # get the average value of each word
    vec = np.zeros(size).reshape((1, size))
    count = 0.
    for word in text:
        try:
            vec += w2v[word].reshape((1, size))
            count += 1.
        except KeyError:
            continue
    if count != 0:
        vec /= count
    return vec

def scaleVec(w2v,trainSet,dim):
    train_vecs = np.concatenate([buildWordVector(w2v,z, dim) for z in trainSet])
    train_vecs = scale(train_vecs)
    return train_vecs

def calculate_result(actual,pred):
    m_precision = metrics.precision_score(actual,pred)
    m_recall = metrics.recall_score(actual,pred)
    print 'Predict info:'
    print 'Precision:{0:.3f}'.format(m_precision)
    print 'Recall:{0:0.3f}'.format(m_recall)
    print 'F1-score:{0:.3f}'.format(metrics.f1_score(actual,pred))

def sgdClassifier(train_vecs,test_vecs,y_test):
    lr = SGDClassifier(loss='log', penalty='l1')
    lr.fit(train_vecs, y_train)
    pred = lr.predict(test_vecs)

    calculate_result(y_test,pred)


if __name__ == "__main__":
    # load file and clean it
    t1, t2 = loadinfor()
    x_train, x_test, y_train, y_test = numpyProcess(t1,t2)
    x_train = cleanText(x_train)
    x_test = cleanText(x_test)
    # build vocab
    vocab = builVocab(300,x_train)
    # training data
    vocab.train(x_train)
    vocab.train(x_test)
    # scale data
    train_vec = scaleVec(vocab,x_train,300)
    test_vec = scaleVec(vocab,x_test,300)
    # add on machine-learning algorithm
    sgdClassifier(test_vec,test_vec,y_test)

    print vocab
    print x_train
    print y_train
# -*- coding: utf-8 -*-
import json
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def ReadJson():

    path = ("./dangjian.json")

    file = open(path, 'r')
    with open("./dangjian.txt","w") as inputFile:
        for line in file.readlines():
            dic = json.loads(line)
            inputFile.write(dic["Content"]+"\n")


if __name__ == "__main__":
    ReadJson()

#coding=utf-8
import re
class Count():
    def __init__(self,path):
        self.padding = dict()
        with open(path,encoding='utf-8') as f:
            data = f.read()
            words = [s for s in re.findall('\w',data)]
            for word in words:
                self.padding[word]=self.padding.get(word,0)+1
    def count1(self,n):
        assert n > 0,'n is langer than 0'
        return sorted(self.padding.items(),key=lambda item: item[1],reverse=True)
if __name__=='__main__':
    con =Count('relax.txt').count1(26)
    for item in con:
        with open('conn','a') as r:
            r.write(str(item)+'\n')



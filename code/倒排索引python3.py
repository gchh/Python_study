from __future__ import print_function
class reverseindex:
    def __init__(self,wordfilename):
        self._filename=wordfilename
    def buildindex(self):
        wordfile=open(self._filename,'r')
        self._worddict={}
        for lineno,line in enumerate(wordfile):
            for word in line.split():
                self._worddict.setdefault(word,set()).add(lineno+1)
    def printindex(self):
        for word in sorted(self._worddict):
            print(word+": ",end="")
            print(', '.join(str(lineno) for lineno in sorted(self._worddict[word])))
    def execquery(self,query):
        if query.startswith("AND:"):
            self.andquery(query[4:])
        elif query.startswith("OR:"):
            self.orquery(query[3:])
        else:
            self.andquery(query)
    def andquery(self,query):
        first=True
        result=set()
        for word in query.split():
            tmp=self._worddict.get(word,set())
            if first:
                result=tmp
                first=False
            else:
                result=result&tmp
        if result:
            print(', '.join(str(lineno) for lineno in sorted(result)))
        else:
            print("None")
    def orquery(self,query):
        result=set()
        for word in query.split():
            tmp=self._worddict.get(word,set())
            result=result|tmp
            if result:
                print(', '.join(str(lineno) for lineno in sorted(result)))
            else:
                print("None") 

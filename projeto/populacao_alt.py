class populacao():
    
    def __init__(self):
        self._start=0
        self._list={}
        
    def add(self,ind):
        self._list.update({ind.getnif(): ind})
        
    def substitui(self,new,old):
        self._list.update({old.getnif(): new})
        
    def getindvlist(self):
        return list(self._list.values())
    
    def getmaxnif(self):
        return max(list(self._list.keys()))
    
    def getniflist(self):
        return list(self._list.keys())
    
    def mata(self,ind):
        del self._list[ind.getnif()]
        
    def vivoQ(self,nif):
        return nif in self._list.keys()
    
    def vazioQ(self):
        return self._list == {}
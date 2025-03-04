class populacao:
    def __init__(self):
        self._start=0
        self._indvlist=[]

    def getindvlist(self):
        return self._indvlist
    

    def getmaxnif(self):
        return self.getniflist()[-1]

    def getniflist(self):
        return [x.getnif() for x in self._indvlist]
    
    def add(self,indv):
        x = self.procura(indv)        
        self._indvlist.insert(x, indv)
        
    def mata(self,indv):
        index = self.procura(indv)
        
        if index == 0:
            self._indvlist = self._indvlist[1:]
            
        elif index==len(self._indvlist):
            self._indvlist = self._indvlist[:-1]            
        else:
            a = self._indvlist[:index] 
            b = self._indvlist[index+1:]
            self._indvlist = a + b
            
        return self._indvlist
    
    def substitui(self,new,old):
        self.mata(old)
        self.add(new)
    
    def procura(self,indv):
        #localiza um individuo na população usando pesquisa binária
        #devolve o maior indice com nif menor ou igual ao do pretendido
        nif = indv.getnif()
        left = 0
        right = len(self._indvlist)
        
        while right > left:
            meio = (left+right)//2
            
            if nif > self._indvlist[meio].getnif():
                left = meio + 1
            else:
                right = meio
        
        return left

    def vivoQ(self,nif):
        return nif in self.getniflist()

    def vazioQ(self):
        return self._indvlist==[]
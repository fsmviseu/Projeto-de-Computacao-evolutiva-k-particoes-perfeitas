from random import randint

class particao:
    
    def __init__(self):
        self._start=0
        self._list = []

    def generate(self, k, w):
        n = len(w)
        self._list = []
        for i in range(n):
            self._list.append(randint(1,k))
        return self

    def troca(self,i,b):
        #troca o elemento na posição i para o bloco b
        self._list[i]=b
        
    def elem_ordem(self,x):
        return self._list[x]
   
    def soma_blocos(self,w,k):
        lista_somas = [0]*k
        
        for i in range(len(w)):
            lista_somas[self._list[i]-1]+=w[i]
        return lista_somas
    
    def coef(self,w,k):        
        coef = 0
        perf = sum(w)//k
        
        for bloco in range(k):
            soma = self.soma_blocos(w,k)[bloco]            
            if soma > perf:
                coef += (soma-perf)/k
            else:
                coef += -(soma-perf)/k                
        return coef

    
    def view(self,w,k):
        bloco=[[] for i in range(k)]
        for j in range(len(w)):
            bloco[self._list[j]-1]+=[w[j]]
            
        return bloco
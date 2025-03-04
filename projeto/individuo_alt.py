class indv:
    
    def __init__(self, k, w, part, tempo, listamagica,nif):
        self._start=0
        self._dados = {
            "nif": nif,
            "particao":part,
            "listamagica":listamagica,
            }
        l = self.update_listamagica(w, k, tempo)
        self._dados.update({"listamagica": l})

    def getnif(self):
        return self._dados.get("nif")
    
    def getparticao(self):
        return self._dados.get("particao")
       
    def create_listamagica(self,w,k, tempo):
        bloco=[]
        for i in range(1,k +1):
            temp = []
            
            for j in range(len(w)):
                if self.getparticao().elem_ordem(j)==i:
                    temp += [w[j]]
            bloco += [temp]
        listamagica = []
        s = sum(w)//k
        for x in bloco:
            soma=0
            for i in range(len(x)):
                soma+=x[i]
            if soma==s:
                listamagica += [tempo]
            else:
                listamagica += [-1]
        return listamagica
  

    def update_listamagica(self, w, k, tempo):
        if self._dados.get("listamagica")==[]:
            return self.create_listamagica(w, k, tempo)
        else:
            bloco=[0]*k
            for j in range(len(w)):
                bloco[self._dados.get("particao").elem_ordem(j)-1]+=w[j]     
            s = sum(w)//k
            mag = self._dados.get("listamagica")
            return [tempo if (bloco[x]==s and mag[x]==-1) else mag[x] for x in range(k)]
        

    def getlista_magica(self):
        return self._dados.get("listamagica")
    
    

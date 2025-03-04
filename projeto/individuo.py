class indv:
    
    def __init__(self, k, w, part, tempo, listamagica,nif):
        self._start=0
        self._particao = part
        self._nif = nif
        self._listamagica = listamagica
        self._listamagica = self.update_listamagica(w, k, tempo)
        
    
    def getnif(self):
        return self._nif
    
    def getparticao(self):
        return self._particao

    def __str__(self):
        return "%s" % self._particao
    
    def create_listamagica(self,w,k, tempo):
        listamagica = []
        perf = sum(w)//k
        lista_somas = self._particao.soma_blocos(w, k)
        for x in lista_somas:
            if x == perf:
                listamagica.append(tempo)
            else:
                listamagica.append(-1)      
        return listamagica
  
    def update_listamagica(self, w, k, tempo):
        if self._listamagica == []:
            return self.create_listamagica(w, k, tempo)
        else:
            lista_somas = self._particao.soma_blocos(w, k)
            perf = sum(w)//k
            return [tempo if (lista_somas[x] == perf and self._listamagica[x] == -1) else self._listamagica[x] for x in range(k)]

    def getlista_magica(self):
        return self._listamagica
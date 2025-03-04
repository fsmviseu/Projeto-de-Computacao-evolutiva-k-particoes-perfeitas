class evento():
    def __init__(self,tipo,alvo,time):
        self._start = 0
        self._dados = (tipo, alvo, time)
        
        
    def gettime(self):
        return self._dados[2]
    
    def getalvo(self):
        return self._dados[1]
        
    def gettipo(self):
        return self._dados[0]
        

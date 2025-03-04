class evento:
    def __init__(self,tipo,alvo,time):
        self._start=0
        self._alvo=alvo
        self._tipo=tipo
        self._time=time
        
    def gettime(self):
        return self._time
    
    def getalvo(self):
        return self._alvo
    
    def gettipo(self):
        return self._tipo
   

from random import random, randint
from math import log, inf
import time


from funcoes import mutacao, reproducao
from partition import particao
#from individuo import indv
from individuo_alt import indv
#from evento import evento
from evento_alt import evento
#from populacao import populacao
from populacao_alt import populacao
#from cap import cap
from cap_alt import cap

def exprandom(c):
    return -c*log(random())


def simulador(NInd, TFim, TMut, TRep, TMor, w, k):
    
    #inicialização do simulador
    start = time.time()
    agenda = cap()
    population = populacao()
    agora = 0
    ganhamos = False

    #adicionar individuos à população e respetiva mutação à agenda
    i = 1
    while i<NInd+1 and not ganhamos:  
        new_part = particao()
        individuo = (indv(k, w, new_part.generate(k,w), agora, [], i))
        population.add(individuo)
        agenda.adicionar(evento("mut", individuo, exprandom(TMut)))
        
        if individuo.getparticao().coef(w,k) == 0:
            sol = [individuo.getparticao()]
            ganhamos = True
        i+=1
        
    #agendar a primeira reprodução e a primeira morte
    agenda.adicionar(evento("rep",[],exprandom(TRep)))
    agenda.adicionar(evento("mor",[], exprandom(TMor)))  
  
    evento_atual = agenda.proximo()
    agora = evento_atual.gettime()

    #simulação
    while agora<TFim and not ganhamos:
        
        tipo = evento_atual.gettipo()
       
        if tipo == "mut" and sum(w)%k==0:
            
            ind = evento_atual.getalvo()
            
            #teste para ver se o indivíduo está vivo
            if population.vivoQ(ind.getnif()):
                
                particao_indv = ind.getparticao()
                magica = ind.getlista_magica()
                
                #realizar a mutação
                new_part = mutacao(w,k,particao_indv)
                
                #atualizar a população e agendar a próxima mutação do individuo
                new = indv(k, w, new_part, agora, magica, ind.getnif())
                population.substitui(new,ind)
                agenda.adicionar(evento("mut", new, agora + exprandom(TMut)))
            
                #verificar se o novo indivíduo representa uma k-partição perfeita
                if new.getparticao().coef(w, k)==0:
                    sol = [new.getparticao()]
                    ganhamos = True
            
        elif tipo == "rep" and sum(w)%k==0 and len(population.getindvlist())>1:

            lista_ind = population.getindvlist()            
            mae = lista_ind[randint(0, len(lista_ind)-1)]
            pai = lista_ind[randint(0, len(lista_ind)-1)]

            #garantir que a mãe e o pai são indivíduos diferentes
            while mae.getnif() == pai.getnif():
               mae = lista_ind[randint(0, len(lista_ind)-1)]
               pai = lista_ind[randint(0, len(lista_ind)-1)]

            #realizar a reprodução
            (success,filho,heranca) = reproducao(mae,pai,w,k)
            
            #se a reprodução for bem sucedida, adicionar o novo indivíduo à população e agendar a sua mutação
            if success:
                result = indv(k, w, filho, agora, heranca, population.getmaxnif()+1)
                population.add(result)
                agenda.adicionar(evento("mut", result, agora + exprandom(TMut)))
                            
                #verificar se o indivíduo gerado é perfeito
                if filho.coef(w, k)==0:
                    sol = [result.getparticao()]
                    ganhamos = True
                    
            #agendar a próxuima população
            agenda.adicionar(evento("rep", [], agora + exprandom(TRep)))
            
        else: #(tipo == "mor")
            for individuo in population.getindvlist():
                lista_magica = individuo.getlista_magica()
                maximo = -inf
                minimo = inf
                for x in lista_magica:
                    if x!=-1:
                      if x > maximo:
                        maximo=x
                      if x < minimo:
                        minimo=x
                if maximo > -inf:     
                    idade_recente = agora - maximo
                    formacao_antigo = minimo
                    if idade_recente > 2*formacao_antigo:
                        population.mata(individuo) 


            #se a população ficar vazia no final, repopular
            if population.vazioQ(): 
                for i in range(1,NInd+1):
                    individuo = indv(k, w, particao().generate(k,w), agora, [], i)
                    population.add(individuo)
                    agenda.adicionar(evento("mut", individuo, agora+exprandom(TMut)))

                    if individuo.getparticao().coef(w,k) == 0:
                        sol = [individuo.getparticao()]
                        ganhamos = True

                agenda.adicionar(evento("rep",[],agora + exprandom(TRep)))
            agenda.adicionar(evento("mor",population, agora + exprandom(TMor)))
        
        agenda.apaga()
        evento_atual = agenda.proximo()
        agora = evento_atual.gettime()

    #caso não tenha sido obtida uma solução exata, obter a(s) aproximada(s)
    if ganhamos == False:
        coefs = [ind.getparticao().coef(w,k) for ind in population.getindvlist()]
        minimo = min(coefs)
        sol=[]
        for ind in population.getindvlist():
            if ind.getparticao().coef(w,k)== minimo:
                sol += [ind.getparticao()]
                
    end = time.time()

    #print(f"tempo de execução: {end-start} segundos")
    
    if len(sol)==1:
        return sol[0].view(w,k)
    
    return [x.view(w,k) for x in sol]
            

if __name__ == "__main__":
    w = [14175, 15055, 16616, 17495, 18072, 19390, 19731, 22161, 23320, 23717, 26343, 28725, 29127, 32257, 40020, 41867, 43155, 46298, 56734, 57176, 58306, 61848, 65825, 66042, 68634, 69189, 72936, 74287, 74537, 81942, 82027, 82623, 82802, 82988, 90467, 97042, 97507, 99564]
    k=2        
    #print(simulador(10,1000,5,5,5,w,k))


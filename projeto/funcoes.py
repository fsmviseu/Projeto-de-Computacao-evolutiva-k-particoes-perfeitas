from random import randint
from copy import deepcopy

def mutacao(w,k,part): 

    soma_e_pos = [[0] for i in range(k)]
    
    for j in range(len(w)):
        soma_e_pos[part.elem_ordem(j)-1][0] += w[j]
        soma_e_pos[part.elem_ordem(j)-1] += [j]

    perf = sum(w)//k

    lista_sup = []
    lista_inf = []

    for x in range(k):
        if soma_e_pos[x][0] > perf:
            lista_sup.append(x)
        elif soma_e_pos[x][0] < perf:
            lista_inf.append(x)

    nb_maior = lista_sup[randint(0,len(lista_sup)-1)]
    nb_menor = lista_inf[randint(0,len(lista_inf)-1)]

    bloco_menor = soma_e_pos[nb_menor]
    x = soma_e_pos[nb_maior][randint(1,len(soma_e_pos[nb_maior])-1)]

    targetsum = w[x] - (soma_e_pos[nb_maior][0] - bloco_menor.pop(0))/2

    soma = 0

    while soma < targetsum and bloco_menor != []:
        proximo = bloco_menor.pop(randint(0, len(bloco_menor) - 1))
        soma += w[proximo]
        part.troca(proximo, nb_maior + 1)
    part.troca(x, nb_menor + 1)

    return part

def reproducao(mae, pai, w, k):
        
    particao_mae = mae.getparticao()
    particao_pai = pai.getparticao()
    
    magica_mae = mae.getlista_magica()
    magica_pai = pai.getlista_magica()
    
    #caso a partição associada ao pai não possua nenhum bloco perfeito, a reprodução não produz efeito; caso contrário, seleciona-se aleatória e uniformemente, um dos blocos perfeitos do pai
    if any(map(lambda x: x != -1, magica_pai)):
    
        filho = deepcopy(particao_mae)
        
        #a herança irá assegurar que os instantes de formação dos blocos perfeitos dos progenitores são herdados pelo filho
        heranca = deepcopy(magica_mae)
    
        resto = []
    
        for i in range(len(w)):
            if magica_mae[particao_mae.elem_ordem(i) - 1] == -1:
                resto.append([w[i], i])
            
        blocos_perf_pai = []
        blocos_por_usar = []
        
        for x in range(1, k+1):
            if magica_pai[x-1] != -1:
                blocos_perf_pai.append(x)
                
            if magica_mae[x-1] == -1:
                blocos_por_usar.append(x)
            
        perf_pai = blocos_perf_pai[randint(0,len(blocos_perf_pai)-1)]
        bloco_pai = [w[i] for i in range(len(w)) if particao_pai.elem_ordem(i) == perf_pai]
        
        bloco_to_fill = blocos_por_usar.pop()

        possivel = True
        i = 0
        
        #caso o bloco perfeito selecionado do pai não possa ser reconstruído com os elementos dos blocos imperfeitos da mãe, a reprodução não produz efeito; caso contrário a reprodução dá origem a um filho
        while possivel and i<len(bloco_pai):
            j = 0
            while j < len(resto) and resto[j][0] != bloco_pai[i]:
                j += 1
                
            if j == len(resto):
                possivel = False
            else:
                filho.troca(resto[j][1], bloco_to_fill)
                resto = resto[:j] + resto[j+1:]
                i += 1
                
        if possivel:
            heranca[bloco_to_fill - 1] = magica_pai[perf_pai - 1]
            for s in range(len(resto)):
                filho.troca(resto[s][1], blocos_por_usar[randint(0, len(blocos_por_usar)-1)]) 
            return (True, filho, heranca)

    return (False, False, False)
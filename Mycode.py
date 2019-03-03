###################################################################################################################
###########################################################Welcome#############################################
#######################################################@author: RAUCHDI MEHDI************##############################
###########################################*************PROJET D'atterissage**************########################
###################################################################################################################

from random import randint
import random
import numpy as np
from ipywidgets.widgets.widget_selectioncontainer import Tab
 


#Tableau fenêtres d’atterrissage
pen=[[1,2,3,4,5,6,7,8,9,10],[129,195, 89, 96, 110 ,120 ,124 ,126 ,135 ,160],[155,258,98,106,123,135,138,140,150,180],[559,744, 510, 521, 555, 576, 577, 573, 591, 657],[10,10,30,30,30,30,30,30,30,30],[10,10,30,30,30,30,30,30,30,30]]
#intervalles de sécurité
ss=[[0,3,15,15,15,15,15,15,15,15],[3,0,15,15,15,15,15,15,15,15],[15,15,0,8,8,8,8,8,8,8],[15,15,8,0,8,8,8,8,8,8],[15,15,8,8,0,8,8,8,8,8],[15,15,8,8,8,0,8,8,8,8],[15,15,8,8,8,8,0,8,8,8],[15,15,8,8,8,8,8,0,8,8],[15,15,8,8,8,8,8,8,0,8],[15,15,8,8,8,8,8,8,8,0]]

pop=[]
def indivis():
 
    while True:
        flag=1
        
    
        while(flag!=0):
            #Remplissage de notre tableau
            T=[]
            for i in range(10):
                T.append(randint(pen[1][i],pen[3][i]))
            #valider si notre individu respect les intervalles de sécurité    
            for j in range(len(T)-1):
                for k in range(1,j+1):
                    if (abs(T[j]-T[k-1])<ss[j][k-1]):
                        flag=0
                        
            if(flag==1):pop.append(T)
        #la taille de notre pop est 10
        if(len(pop)>=10):
            break

        
#Evaluation de chaque individu
def evalu(ind):
    penali=[]
    for j in range(len(ind)):
        penali.append(abs(ind[j]-pen[2][j])*pen[4][j])
    SumPenali=sum(penali)
    #print("Tab d penalité :",penali)
    #print("Sum Penalité:",SumPenali)
    return SumPenali

#afficher l'individus avec la penalité minime avec son indice
def best(ind):
    best=evalu(ind[0])
    indice=0
    for i in range(1,len(ind)):
        may=evalu(ind[i])
        if best>may:
            best=may
            indice=i
    #print("Le meilleur de la population est: ",best," ;Son indice est :", indice)
    T=[best,indice]
    return T
#Selectionner aleatoirement un individu de la pop 
def Select():
    flag=randint(0,9)
    #print("individu selectionner aleatoirement est: ",pop[flag]," ;Son indice",flag)
    T=[pop[flag],flag]
    return T

#tableau des indices des individus à croiser
def TabC():
    C=[] #Tableau des individus à croiser
    pc=0.7
    for i in range(10):
        if random.random()<pc:
            C.append(i)
    #print("Tableau des individus à croiser est :",C)
    return C
#Tableau de mutation
def TabM():
    M,pm=[],0.3
    for i in range(10):
        if random.random()<pm:
            M.append(i)
    #print("Tableau des individus à Muter est :",M)
    return M

#Croisement de deux individus
def croi(one,two):
    p,T1,T2,T=randint(1,9),[],[],[]
    #print("pos de croi",p)
    for i in range(10):
        if i<=p:
            T1.append(one[i])
            T2.append(two[i])
        else:
            T1.append(two[i])
            T2.append(one[i])
    T.append(T1);T.append(T2)    
    return T

#verifie Croisement : Securtiy seulement
def VerifieC(ind):
        flag=1 #True        
        #valider si notre individu respect les intervalles de sécurité    
        for j in range(len(ind)-1):
            for k in range(1,j+1):
                if (abs(ind[j]-ind[k-1])<ss[j][k-1]):
                    flag=0 #false
                    
        return flag
    

#verifie mutation
def VerifieM(ind):

        flag=1 #True        
        #Verifier si notre individu verifie l'intervalle
        for i in range(10):
                if ind[i]<pen[1][i] and ind[i]>pen[3][i]:
                    flag=0
                    break
        #valider si notre individu respect les intervalles de sécurité    
        for j in range(len(ind)-1):
            for k in range(1,j+1):
                #print("here")
                if (abs(ind[j]-ind[k-1])<ss[j][k-1]):
                    flag=0 #false
                    
        #print("resultat",flag)
        return flag

#Mutation de deux genes d'un individu
def mut(T,ind):
    #T=[]
    indd=np.copy(ind) #faire une copie de notre individu
    a,b=randint(1,9),randint(1,9)
    #Eliminer le fait que les position de mutation soit egaux
    while(a==b):
        a,b=randint(1,9),randint(1,9)  
    #Permuter dans le teste
    indd[a],indd[b]=indd[b],indd[a]
    #print("position de mutation",a,b)
    #print("before \n",indd)
    #print("after \n",ind)
    if VerifieM(indd)==1: #flage ==1 => Realisable
        #si c'est bien on change dans notre pop
        ind[a],ind[b]=ind[b],ind[a]
    
    return T

def afficher(pop):
    print("Votre pop est :")
    for i in range(len(pop)):
        print(pop[i])   



def replace():
    #on choisis un nombre aleatoire
    alea=randint(0,1)
    #on ne remplace pas
    if alea==0:
        re=0
    #on remplace
    else:
        re=1
    return re

def QestionCroisement():
    TableauC=TabC()
    #tableau qui contient la liste des individus à croiser
    tailleC=len(TableauC)
    #Vu que nous voulons 6 croisement la taille de notre tableau doit etre egale à 7 (0-1/1-2/2-3/3-4/4-5/5-6)
    while tailleC<7:
        TableauC=TabC()
        tailleC=len(TableauC)
    #on va tester si notre tableau est paire ou impaire pour eviter de depasser la taille du tableau au cas impaire
    if (tailleC %2==0) :    
        for i in range(tailleC):
            #0-1/1-2/2-3/3-4/4-5/5-6
            if i<=4:    
                HEC=croi(pop[TableauC[i]],pop[TableauC[i+1]])
                if VerifieC(HEC[0])==1 and replace()==1:
                    #je change le pere par le fils
                    pop[TableauC[i]]=HEC[0]
                if VerifieC(HEC[1])==1 and replace()==1:
                    #je change le pere par le fils
                    pop[TableauC[i+1]]=HEC[1]

    else:
        if tailleC>=2:
            for i in range(tailleC-1):
                if(i<=4):
                    HEC=croi(pop[TableauC[i]],pop[TableauC[i+1]])
                    if VerifieC(HEC[0])==1 and replace()==1:
                        #je change le pere par le fils
                        pop[TableauC[i]]=HEC[0]
                    if VerifieC(HEC[1])==1 and replace()==1:
                        #je change le pere par le fils
                        pop[TableauC[i+1]]=HEC[1]

def QuestionMutation():
    myTab=TabM()
    #print("Tableau des individus à muter",myTab)
    
    #On va muter que 2 parmis les 8
    mutnumber=2
    for i in range(len(myTab)):
        if i<mutnumber:
            mut(pop,pop[myTab[i]])
    

if __name__ == '__main__':
    indivis()
    afficher(pop)
    
    print("Le meilleur de la pop est :",best(pop))
    print("l'individu selectionner aleatoirement est:",Select())


    print("#########################################Trois individus choisit aleatoirement#############################################################")

    
    r=[]
    for i in range(3):
        r.append(Select()[0])
    print("Notre nouveau tableau de 3",r)
    print("Evaluation des 3 indiv",evalu(r[0])," ;",evalu(r[1])," ;",evalu(r[2]))
    print("best of R",best(r))

    #Croisement=TabC()
    #Mutation=TabM()
    #print(croi(pop[TabC()[0]],pop[TabC()[1]])
    #print(";",pop[TabC()[0]])
    print("########################################phase de Croisement#############################################################")
    
    TableauC=TabC()
    print("tableau des ind à croiser",TableauC)
    #tableau qui contient la liste des individus à croiser
    tailleC=len(TableauC)
    
    #print("taille du tabC",tailleC)
    #on va tester si notre tableau est paire ou impaire pour eviter de depasser la taille du tableau au cas impaire
    if (tailleC %2==0) :    
        for i in range(tailleC):
            #0-1/1-2/2-3/3-4/4-5/5-6
            if i<=4:    
                HEC=croi(pop[TableauC[i]],pop[TableauC[i+1]])
                if VerifieC(HEC[0])==1 and replace()==1:
                    #je change le pere par le fils
                    pop[TableauC[i]]=HEC[0]
                if VerifieC(HEC[1])==1 and replace()==1:
                    #je change le pere par le fils
                    pop[TableauC[i+1]]=HEC[1]

    else:
        if tailleC>=2:
            for i in range(tailleC-1):
                if(i<=4):
                    HEC=croi(pop[TableauC[i]],pop[TableauC[i+1]])
                    if VerifieC(HEC[0])==1 and replace()==1:
                        #je change le pere par le fils
                        pop[TableauC[i]]=HEC[0]
                    if VerifieC(HEC[1])==1 and replace()==1:
                        #je change le pere par le fils
                        pop[TableauC[i+1]]=HEC[1]
    #print("verifie croi f1",VerifieC(HEC[0]))
    #print("verifie croi f2",VerifieC(HEC[1]))
    
    
    print("########################################phase de mutation#############################################################")
    myTab=TabM()
    print("Tableau des individus à muter",myTab)
    
    #Faire une copie de notre population
    #for i in range(len(pop)):
    #    tes=np.copy(pop)
    
    #test=[]
    #test=tes
    print("\nbefore Mutation:")
    #affichage de notre tableau 
    #for i in range(len(pop)):
    #    print(pop[i])
    afficher(pop)
    #On va muter que 2 parmis les 8
    mutnumber=2
    for i in range(len(myTab)):
        if i<mutnumber:
            mut(pop,pop[myTab[i]])
    print("\nAfter mutation et verification:")
    #for i in range(len(pop)):
    #    print(pop[i])
    afficher(pop)
    #VerifieM(test[myTab[0]])

    #print("\n Mutation:\n")
    
    #for i in range(len(pop)):
    #    print(test[i])
    #print(len(pop))
    #print(type(test))

    print("########################################Question 13 & 14#############################################################")
    n=10
    Bestof=[best(pop)[0],0]
    for i in range(1,n):
        print("######## Iteration ",i," ####################")
        #Bestof=[best(pop)[0],i]
        #print("bestOf",Bestof)
        #afficher(pop)
        #croiser
        QestionCroisement()
        #muter
        QuestionMutation()
        
        bpp=best(pop)[0]
        #print(bpp)
        print("Le meilleur de la pop est :",bpp)
        if bpp<=Bestof[0]:
            Bestof[0],Bestof[1]=bpp,i
            
    print("le meilleure de toute la pop",Bestof[0],"il est trouvé à l'iteration :",Bestof[1])

    

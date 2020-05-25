import math
import itertools
import statistics
import collections

print("Enter two numbers with a space in between followed by enter")
print("The first should be the number of balls b and the second the period p")
print("This program returns all patterns of period p with b balls as well as how many there are")
print("It will proceed to check if there are repeatable subsequences to return all patterns of minimal period p")
print("It will explicitly return the ones which are not of minimal period")
print("Have fun!")
#input is list of 2 numbers with spaces
#elements are.. 1: number of balls and 2:period
onnodig=[int(x) for x in input().split()]
b=onnodig[0]
p=onnodig[1]

#make a list of beats to work with
beats=[]
i=0
while i<p:
    beats.append(i)
    i=i+1
permutaties=list(itertools.permutations(beats))

#checks if two sequences are cyclic shifts of each other
def shiftchecker(lijst1, lijst2):    
    a_list=collections.deque(lijst1)
    
    for i in range(0,len(lijst1)):
        a_list.rotate(1)
       
        if list(a_list)==lijst2:
            return True
    return False
#applies the shift chcker to a list of seuences to see if any two are the same up to cyclic shift           
def cykelvuller(lijst):
    echte_permutaties=[]
    for  j in range(0,int(len(lijst))):
        echte_permutaties.append(lijst[j])
        weg_ermee=[]
        for i in range(j+1,int(len(lijst))):
            if shiftchecker(lijst[j],lijst[i]):                
                weg_ermee.append(i)
       
        weg_ermee.reverse()        
        for k in weg_ermee:
            lijst.pop(k)
        
        if j==int(len(lijst))-1:
            break
        
    return echte_permutaties


#patronen gets filled with patterns who do not have our desired average of b yet
#jongleerbaar  will become a pattern corresponding to permutaties[i] 
def patronenvinder(periode):
    patronen=[]
    for i in range(0,len(permutaties)):
        jongleerbaar=[]
        for j in range(0,periode):
            jongleerbaar.append((permutaties[i][j]-beats[j])%periode)
        patronen.append(jongleerbaar)
    
    return cykelvuller(patronen)
    
        

#sequentie is a pattern inputted as a list
#lijstgenerator determines how much a sequentie is off from the desired average
#if non-nagtive we continue
#generates a list of all the possible lists whose sum is this afwijking

def lijstgenerator(sequentie):
    gemiddelde=statistics.mean(sequentie)
    afwijking=b-gemiddelde
    if afwijking>=0:
        getallen=[int(i) for i in range(0,afwijking+1)]
        lijst_afwijking=[]
        for x in itertools.product(getallen, repeat=p):
            if sum(x)==afwijking:
                lijst_afwijking.append(x)
        
        return (lijst_afwijking)
    
#this function does all the work calling on all the other functions
def sequencegenerator():
    jongleer_patronen=[]
    for i in range(0,len(patronenvinder(p))):
        huidige=patronenvinder(p)[i]
        goeie_sommen=lijstgenerator(huidige)
        if isinstance(goeie_sommen, list):
            for j in range(0,len(goeie_sommen)):
                patroon=[]               
                for k in range(0,p):
                    patroon.append(huidige[k]+p*goeie_sommen[j][k])
                jongleer_patronen.append(patroon)
    return (cykelvuller(jongleer_patronen))                    
    
#divisor gives all the divisors of an integer    
def divisors(x):
    divisors=[]
    for i in range(1,x+1):
        if x%i==0:
            divisors.append(i)            
    return divisors

#sequence checks wehther or not a pattern has repeatable subsequences 
def sequence(pattern):
    delers=divisors(len(pattern))
    delers.pop()
    for i in range(0,len(delers)):
        deler=delers[i]
        aantal=len(pattern)/deler
        j=0
        while j<aantal-1 and pattern[deler*j:deler*(j+1)]==pattern[deler*(j+1):deler*(j+2)]:
            j=j+1
                    
        if j==aantal-1:
            return True
        
    return False


#this is where the action starts
patroontjes=sequencegenerator()
for x in patroontjes:
    print(" ".join(str(y) for y in x))
print("the number of patterns with "+str(b)+" balls and period "+str(p)+" is")
print(len(patroontjes))

#go through elements from the back to make sure popping does not change index of elements still to examine
for i in range(len(patroontjes)-1,0,-1):
    if sequence(patroontjes[i]):
        print("This is not really period "+str(p))
        print(" ".join(str(y) for y in patroontjes.pop(i)))
        

for x in patroontjes:
    print(" ".join(str(y) for y in x))
print("the number of patterns with "+str(b)+" balls and minimal period "+str(p)+" is")
print(len(patroontjes))








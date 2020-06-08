import math
import itertools
import statistics 

print("Enter a list of numbers with spaces with an integer average")
print("This program will give you a jugglable permutation")

#input is a_0 a_1... a_{p-1} with spaces
#input should have a whole average

sequence=[int(a_i) for a_i in input().split()]

lengte=int(len(sequence))
legelijst=[0]*lengte #this will be returned as the jugglable permutation
beats=[int(i) for i in range(0,lengte)]


#every time this function is called it changes a number in the legelijst to make it match the number in lijst
#it matches index i, and uses index j to fix the average
#k is the element of the lijst which we want to assign to the ith element of legelijst
#whenever we call upon this function legelijst will be jugglable

def rechtprater(lijst, i, j, k):     
    landings=[(beats[l]+legelijst[l])%lengte for l in range(0,lengte)] #set landing times everytime with our new legelijst      
    d_i=int(k-legelijst[i])     #d_i is whatever the ith element of legelijst is missing at this point from becoming k
    legelijst[i]=k     #force the ith element to be k

    #We force the jth element to be the smallest multiple of p which is greater than d_i and substract d_i
    
    
    legelijst[j]=int(math.ceil(d_i/lengte)*lengte-d_i)+legelijst[j]
    
    #after changing these two numbers in legelijst we use the function belows to find the jugglable permutation
    permutatiezoekert(legelijst, i, j, landings, lijst)


#swaps two elements in a list on the given positions
def lijstswappert(lijst, pos_1, pos_2): 
    lijst[pos_1],lijst[pos_2]=lijst[pos_2],lijst[pos_1]
    return lijst


#this function finds the jugglable permutation of a given list where two elements, ith and jth, were changed
#it uses the landingsites from before changing the ith and jth element to find something jugglable according to the algorithm described in the proof of the lemma

#we check 4 different cases in which we can already permutate it to a juggling sequence
#if we cannot we make a legal swap of throws and try again

def permutatiezoekert(legelijst, i, j, landings, lijst):
    
    if (beats[i]+legelijst[i])%lengte==landings[i]:
        #it is jugglable as it is

        scanner_output=scanner(lijst, legelijst)     #we scan our current legelijst to our targeted sequence to see what are the first two indices which need fixing

        #we have three cases
        
        if scanner_output==[]:      #it outputs empty list if everything matches element wise
            #since it is already jugglable we can print and stop the program
            print("the juggling sequence is")
            print(" ".join(str(x) for x in legelijst))
           
            
        elif len(scanner_output[0])==1:     #if there is 1 index no right we force fix it and also print and stop the program
            legelijst[scanner_output[0][0]]=scanner_output[1]
            print("the juggling sequence is")
            print(" ".join(str(x) for x in legelijst))
            
            
        else:       #in this case there are at least two indices not correct yet so we assign these to i and j
            #we also assign the first element that is not in legelijst to k (the element which we will assign to the ith element of legelijst) 
            i=scanner_output[0][0]
            j=scanner_output[0][1]       
            k=scanner_output[1]
            
            #in this case we ask rechtprater to change the indices as needed and assigned
            rechtprater(lijst, i, j, k)
            
                   
    #same as above    
    elif (beats[i]+legelijst[i])%lengte==landings[j]:
        
        
        scanner_output=scanner(lijst, legelijst)
        
        if scanner_output==[]:
            print("the juggling sequence is")
            print(" ".join(str(x) for x in legelijst))
           
        elif len(scanner_output[0])==1:
            legelijst[scanner_output[0][0]]=scanner_output[1]
            print("the juggling sequence is")
            print(" ".join(str(x) for x in legelijst))
                 
        else:
            i=scanner_output[0][0]
            j=scanner_output[0][1]       
            k=scanner_output[1]
            
            
            rechtprater(lijst, i, j, k)
        
        
    #same except for the need to perform a swap of 2 throws to make the sequence jugglable    
    elif (beats[i]+legelijst[j])%lengte==landings[i]:
               
        lijstswappert(legelijst, i, j)        
        
        scanner_output=scanner(lijst, legelijst)
        
        if scanner_output==[]:
            print("the juggling sequence is")
            print(" ".join(str(x) for x in legelijst))
            
        elif len(scanner_output[0])==1:
            legelijst[scanner_output[0][0]]=scanner_output[1]
            print("the juggling sequence is")
            print(" ".join(str(x) for x in legelijst))
            
        else:
            i=scanner_output[0][0]
            j=scanner_output[0][1]       
            k=scanner_output[1]
            
            rechtprater(lijst, i, j, k)

       
    #same as above    
    elif (beats[i]+legelijst[j])%lengte==landings[j]:
        
        lijstswappert(legelijst, i, j)
        
        scanner_output=scanner(lijst, legelijst)
        
        if scanner_output==[]:
            print("the juggling sequence is")
            print(" ".join(str(x) for x in legelijst))
            
        elif len(scanner_output[0])==1:
            legelijst[scanner_output[0][0]]=scanner_output[1]
            print("the juggling sequence")
            print(" ".join(str(x) for x in legelijst))
            
        else:
            i=scanner_output[0][0]
            j=scanner_output[0][1]       
            k=scanner_output[1]
                        
            rechtprater(lijst, i, j, k)
         
    #apprently there is no permutation jugglable yet so we need to swap some throws    
    else:
        beat_i=(landings[i]-legelijst[i])%lengte        #we check which beat corresponds to throw and landing spot i (modulo period)
        
        lijstswappert(legelijst, beat_i, i)     #we swap the throws made at said beats which is legal due to the check above

        lijstswappert(landings, beat_i, i)      #we also swap corresponding landing sites (to have moved the entire column as analogy to the proof)

        lijstswappert(landings, i, j)           #to wrap up we now also swap landing sites of i (which now contains landing site of beat_i) and i+1 to avoid going back here in the next step
               
        permutatiezoekert(legelijst, i, j, landings, lijst)    #we hope for the best and try again
    
    



#this takes two lists, sequence and leglijst, and will look for through legelijst from left to right
#its goal is to spot the first two elements in legelijst which are not in sequence
#of these we want to save the index 

def scanner (a, b):
    targetlist=list(a)
    currentlist=list(b)
   
    lengte_target=int(len(targetlist))
    lengte_current=int(len(currentlist))

    index=[] #we will fill this with indices corresponding to elements which are in legelijst but not in sequence
        
    if lengte_target!=lengte_current:
        print('WE POOPED UP!!!')
    else:

        #we want to stop when we have found 2 indices or when we have checked every element from currentlist       
        while int(len(index))!=2 and int(len(currentlist))!=0:                   
            i=0
            #we want to stop when we have had every element from the largetlist or when we find an element in targetlist which is not equal to the first element in currentlist
            while i!=int(len(targetlist)) and currentlist[0]!=targetlist[i]:
                    i=i+1                    

            #if we have had every element from the targetlist we know that currentlist[0] is not in there
            #we save its index in currentlist
            #we take this element away from currentlist so that the next one becomes currentlist[0]
            if i==int(len(targetlist)):
                index.append(lengte_current-int(len(currentlist))) 
                currentlist.pop(0) 
                               
            #if we find a match then we don't want to save currentlist[0]'s index but we do want to take it away from currentlist
            #we also want to take away the matching element from targetlist as we don't want to use it again to check
            else:
                currentlist.pop(0)
                targetlist.pop(i)
                
                
    #we have stopped so apparently we have found 2 indices or the currentlist has length 0

    #if there are elements remaining in the targetlist the currentlist can be empty or non emtpy
    #in either scenario we can be sure that indices were added since, if this would not have happened, they would have all matched and targetlist would in fact be empty 
    #we don't know how many indices are in there but it is non empty so we return the list and check later how many we have
    if int(len(targetlist))!=0:
        return [index,targetlist[0]]

    #however if the targetlist is empty we can be sure that the currentlist is empty as well
    #that means both lists are emtpy which only happens when all elements match
    else:
        return [] 

if statistics.mean(sequence)==int(statistics.mean(sequence)):
   rechtprater(sequence, 0, 1, sequence[0]) 
else:
    print("That is not an integer average!")
    

     







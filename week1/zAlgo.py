from typing import List, Tuple
txt = "abcdabc"

def gusfieldZAlgo(pat: str) -> List[Tuple[int,int]]:

    #Zi values 
    ziValues = [0] * len(pat)
    #L & R values 
    lrValues = [(0,0)] * len(pat)

    # Base Case: 
    for i in range(len(pat)-1):

        z1 = i 
        z2 = i + 1 

        if pat[z1] != pat[z2]:
            break 
    
    ziValues[1] = i  
    if ziValues[1] != 0: 
        lrValues[1] = (1, ziValues[1])

    # Case 1 and Case 2: 
    for k in range(1, len(pat)): 
        
        l, r = lrValues[k-1]
        
        # Case 1 => completely outside the previous Z box 
        if k > r: 
            q = k  
            while q !=  len(pat) and pat[q-k] == pat[q]:
                q += 1
            
            ziValues[k] = q-k
            if ziValues[k] > 0: 
                lrValues = (k, q-1)


        elif k<= r: 
            pass 



    print(ziValues)
    print(lrValues)

gusfieldZAlgo(txt)
        




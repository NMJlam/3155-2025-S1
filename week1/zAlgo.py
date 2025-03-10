from typing import List, Tuple
txt = "aabaabcaxaabaabcy"
def gusfieldZAlgo(pat: str) -> List[Tuple[int,int]]:

    #Zi values 
    ziValues = [0] * len(pat)
    #L & R values 
    lrValues = [(0,0)] * len(pat)

    # Base Case: 
    i = 0
    while i+1 < len(pat) and pat[i] == pat[i+1]:
        i += 1
    ziValues[1] = i
    if i > 0:
        l, r = 1, i 
        lrValues[1] = (1, i)
    else: 
        l, r = 0, 0  

    # Case 1 and Case 2: 
    for k in range(2, len(pat)): 
        
        # Case 1 => completely outside the previous Z box 
        if k > r: 
            q = k  
            while q !=  len(pat) and pat[q-k] == pat[q]:
                q += 1
            
            ziValues[k] = q-k
            if ziValues[k] > 0:
                l, r = k, q-1 
                lrValues[k] = (l, r)

        elif k<= r: 
            
            zIndex = k - l  
            rhsEquality = r - k + 1

            if ziValues[zIndex] < rhsEquality: 
                ziValues[k] = ziValues[zIndex]
                lrValues[k] = (l,r)


            elif ziValues[zIndex] >= rhsEquality: 

                q = r + 1 

                while q != len(pat) and pat[q-k] == pat[q]:
                    q += 1

                l,r = k, q-1
                ziValues[k] = q - k 
                lrValues[k] = (l, r)



gusfieldZAlgo(txt)
        




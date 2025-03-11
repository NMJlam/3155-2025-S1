from typing import List, Tuple

from zAlgo3155 import gusfieldZAlgo

pat = "ana"
txt = "analogyanalogousanalanalyticalaneurysm"

def findPatternInString(pat: str, txt: str) -> List[int]:
    string = pat + "$" + txt

    ziValues, lrValues = gusfieldZAlgo(string)

    m = len(pat) 
    
    res = []

    for i, zValue in enumerate(ziValues[m+1::], start= m + 1): 

        if zValue == m: 
            res.append(i - (m+1))
    
    return res 

print(findPatternInString(pat, txt))
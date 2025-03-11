from typing import List, Tuple

txt = "zad123zaabczad123"
pat = "zad"

def naive_pattern_matching(txt: str, pat: str) -> List[int]: 
    """
    Function: slides the pattern for every single letter to find a match and outputs a list of 
    indices which the pattern fully matches

    Time Complexity: Let n be the length of the reference text and m be the length of the pattern 
    Given that for every single letter we compare a lenght of m the complixity is O(n * m)
    
    """
    txt_len = len(txt) - 1
    pat_len = len(pat) - 1

    output = []

    for i in range(txt_len - pat_len):
            
            if pat != txt[i:i + pat_len + 1]:
                continue

            output.append(i)

    return output 




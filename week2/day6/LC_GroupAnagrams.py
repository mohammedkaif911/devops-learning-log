class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {} #created a empty dict
        for w in strs:
            sorted_w = sorted(w) # making the word into sorted word
            key = "".join(sorted(w)) #making a empty key 
            if key in anagrams:
                
                anagrams[key].append(w) #adding key if the value is in the anagrams
            else:
                anagrams[key] = [w]
        return list(anagrams.values()) # returning the values in a list format
        
        
class Solution:
    def numMatchingSubseq(self, s: str, words: list[str]) -> int:
                                    
        @lru_cache(None)            
        def checkWord(word):
            start = 0 

            for ch in word:         
                start = s.find(ch, start) + 1          # <-- find gives us the index of the
                if not start: return False             #     the next occurence of ch after
                                                       #     the index "start"
            return True
        
        return sum(checkWord(w) for w in words)  
        
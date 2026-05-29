class Solution:
    def stringIndices(self, wordsContainer: list[str], wordsQuery: list[str]) -> list[int]:
        
        best_global_index = 0
        best_global_length = len(wordsContainer[0])
        
        for i, word in enumerate(wordsContainer):
            if len(word) < best_global_length:
                best_global_length = len(word)
                best_global_index = i
                
        
        root = [{}, best_global_index, best_global_length]
        
        
        for i, word in enumerate(wordsContainer):
            curr_node = root
            curr_len = len(word)
            
            
            for j in range(curr_len - 1, -1, -1):
                char = word[j]
                
               
                if char not in curr_node[0]:
                    curr_node[0][char] = [{}, i, curr_len]
                
                curr_node = curr_node[0][char]
                
                
                if curr_len < curr_node[2]:
                    curr_node[1] = i
                    curr_node[2] = curr_len
                    
      
        result = []
        for query in wordsQuery:
            curr_node = root
            curr_len = len(query)
            
            for j in range(curr_len - 1, -1, -1):
                char = query[j]
                if char in curr_node[0]:
                    curr_node = curr_node[0][char]
                else:
                    break
            
            result.append(curr_node[1])
            
        return result
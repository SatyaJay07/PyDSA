from collections import defaultdict
import operator
class Solution:
    def topKFrequent(self, words: list[str], k: int)->list[str]:
        dico = defaultdict(int)
        for word in words:
            dico[word] += 1
        sortDico = sorted(dico, key= lambda x : (-dico[x],x))
        return sortDico[:k]
# key= lambda x : (-dico[x],x)  -> -dico[x] for negative key(decreasing order), x is 
# 2nd key parameter used for sorting in alphabetical order (ascending so no negative sign)
words = ["the","day","is","sunny","the","the","the","sunny","is","is"]
k = 4
solution = Solution()
result = solution.topKFrequent(words, k)
print(result)

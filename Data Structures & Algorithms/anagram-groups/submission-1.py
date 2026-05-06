class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)
        for word in strs:
            charCount = [0]*26
            for letter in word:
                charCount[ord(letter)-ord('a')]+=1
            res[tuple(charCount)].append(word)
        return list(res.values())
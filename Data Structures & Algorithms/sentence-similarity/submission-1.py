class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False

        similar_set = set()
        for u, v in similarPairs:
            similar_set.add((u, v))
            similar_set.add((v, u))

        for i in range(len(sentence1)):
            word1 = sentence1[i]
            word2 = sentence2[i]

            if word1 != word2 and (word1, word2) not in similar_set and (word2, word1) not in similar_set:
                return False

        return True
        
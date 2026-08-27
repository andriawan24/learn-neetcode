class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False

        for i in range(len(sentence1)):
            word1 = sentence1[i]
            word2 = sentence2[i]

            if word1 == word2:
                continue

            available = False
            for pair in similarPairs:
                if word1 == pair[0]:
                    if word2 == pair[1]:
                        available = True
                        break
                elif word1 == pair[1]:
                    if word2 == pair[0]:
                        available = True
                        break

            if not available:
                return False

        return True
        
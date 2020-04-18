class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = {}

        for word in strs:
            if word in words.keys():
                words[word].append(word)
            else:
                lw = list(word)
                w = "".join(sorted(lw))

                if w in words.keys():
                    words[w].append(word)
                else:
                    words.update({w: [word]})

        anagrams = []

        for l in words.values():
            anagrams.append(l)

        return anagrams

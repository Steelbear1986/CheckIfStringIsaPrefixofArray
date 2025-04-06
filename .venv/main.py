class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        ansver=''
        for i in range(len(words)):
            ansver+=words[i]
            if ansver==s:
                return True
        return False
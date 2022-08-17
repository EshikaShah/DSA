class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        s = set()
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        for word in words:
            a = ""
            for letter in word:
                a += morse[ord(letter) - 97]
            s.add(a)
        return len(s)
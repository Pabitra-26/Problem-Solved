# Problem name: Unique Morse Code Words
# Description: International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes,
# as follows: "a" maps to ".-", "b" maps to "-...", "c" maps to "-.-.", and so on.
# For convenience, the full table for the 26 letters of the English alphabet is given below:
# [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        di=dict()
        di['a']=".-"
        di['b']="-..."
        di['c']="-.-."
        di['d']="-.."
        di['e']="."
        di['f']="..-."
        di['g']="--."
        di['h']="...."
        di['i']=".."
        di['j']=".---"
        di['k']="-.-"
        di['l']=".-.."
        di['m']="--"
        di['n']="-."
        di['o']="---"
        di['p']=".--."
        di['q']="--.-"
        di['r']=".-."
        di['s']="..."
        di['t']="-"
        di['u']="..-"
        di['v']="...-"
        di['w']=".--"
        di['x']="-..-"
        di['y']="-.--"
        di['z']="--.."
        s=set()
        for i in words:
            word=""
            for j in i:
                word+=di[j]
            s.add(word)
        return(len(list(s)))
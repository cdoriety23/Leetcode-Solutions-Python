import re


def rem_vowel(string):
    return re.sub("[aeiou]", "", string)

'''

chrassguuioousssussaaaiieeuuuwwwwuuww
aeiou
leetcodeisacommuintyforcoders


'''

print(rem_vowel("chrassguuioousssussaaaiieeuuuwwwwuuww"))#chrssgssssswwwwww
print(rem_vowel("aeiou"))#empty
print(rem_vowel("leetcodeisacommuintyforcoders"))#ltcdscmmntyfrcdrs